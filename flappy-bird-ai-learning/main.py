from config import config
import pygame
import neat
import os
from bird import Bird
from pipe import Pipe
from ground import Ground

pygame.font.init()

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT

IMAGE_PATH = config.IMAGE_PATH
IMAGE_BIRD = config.IMAGE_BIRDS
IMAGE_PIPE = config.IMAGE_PIPE
IMAGE_GROUND = config.IMAGE_GROUND
IMAGE_BACKGROUND = config.IMAGE_BACKGROUND
STAT_FONT = config.STAT_FONT
NEAT_CONFIG_PATH = config.NEAT_CONFIG_PATH

pygame.display.set_caption("Flappy Bird")

gen = 0


def draw_window(window, birds, pipes, ground, score):
    global gen
    if gen == 0:
        gen = 1
    window.blit(IMAGE_BACKGROUND, (0, 0))

    for pipe in pipes:
        pipe.draw(window)

    # bird score
    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    window.blit(score_label, (WINDOW_WIDTH - score_label.get_width() - 15, 10))

    # how many generations
    score_label = STAT_FONT.render("Gens: " + str(gen - 1), 1, (255, 255, 255))
    window.blit(score_label, (10, 10))

    # alive
    score_label = STAT_FONT.render("Alive: " + str(len(birds)), 1, (255, 255, 255))
    window.blit(score_label, (10, 50))

    ground.draw(window)
    for bird in birds:
        bird.draw(window)

    pygame.display.update()


def main(genomes, config):
    global gen
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    gen += 1

    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    ground = Ground(730)
    pipes = [Pipe(600)]
    score = 0

    clock = pygame.time.Clock()

    run_game = True
    while run_game and len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()
                quit()
                break

        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_index = 1

        for x, bird in enumerate(birds):
            ge[x].fitness += 0.1
            bird.move()

            output = nets[x].activate((bird.y,
                                       abs(bird.y - pipes[pipe_index].height),
                                       abs(bird.y - pipes[pipe_index].bottom)))

            if output[0] > 0.5:
                bird.jump()

        ground.move()

        rem = []
        add_pipe = False
        for pipe in pipes:
            pipe.move()
            for bird in birds:
                if pipe.collide(bird):
                    ge[birds.index(bird)].fitness -= 1
                    nets.pop(birds.index(bird))
                    ge.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            score += 1
            # can add this line to give more reward for passing through a pipe (not required)
            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(WINDOW_WIDTH))

        for r in rem:
            pipes.remove(r)

        for bird in birds:
            if bird.y + bird.image.get_height() - 10 >= 730 or bird.y < -50:
                nets.pop(birds.index(bird))
                ge.pop(birds.index(bird))
                birds.pop(birds.index(bird))

        draw_window(window, birds, pipes, ground, score)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    statistics = neat.StatisticsReporter()
    population.add_reporter(statistics)

    winner = population.run(main, 100)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, NEAT_CONFIG_PATH)
    run(config_path)

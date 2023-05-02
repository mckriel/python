import pygame
import os

pygame.font.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

IMAGE_PATH = 'image'

IMAGE_BIRDS = [pygame.transform.scale2x(pygame.image.load(os.path.join(IMAGE_PATH, 'bird1.png'))),
               pygame.transform.scale2x(pygame.image.load(os.path.join(IMAGE_PATH, 'bird2.png'))),
               pygame.transform.scale2x(pygame.image.load(os.path.join(IMAGE_PATH, 'bird3.png')))]
IMAGE_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join(IMAGE_PATH, 'pipe.png')))
IMAGE_GROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(IMAGE_PATH, 'base.png')))
IMAGE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(IMAGE_PATH, 'bg.png')))

STAT_FONT = pygame.font.SysFont('comicsans', 50)

NEAT_CONFIG_PATH = './config/neat-config.txt'

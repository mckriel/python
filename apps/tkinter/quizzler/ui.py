from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzy')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Question text',
            fill=THEME_COLOR,
            font=('Arial', 16, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_true = PhotoImage(file='images/true.png')
        self.button_true = Button(image=image_true, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        image_false = PhotoImage(file='images/false.png')
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

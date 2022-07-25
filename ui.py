import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # screen
        self.window = tkinter.Tk()
        self.window.title("IT-Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = tkinter.Canvas(width=300, height=240, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     120,
                                                     width=280,
                                                     text="hello",
                                                     fill=THEME_COLOR,
                                                     font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # label
        self.score = tkinter.Label(text="Score: ")
        self.score.config(bg=THEME_COLOR, fg="white", font=("arial", 15, "bold"))
        self.score.grid(column=0, row=0, columnspan=2)

        # calling function
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You're score is: {self.quiz.score}")
            self.canvas.config(bg="yellow")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




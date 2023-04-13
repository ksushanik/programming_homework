import tkinter as tk
from typing import List


class Question:
    def __init__(self, prompt: str, choices: List[str], correct_answers: List[int]):
        self.prompt = prompt
        self.choices = choices
        self.correct_answers = correct_answers


class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.question_number = 0
        self.score = 0

        self.question_text = tk.Label(master, text="", font=("Arial", 16), wraplength=600)
        self.question_text.pack(pady=10)

        self.selected_answer = tk.IntVar()
        self.answer_buttons = []
        frame = tk.Frame(master)
        frame.pack()

        for i in range(len(self.questions[0].choices)):
            button = tk.Radiobutton(frame, text="", variable=self.selected_answer, value=i)
            self.answer_buttons.append(button)
            button.grid(row=i, column=0, sticky="w", padx=10, pady=5)

        self.answer_button = tk.Button(master, text="Ответить", command=self.check_answer)
        self.answer_button.pack(pady=5)

        self.score_label = tk.Label(master, text="")
        self.score_label.pack(pady=10)

        self.show_question()

        # установка фиксированного размера окна и запрет на изменение его размера
        master.geometry("600x300")
        master.resizable(False, False)

    def show_question(self):
        question = self.questions[self.question_number]
        self.question_text.configure(text=question.prompt)

        for i in range(len(question.choices)):
            self.answer_buttons[i].configure(text=question.choices[i])

    def check_answer(self):
        question = self.questions[self.question_number]
        selected_answer = self.selected_answer.get()
        if selected_answer in question.correct_answers:
            self.score += 1

        self.question_number += 1
        if self.question_number == len(self.questions):
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        self.question_text.configure(text=f"Результат: {self.score}/{len(self.questions)}")
        self.answer_button.pack_forget()
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.configure(text=f"Процент правильных ответов: {self.score / len(self.questions) * 100:.2f}%")


def read_questions(filename: str) -> List[Question]:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    list_questions = []
    prompt = ""
    choices = []
    correct_answers = []
    for line in lines:
        line = line.strip()
        if line.startswith("q:"):
            if prompt:
                list_questions.append(Question(prompt, choices, correct_answers))
            prompt = line[2:]
            choices = []
            correct_answers = []
        elif line.startswith("+"):
            correct_answers.append(len(choices))
            choices.append(line[1:])
        else:
            choices.append(line)
    if prompt:
        list_questions.append(Question(prompt, choices, correct_answers))
    return list_questions


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Тест")

    text_questions = read_questions("quiz.txt")
    app = QuizApp(root, text_questions)

    app.master.mainloop()

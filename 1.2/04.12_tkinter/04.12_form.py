import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Анкета по литературе")

fields = {
    "Введите свое имя:": tk.Entry,
    "Выберите свои любимые жанры:": tk.Checkbutton,
    "Выберите своих любимых авторов:": tk.Checkbutton
}

options = [
    ("Классика", tk.IntVar()),
    ("Фантастика", tk.IntVar()),
    ("Детектив", tk.IntVar()),
    ("Роман", tk.IntVar()),
    ("Приключения", tk.IntVar()),
    ("Лев Толстой", tk.IntVar()),
    ("Федор Достоевский", tk.IntVar()),
    ("Джоан Роулинг", tk.IntVar()),
    ("Эрих Мария Ремарк", tk.IntVar()),
    ("Агата Кристи", tk.IntVar())
]

for text, field_type in fields.items():
    if field_type == tk.Entry:
        tk.Label(root, text=text).pack()
        fields[text] = field_type(root)
        fields[text].pack()
    else:
        tk.Label(root, text=text).pack()
        for option, var in options:
            if (text == "Выберите свои любимые жанры:" and options.index((option, var)) < 5) or \
                    (text == "Выберите своих любимых авторов:" and options.index((option, var)) >= 5):
                tk.Checkbutton(root, text=option, variable=var).pack()


def save_results():
    name = fields["Введите свое имя:"].get()
    genres = [option[0] for option in options[:5] if option[1].get()]
    authors = [option[0] for option in options[5:] if option[1].get()]

    with open("results.txt", "a", encoding='utf8') as f:
        f.write(f"Имя: {name}\n")
        f.write("Любимые жанры: " + ", ".join(genres) + "\n")
        f.write("Любимые авторы: " + ", ".join(authors) + "\n\n")

    fields["Введите свое имя:"].delete(0, tk.END)
    for option_, var_ in options:
        var_.set(0)

    messagebox.showinfo("Результаты сохранены", "Ваши ответы были сохранены в файле 'results.txt'.")


tk.Button(root, text="Сохранить результаты", command=save_results).pack()
tk.Button(root, text="Выход", command=root.destroy).pack()

root.mainloop()

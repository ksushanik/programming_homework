import tkinter as tk


def add():
    try:
        num1 = float(num1_field.get())
        num2 = float(num2_field.get())
        result = num1 + num2
        result_field.delete(0, tk.END)  # Очистить поле для результата
        result_field.insert(0, result)  # Вставить результат в поле для результата
    except ValueError:
        result_field.delete(0, tk.END)
        result_field.insert(0, "Неверный ввод")


# Создать главное окно
root = tk.Tk()
root.title("Сложение двух чисел")

# Создать виджеты
num1_label = tk.Label(root, text="Первое число:")
num1_field = tk.Entry(root)
num2_label = tk.Label(root, text="Второе число:")
num2_field = tk.Entry(root)
add_button = tk.Button(root, text="Сложить", command=add)
result_label = tk.Label(root, text="Результат:")
result_field = tk.Entry(root)

# Добавить виджеты на окно
num1_label.grid(row=0, column=0)
num1_field.grid(row=0, column=1)
num2_label.grid(row=1, column=0)
num2_field.grid(row=1, column=1)
add_button.grid(row=2, column=0, columnspan=2)
result_label.grid(row=3, column=0)
result_field.grid(row=3, column=1)

# Запустить главный цикл
root.mainloop()

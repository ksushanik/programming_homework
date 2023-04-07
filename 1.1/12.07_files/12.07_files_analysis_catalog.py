# Написать программу анализа файлов в заданном каталоге.
# 1. Ввести с клавиатуры путь к каталогу
# 2. Организовать цикл просмотра каталога
# 3. Подсчитать количество текстовых файлов (с расширениями .docx, .txt, .dat)
# 4. Подсчитать количество графических файлов (с расширениями .jpg, .png, .jpeg, .gif)
# 5. Подсчитать количество табличных файлов (с расширением .xlsx)
# 6. Записать в отдельный файл полученную статистику.

from pathlib import Path

uset_path = Path(input("Введите путь к каталогу: "))

count_dict = {
    ".docx": 0,
    ".txt":  0,
    ".dat":  0,
    ".jpg":  0,
    ".png":  0,
    ".jpeg": 0,
    ".gif":  0,
    ".xlsx": 0
}

for file in Path(uset_path).rglob("*.*"):
    if file.suffix in count_dict:
        count_dict[file.suffix] += 1

with open('out_static.txt', 'w', encoding='windows-1251') as f:
    text = f"Количество текстовых файлов (с расширениями .docx, .txt, .dat): " \
           f"{sum((count_dict['.docx'], count_dict['.txt'], count_dict['.dat']))}"
    graph = f"Количество графических файлов (с расширениями .jpg, .png, .jpeg, .gif): " \
            f"{sum((count_dict['.jpg'], count_dict['.png'], count_dict['.jpeg'], count_dict['.gif']))}"
    table = f"Количество табличных файлов (с расширением .xlsx): " \
            f"{count_dict['.xlsx']}"
    f.write(f"{text}\n{graph}\n{table}")

# C:\Users\Ksusha\Documents

# Необходимо взять отрывок пьесы "Ревизор", прикреплённый к заданию. Сохранить его в
# виде файла с расширением txt и разобрать по ролям.
import re
from collections import defaultdict

space_smbl = r"\n\s{2,}|\xa0"
author_phrase = r"(?<=\()[^\)]+(?=\))"
del_author_phrase = r"\([^\)]+\)"
role_pattern = r"^[А-Яа-я\w\s]+(?=:)"
text_pattern = r"(?<=:).+"

with open('roles.txt', encoding='utf-8') as f:
    # удаляем лишние пробелы, в том числе неразрывные
    piece = re.sub(space_smbl, " ", f.read()).split('\n')

    # создаем список с фразами автора
    author = []
    for line in piece:
        if re.search(author_phrase, line):
            author.extend(re.findall(author_phrase, line))

    # разбиваем текст на связанные фразы
    text_lines = [piece[i] for i in range(piece.index('textLines:') + 1, len(piece))]

# создаем словарь, с распределенными по ролям, фразами
roles_dict = defaultdict(list)
for idx, line in enumerate(text_lines, 1):
    role = re.search(role_pattern, line).group()
    text = re.search(text_pattern, line).group()
    text = re.sub(del_author_phrase, '', text)
    roles_dict[role].append(f"{idx}) {text.lstrip()}\n")

# записываем полученные данные в файл согласно шаблону в задании
with open('roles_out.txt', 'w', encoding='utf-8') as f:
    for key in roles_dict:
        f.write(f'{key}:\n')
        for value in roles_dict[key]:
            f.write(f'{value}')
        f.write('\n')
    f.write('Слова автора:\n')
    for phrase in author:
        f.write(f'{phrase}\n')

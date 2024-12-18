import string

# Чтение из файла input.txt и запись в output.txt
with open('input.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Проверка наличия знаков пунктуации в строке
        if any(char in string.punctuation for char in line):
            outfile.write(line)
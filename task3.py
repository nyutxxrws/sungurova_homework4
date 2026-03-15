def append_to_file(text, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"\nЧётные строки файла {filename}:")
    for i, line in enumerate(lines, 1):
        if i % 2 == 0:
            print(line.strip())
text = input("Добавить в файл: ")
f = input("Название файла: ")
append_to_file(text, f)
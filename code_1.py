#Функция для выбора данных из файла
def choose_data_from_file(file_path, line_number):
    with open(file_path, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()
        if line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return None

# Функция для записи данных в файл
def write_data_to_file(file_path, data):
    with open(target_file_path, 'a', encoding='utf-8') as target_file:
        target_file.write(data + '\n')

# Выбор пользователем строки для копирования
file_path = 'source_file.txt'
line_number = int(input("Введите номер строки, которую нужно скопировать: "))
target_file_path = 'target_file.txt'
selected_data = choose_data_from_file(file_path, line_number)

# Запись данных в целевой файл
if selected_data:
    write_data_to_file(target_file_path, selected_data)
    print("Данные успешно скопированы в указанный файл.")
else:
    print("Указанная строка не существует в выбранном файле.")
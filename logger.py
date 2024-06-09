from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    elif var == 2:
         with open('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()        
        # data_first_list = []
        # j = 0
        # for i in range(len(data_first)):
        #     if data_first[1] == '\n' or i == len(data_first) - 1:
        #         data_first_list.append(''.join(data_first[j:i+1]))
        #         j = i
        # print(''.join(data_first_list))
        for line in data_first:
            print(line.strip())

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        # print(*data_second)
        for line in data_second:
            print(line.strip())

def search_data():
    name = input("Введите имя для поиска: ")
    surname = input("Введите фамилию для поиска: ")
    found = False

    print('Ищу данные в 1 файле: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        for i in range(0, len(data_first), 5):
            if name in data_first[i] and surname in data_first[i+1]:
                print(''.join(data_first[i:i+5]).strip())
                found = True

    print('Ищу данные в 2 файле: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        for line in data_second:
            if name in line and surname in line:
                print(line.strip())
                found = True

    if not found:
        print("Данные не найдены")

def delete_data():
    name = input("Введите имя для удаления: ")
    surname = input("Введите фамилию для удаления: ")
    found = False

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        for i in range(0, len(data_first), 5):
            if name in data_first[i] and surname in data_first[i+1]:
                found = True
            else:
                f.write(''.join(data_first[i:i+5]))

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        for line in data_second:
            if name in line and surname in line:
                found = True
            else:
                f.write(line)

    if found:
        print("Данные успешно удалены")
    else:
        print("Данные не найдены")

def update_data():
    name = input("Введите имя для обновления: ")
    surname = input("Введите фамилию для обновления: ")
    found = False

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        for i in range(0, len(data_first), 5):
            if name in data_first[i] and surname in data_first[i+1]:
                print("Введите новые данные")
                new_name = name_data()
                new_surname = surname_data()
                new_phone = phone_data()
                new_address = address_data()
                f.write(f"{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n")
                found = True
            else:
                f.write(''.join(data_first[i:i+5]))

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        for line in data_second:
            if name in line and surname in line:
                print("Введите новые данные")
                new_name = name_data()
                new_surname = surname_data()
                new_phone = phone_data()
                new_address = address_data()
                f.write(f"{new_name};{new_surname};{new_phone};{new_address}\n")
                found = True
            else:
                f.write(line)

    if found:
        print("Данные успешно обновлены")
    else:
        print("Данные не найдены")

from logger import input_data, print_data, search_data, delete_data, update_data

def interface():
    # print('Добрый день! Вы попали на специальный бот-справочник \n 1 - запись данных \n 2 - вывод данных')
    # command = int(input('Введите число: '))

    # while command != 1 and command != 2:
    #     print('Неправильный ввод')
    #     command = int(input('Введите число: '))

    # if command == 1:
    #     input_data()
    # elif command == 2:
    #     print_data()

    while True:
        print('Добрый день! Вы попали на специальный бот-справочник')
        print('1 - запись данных')
        print('2 - вывод данных')
        print('3 - поиск данных')
        print('4 - удаление данных')
        print('5 - обновление данных')
        print('6 - выход')
        try:
        # command = int(input('Введите число: '))
            command = input('Введите число: ').strip()
            if command.isdigit():
                command = int(command)
                if command == 1:
                    input_data()
                elif command == 2:
                    print_data()
                elif command == 3:
                    search_data()
                elif command == 4:
                    delete_data()
                elif command == 5:
                    update_data()
                elif command == 6:
                    break
                else:
                    print('Неправильный ввод')

            else:
                print('Неправильный ввод, введите число от 1 до 6')
        except ValueError:
            print('Неправильный ввод, введите число от 1 до 6')

if __name__ == '__main__':
    interface()



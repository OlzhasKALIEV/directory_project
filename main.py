from directory import create_database, create

if __name__ == '__main__':
    create_database()

    while True:
        print("Номера команд: \n1 - добавить запись \n2 - выход")
        user_input = input('Введите номер команды: ')

        if user_input == '1':
            create()
        elif user_input == '2':
            break
        else:
            print('Неверная команда')
import os
from directory import create_database, create, get_all, get_id, update_id

if __name__ == '__main__':
    if not os.path.exists('contacts.db'):
        create_database()

    while True:
        print("Номера команд: "
              "\n1 - Добавить запись "
              "\n2 - Отобразить все данные "
              "\n3 - Отобразить данные по номеру ID"
              "\n4 - Изменить данные по номеру ID"
              "\n5 - Выход")
        user_input = input('Введите номер команды: ')

        if user_input == '1':
            create()
            continue
        if user_input == '2':
            get_all()
        if user_input == '3':
            get_id()
            continue
        if user_input == '4':
            update_id()
            continue
        if user_input == '5':
            break
        else:
            print('Неверная команда')
from flask import Flask
from database import db, Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def create_database():
    with app.app_context():
        db.create_all()
    return 'Database created successfully'


def create():
    with app.app_context():
        last_name = input('Введите Фамилию: ')
        first_name = input('Введите Имя: ')
        middle_name = input('Введите Отчество: ')
        organization = input('Наименование Организации: ')
        work_phone = input('Рабочий номер телефона: ')
        personal_phone = input('Личный номер телефона: ')

        contact = Contact(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            organization=organization,
            work_phone=work_phone,
            personal_phone=personal_phone,
        )
        db.session.add(contact)
        db.session.commit()

    print('Запись успешно создана!!!')


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
            print('Invalid command')

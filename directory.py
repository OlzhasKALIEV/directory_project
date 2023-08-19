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


def get_all():
    with app.app_context():
        contacts = Contact.query.all()

    if contacts:
        for contact in contacts:
            print(f'ID записи: {contact.id_directory}')
            print(f'Фамилия: {contact.last_name}')
            print(f'Имя: {contact.first_name}')
            print(f'Отчество: {contact.middle_name}')
            print(f'Наименование Организации: {contact.organization}')
            print(f'Рабочий номер телефона: {contact.work_phone}')
            print(f'Личный номер телефона: {contact.personal_phone}')
            print('---------------------------------')
    else:
        print('Нет данных')


def get_id():
    id_directory = int(input("Введите номер ID записи: "))
    with app.app_context():
        contacts = Contact.query.get(id_directory)

    if contacts:
        print(f'ID записи: {contacts.id_directory}')
        print(f'Фамилия: {contacts.last_name}')
        print(f'Имя: {contacts.first_name}')
        print(f'Отчество: {contacts.middle_name}')
        print(f'Наименование Организации: {contacts.organization}')
        print(f'Рабочий номер телефона: {contacts.work_phone}')
        print(f'Личный номер телефона: {contacts.personal_phone}')
        print('---------------------------------')
    else:
        print('Нет данных')


def update_id():
    id_directory = int(input("Введите номер ID записи: "))
    with app.app_context():
        contact = Contact.query.get(id_directory)

        if contact:
            print(f'ID записи: {contact.id_directory}')
            print(f'Фамилия: {contact.last_name}')
            print(f'Имя: {contact.first_name}')
            print(f'Отчество: {contact.middle_name}')
            print(f'Наименование Организации: {contact.organization}')
            print(f'Рабочий номер телефона: {contact.work_phone}')
            print(f'Личный номер телефона: {contact.personal_phone}')
            print('---------------------------------')
            print("Какие данные необходимо изменить?"
                  "\n1 - Фамилию"
                  "\n2 - Имя"
                  "\n3 - Отчество"
                  "\n4 - Наименование Организации"
                  "\n5 - Рабочий номер телефона"
                  "\n6 - Личный номер телефона")

            team_number = int(input("Введите номер: "))

            if team_number == 1:
                last_name = input('Введите новую Фамилию: ')
                contact.last_name = last_name
                db.session.commit()

            if team_number == 2:
                first_name = input('Введите новое Имя: ')
                contact.first_name = first_name
                db.session.commit()

            if team_number == 3:
                middle_name = input('Введите новое Отчество: ')
                contact.middle_name = middle_name
                db.session.commit()

            if team_number == 4:
                organization = input('Введите новое Наименование Организации: ')
                contact.organization = organization
                db.session.commit()

            if team_number == 5:
                work_phone = input('Введите новый Рабочий номер телефона: ')
                contact.work_phone = work_phone
                db.session.commit()

            if team_number == 6:
                personal_phone = input('Введите новый Личный номер телефона: ')
                contact.personal_phone = personal_phone
                db.session.commit()

            print('Запись успешно обновлена!!!')
        else:
            print('Нет данных')
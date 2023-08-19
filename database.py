from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = 'directory'

    id_directory = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    organization = db.Column(db.String(100))
    work_phone = db.Column(db.String(12))
    personal_phone = db.Column(db.String(12))


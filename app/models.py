import datetime
from app import db


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.datetime.now)
    nome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    assunto = db.Column(db.String(50), nullable=True)
    menssagem = db.Column(db.String(50), nullable=True)
    respondido = db.Column(db.Integer, default=0)

    
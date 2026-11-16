from datetime import date
from flask_sqlalchemy import SQLAlchemy
from argon2 import PasswordHasher

db = SQLAlchemy()
ph = PasswordHasher()

class Gestora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def definir_senha(self, senha_plana: str):
        self.senha_hash = ph.hash(senha_plana)

    def verificar_senha(self, senha_plana: str) -> bool:
        return ph.verify(self.senha_hash, senha_plana)

class Insumo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    quantidade_minima = db.Column(db.Float, nullable=False, default=3.0)
    validade = db.Column(db.Date, nullable=False)

    @property
    def alerta_critico(self) -> bool:
        return self.quantidade <= self.quantidade_minima or self.validade <= date.today()

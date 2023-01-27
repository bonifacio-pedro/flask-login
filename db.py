from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
Base = declarative_base() # Utilizado para mapear qual base(tabela) será utilizada
context = CryptContext(schemes=['argon2']) # Utilizando o algoritmo Argon2 para hash

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(86), nullable=False)
    passwd = Column(String(25), nullable=False)

    def __init__(self,username,passwd):
        """
        Instancia do usuário, com o hash para senha
        """
        self.username = username
        self.passwd = context.hash(passwd)

    def verify_passwd(self,passwd):
        """
        Verificando a senha, se for igual o hash.
        """
        return context.verify(passwd,self.passwd)

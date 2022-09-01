from servicos import Servicos
from log import LogMixin

class Pessoa():

    def __init__(self, nome: str, cpf: str, telefone: str):
        self.nome = nome
        self._cpf = cpf
        self.telefone = telefone

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        self._cpf = valor
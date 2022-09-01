from datetime import datetime
from cliente import Cliente
from funcionario import Funcionario 

class Reserva:
   
    def __init__(self, data_inicial: datetime.date, data_final: datetime.date, cliente: Cliente, funcionario: Funcionario):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.cliente = cliente
        self.funcionario = funcionario

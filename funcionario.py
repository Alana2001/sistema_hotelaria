from servicos import Servicos
from pessoa import Pessoa
from log import LogMixin

class Funcionario(Pessoa):
 
    def __init__(self, nome: str, cpf: str, telefone: str):
        super().__init__(nome, cpf, telefone)
        self.trabalhando = True

    def parar_de_trabalhar(self) -> None:
      
        self.trabalhando = False

    def voltar_a_trabalhar(self) -> None:
       
        self.trabalhando = True
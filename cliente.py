from pessoa import Pessoa
from servicos import Servicos
from log import LogMixin

class Cliente(Pessoa, LogMixin):
  
    def __init__(self, nome: str, cpf: str, telefone: str):
        super().__init__(nome, cpf, telefone)

        self.quartos_reservados = []
        self.consumidos = []
        self.servicos = []

    def pagar_diaria(self) -> None:
       
        total = sum([x.valor_diaria for x in self.quartos_reservados])
        if total > 0:
            print(f'Foi realizado o pagamento de R$ {total} da(s) diária(s)')
            self.log_info(f'Cliente - {self.nome} pagou um total de R${total} de diaria')
            return

        print('Você não realizou nenhuma reserva')

    def consumir(self, quarto_id: int, item: str) -> None:
        
        if quarto_id >= len(self.quartos_reservados):
            print('Não encontramos esse quarto')
            self.log_erro(f'Cliente - {self.nome} tentou acessar um quarto inexistente ')
            return

        if item in self.quartos_reservados[quarto_id].itens:
            if self.quartos_reservados[quarto_id].itens[item]['quantidade'] >= 1:
                self.quartos_reservados[quarto_id].itens[item]['quantidade'] -= 1
                print(f'Foi consumido 1 {item} com sucesso')
                self.log_info(
                    f'Cliente - {self.nome} consumiu um {item} de R${self.quartos_reservados[quarto_id].itens[item]["valor"]} ')
                return
        print(f'Não foi possível consumir {item}')

    def solicitar_servico(self, servico: Servicos) -> None:
       
        if not isinstance(servico, Servicos):
            self.log_erro(f'Cliente {self.nome} solicitou um cliente que nao existe')
            raise TypeError('Servico solicitado não é um Enum')

        self.log_info(f'Cliente - {self.nome} fez um servico pelo valor de R${servico.value}')
        print(f'Serviço realizado com o custo de R${servico.value}')

    def desocupar_quarto(self, quarto_id: int) -> None:
       
        if quarto_id >= len(self.quartos_reservados):
            print('Não foi possivel desocupar esse quarto')
            return

        self.log_info(f'Cliente - {self.nome} desocupou o quarto de num {quarto_id} dele')
        print(f'{self.nome} desocupou um quarto')
        self.quartos_reservados.pop(quarto_id).fazer_manutencao()

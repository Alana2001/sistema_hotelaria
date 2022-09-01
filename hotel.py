from cliente import Cliente
from funcionario import Funcionario
from quartos import QuartoLuxo, QuartoCasal, QuartoSimples, QuartoDuplo
from log import LogMixin
import random


class Hotel(LogMixin):

    def __init__(self):
        self.clientes = [
            Cliente('Alana', '459445421', '89999055383'),
            Cliente('Bira', '5449879545', '89999820877')
        ]
        self.quartos = {
            'luxo': [QuartoLuxo(1), QuartoLuxo(2)],
            'casal': [QuartoCasal(3), QuartoCasal(4)],
            'simples': [QuartoSimples(5), QuartoSimples(6)],
            'duplo': [QuartoDuplo(7), QuartoDuplo(8)]
        }
        self.funcionarios = [
            Funcionario('Vilson', '24574522', '899994216885'),
            Funcionario('Leandro', '24421582', '899990526418')
        ]

    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
       
        self.funcionarios.append(funcionario)
        self.log_info(f'Adicionado funcionário com sucesso')

    def cadastrar_cliente(self, cliente: Cliente) -> None:
        

        if not isinstance(cliente, Cliente):
            self.log_erro('Tentativa de cadastrar um objeto que não é Cliente')
            print('Não foi possível cadastrar esse cliente')
            return

        if cliente in self.clientes:
            print('Cliente já está cadastrado')
            return

        self.clientes.append(cliente)
        print(f'Cliente {cliente.nome} cadastrado com sucesso')
        self.log_info(f'Cliente - {cliente.nome} cadastrado com sucesso')

    def autenticar(self, cliente: Cliente) -> bool:
        
        if not isinstance(cliente, Cliente):
            self.log_erro(f'Tentativa de login por objeto diferente de cliente')
            return False

        if not cliente in self.clientes:
            self.cadastrar_cliente(cliente)
            print(f'Foi preciso cadastrar o {cliente.nome} no hotel antes de autenticar')

        self.log_info(f'Cliente - {cliente.nome} autenticado com sucesso')
        return True

    def encontrar_quarto_disponivel(self, data_inicial: str, data_final: str, tipo_quarto: str,
                                    cliente: Cliente) -> None:
        
        if not isinstance(cliente, Cliente):
            raise TypeError('Utilize um objeto da classe cliente')

        try:
            # Pega um funcionário aleatório para ser responsável por esse quarto caso alugado
            funcionario = self.funcionarios[random.randint(0, len(self.funcionarios) - 1)]
            for quarto in self.quartos[tipo_quarto]:

                if quarto.reservar(data_inicial=data_inicial, data_final=data_final, cliente=cliente,
                                   funcionario=funcionario):
                    print(f'Foi realizada a reserva do quarto ({tipo_quarto}) com sucesso!')

                    self.log_info(
                        f'{cliente.nome} realizou a reserva com sucesso para a data de {data_inicial} e {data_final}\n'
                        f'para o quarto({tipo_quarto}) de numero: {quarto.numero}, funcionario: {funcionario.nome}')
                    return
        except KeyError:
            self.log_erro('Quarto procurado nao existe')
            raise KeyError('Tipo de quarto nao existe')
        except Exception as e:
            self.log_erro(f'Ocorreu um erro {e}')
            raise ValueError('Erro ao encontrar um quarto')

        print(f'Não encontramos nenhum quarto tipo({tipo_quarto}) para esse intervalo de data :/')
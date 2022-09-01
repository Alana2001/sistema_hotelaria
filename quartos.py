from datetime import datetime
from cliente import Cliente
from funcionario import Funcionario
from reserva import Reserva


class Quarto():
   
    def __init__(self, numero: int = 100):
        self.numero = numero
        self.reserva = []
        self.itens = {
            'refrigerante': {
                'valor': 7,
                'quantidade': 5
            },
            'cerveja': {
                'valor': 10,
                'quantidade': 15
            }
        }

    def fazer_manutencao(self) -> None:
     
        self.itens = {
            'refrigerante': {
                'valor': 7,
                'quantidade': 5
            },
            'cerveja': {
                'valor': 10,
                'quantidade': 15
            }
        }
        print('Produtos reabastecidos')

    def _data_disponivel(self, data_inicial: datetime, data_final: datetime) -> bool:
      
        if data_inicial >= data_final:
            return False

        for reserva in self.reserva:
            if reserva.data_inicial == data_inicial or reserva.data_final == data_final:
                return False
            if data_inicial > reserva.data_inicial and data_final < reserva.data_final:
                return False

        return True

    def reservar(self, data_inicial: str, data_final: str, cliente: Cliente, funcionario: Funcionario = None) -> bool:
        
        if not isinstance(data_inicial, str):
            raise TypeError('"data_inicial" precisa ser (str)')

        if not isinstance(data_final, str):
            raise TypeError('"data_final" precisa ser (str)')

        try:
            data_inicial_convertido = datetime.strptime(data_inicial, '%d/%m/%Y').date()
            data_final_convertido = datetime.strptime(data_final, '%d/%m/%Y').date()
            if self._data_disponivel(data_inicial_convertido, data_final_convertido):
                self.reserva.append(
                    Reserva(data_inicial_convertido, data_final_convertido, cliente, funcionario)
                )
                cliente.quartos_reservados.append(self)

                print(
                    f'Reservar para o dia inicial: {data_inicial} com encerramento para o dia: {data_final} realizada com sucesso')
                return True
        except Exception as e:
            raise ValueError('Valor inválido para data')
        return False


class QuartoSimples(Quarto):
    valor_diaria = 150

class QuartoDuplo(Quarto):
    valor_diaria = 200

class QuartoCasal(Quarto):
    valor_diaria = 300

class QuartoLuxo(Quarto):
    valor_diaria = 450
from hotel import Hotel
from cliente import Cliente
from funcionario import Funcionario 
from servicos import Servicos

alana = Cliente('Alana', '459445421', '8999055634')
bira = Cliente('Bira', '5449879545', '8955267216')

hotel = Hotel()
hotel.autenticar('sla')
hotel.cadastrar_cliente(alana)
hotel.cadastrar_cliente(bira)
hotel.encontrar_quarto_disponivel('02/09/2022', '07/09/2022', 'luxo', alana)
hotel.encontrar_quarto_disponivel('02/09/2022', '07/09/2022', 'luxo', bira)
alana.pagar_diaria()
bira.pagar_diaria()
hotel.autenticar(alana)
alana.solicitar_servico(Servicos.limpar_quarto)
alana.desocupar_quarto(0)
hotel.encontrar_quarto_disponivel('07/09/2022', '14/09/2022', 'simples', alana)
alana.pagar_diaria()
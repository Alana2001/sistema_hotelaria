class LogMixin:
   
    @staticmethod
    def escrever(mensagem: str) -> None:
      
        with open('log.txt', 'a+') as arquivo:
            arquivo.write(f'{mensagem}\n')

    def log_info(self, mensagem: str) -> None:
      
        self.escrever(f'Info: {mensagem}')

    def log_erro(self, mensagem: str) -> None:
       
        self.escrever(f'Error: {mensagem}')
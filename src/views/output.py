# TODO: preciso de um output padrão



class Output:
    def __init__(self):
          self.total_lenght = 30
    
    def _make_rodape(self, name: str):
        length = len(name)
        padding = self.total_length - length
        print("-" * padding + name)
        print("-" * self.total_lenght)
        
    def _make_transaction_update_form(self):
        pass
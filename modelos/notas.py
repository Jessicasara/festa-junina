class Nota:
    def __init__(self, elegancia, desenvoltura, simpatia, item_reciclavel):
        self.elegancia = elegancia
        self.desenvoltura = desenvoltura
        self.simpatia = simpatia
        self.item_reciclavel = item_reciclavel
        
    def __str__(self):
        return f'Elegancia: {self.elegancia} | Desenvoltura: {self.desenvoltura} | Simpatia: {self.simpatia} | Reciclagem: {self.item_reciclavel}'
    

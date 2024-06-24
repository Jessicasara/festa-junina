class Jurados:

    def __init__(self, nome, area):
        self._nome = nome
        self.area = area        

    def __str__(self):
        return f'Nome: {self._nome} | Especialidade: {self.area}'
    
    def avaliar_aluno(self, aluno, notas):
        aluno._notas.append(notas)


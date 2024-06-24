class Aluno:
    alunos = []

    def __init__(self, nome, sala, categoria):
        self._nome = nome
        self.sala = sala
        self.categoria = categoria
        self._notas = []
        Aluno.alunos.append(self)

    def __str__(self):
        notas_str = "\n".join(str(nota) for nota in self._notas)
        return f'Nome: {self._nome} | Turma: {self.sala} | Categoria: {self.categoria} \nNotas: \n{notas_str}'
    
    
    # @classmethod
    # def listar_alunos(cls):
    #     # print(f'{'Nome aluno'.ljust(25)} | {'Turma'.ljust(25)} | {'Nota'.ljust(25)} | {'Categoria'.ljust(25)}')
    #     for aluno in cls.alunos:
    #         print(f'{aluno._nome.ljust(25)} | {aluno.sala.ljust(25)} | {aluno.nota.ljust(25)} | {aluno.categoria.ljust(25)}')

        
from modelos.jurados import Jurados
from modelos.alunos import Aluno
from modelos.notas import Nota

def cadastrar_aluno():
    while True:
        print('Cadastre o aluno\n')
        nome_aluno = input('Digite o nome do aluno ❣ ')
        sala_aluno = input('Digite a sala do aluno ❣ ')
        categoria_aluno = input('Digite a categoria do aluno (miss ou mister) ❣ ')
        nota_aluno = input('Digite a nota do aluno ❣ ')
        dados_do_aluno = {'nome': nome_aluno, 'sala': sala_aluno, 'categoria': categoria_aluno, 'nota': nota_aluno}
        Aluno.alunos.append(dados_do_aluno)
        
        opcao = input('Você deseja cadastrar um novo aluno? (s/n) ')
        if opcao.lower() == 'n':
            break
        elif opcao.lower() != 's':
            print('Opção inválida')

def cadastrar_jurado():
    while True:
        print('Cadastre o jurado\n')
        nome_jurado = input('Digite o nome do jurado ❣ ')
        area_jurado = input('Digite a especialidade do jurado ❣ ')
        dados_do_jurado = {'nome': nome_jurado, 'especialidade': area_jurado}
        Jurados.jurados.append(dados_do_jurado)

        opcao = input('Você deseja cadastrar um novo jurado? (s/n) ')
        if opcao.lower() == 'n':
            print('Voltar à tela inicial')
            break
        elif opcao.lower() != 's':
            print('Opção inválida')

def registrar_nota():
    aluno_nome = input("Digite o nome do aluno: ")
    jurado_nome = input("Digite o nome do jurado: ")
    
    # Procure os objetos Aluno e Jurado
    aluno = next((aluno for aluno in Aluno.alunos if aluno['nome'] == aluno_nome), None)
    jurado = next((jurado for jurado in Jurados.jurados if jurado['nome'] == jurado_nome), None)
    
    if aluno and jurado:
        valor = float(input(f"Digite a nota do aluno {aluno['nome']} por {jurado['nome']}: "))
        nota = Nota(aluno, jurado, valor)
        Nota.notas.append(nota)
    else:
        print("Aluno ou jurado não encontrados.")

def main():
    while True:
        print("\nSejam Todos Bem-Vindos Ao Nosso Arraial!")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Jurado")
        print("3. Registrar Nota")
        print("4. Listar alunos e jurados")
        print("5. Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            cadastrar_jurado()
        elif opcao == 3:
            registrar_nota()
        elif opcao == 4:
            print("Alunos:", Aluno.alunos)
            print("Jurados:", Jurados.jurados)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == '__main__':
    main()

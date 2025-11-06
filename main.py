from software_treino import *

def menu():
    print("MENU SISTEMA GERADOR DE TREINOS")
    print("================*================")
    print("1) Cadastrar aluno")
    print("2) Alunos cadastrados")
    print("3) Consultar treino")
    print("4) Criar treino")
    print("5) Sair")

def main():
    alunos = []

    while True:
        menu()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            print("\nCadastrar novo auno:")
            nome = input("Nome: ")
            data = input("Data de nascimento (dd/mm/aa): ")
            cpf = input("CPF: ")
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))

            
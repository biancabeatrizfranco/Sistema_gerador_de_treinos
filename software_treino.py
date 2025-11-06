from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Pessoa(ABC):
    __nome : str 
    __dataNascimento : str
    __cpf : int
    peso : float
    altura : float

    def __init__(self, nome, data, cpf, peso, altura ):
        self.__nome = nome 
        self.__dataNascimento = datetime.strptime(data, "%d/%m/%Y")
        self.__cpf = cpf 
        self.peso = peso 
        self.altura = altura

    def calcular_Idade(self):
        data_atual = datetime.now()
        idade = data_atual.year - self.__dataNascimento.year
    # Ajuste se ainda não fez aniversário no ano atual
        if data_atual.month < self.__dataNascimento.month or (data_atual.month == self.__dataNascimento.month and data_atual.day < self.__dataNascimento.day):
            idade -= 1
        return idade

    def __str__(self):
        idade = self.calcular_Idade()
        txt = f"Nome: {self.__nome}\n"
        txt += f"Idade: {idade} anos\n"
        txt += f"Peso: {self.peso}kg\n"
        txt += f"Altura: {self.altura}m\n"
        return txt


class Aluno(Pessoa):
    matricula : int 
    objetivo : str
    treinos: List[str]

    def __init__(self, nome, data, cpf, peso, altura, matricula, objetivo):
        super().__init__(nome, data, cpf, peso, altura)
        self.matricula = matricula
        self.objetivo = objetivo
        self.treinos = []

    def visualizar_Treino(self):
        if len(self.treinos) == 0:
            print("Este aluno não possui treinos cadastrados")
        else:
            for treino in self.treinos:
                print(treino)

        
if __name__ == "__main__":
    p1 =Aluno("Bianca", "24/09/2003", 49057643863, 65.5, 1.60, 554112, "Emagrecer")
    print(p1.visualizar_Treino())





'''4. Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
OBS: por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)
    
    def engordar(self, quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
        self.peso -= quilos
    
    def crescer(self, centimetros):
        self.altura += centimetros

# Programa principal
nome = input("Informe o nome da pessoa: ")
idade = int(input("Informe a idade da pessoa: "))
peso = float(input("Informe o peso da pessoa: "))
altura = float(input("Informe a altura da pessoa: "))

pessoa = Pessoa(nome, idade, peso, altura)

anos_a_envelhecer = int(input("Informe quantos anos a pessoa irá envelhecer: "))
quilos_a_engordar = float(input("Informe quantos quilos a pessoa irá engordar: "))
quilos_a_emagrecer = float(input("Informe quantos quilos a pessoa irá emagrecer: "))

pessoa.envelhecer(anos_a_envelhecer)
pessoa.engordar(quilos_a_engordar)
pessoa.emagrecer(quilos_a_emagrecer)

print("Dados da pessoa:")
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso)
print("Altura:", pessoa.altura)
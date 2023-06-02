'''3. Classe Retângulo: Crie uma classe que modele um retângulo.

Atributos: Lado A, Lado B (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, retornar valor dos lados, calcular área e calcular perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local, 
depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_BA(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornar_BA(self):
        return self.base, self.altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


print("Informe as medidas do local")
base = float(input("base: "))
altura = float(input("altura: "))

retangulo = Retangulo(base, altura)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print("Área do local: %.2f" % area)
print("Perímetro do local: %.2f" % perimetro)

tamanho_piso = float(input("Informe o tamanho do piso em metros quadrados: "))
tamanho_rodape = float(input("Informe o tamanho do rodapé em metros: "))

quantidade_pisos = area / tamanho_piso
quantidade_rodapes = perimetro / tamanho_rodape

print("Quantidade de pisos necessários: %.2f" % quantidade_pisos)
print("Quantidade de rodapés necessários: %.2f" % quantidade_rodapes)

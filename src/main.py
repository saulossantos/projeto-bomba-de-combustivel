class bombaCombustivel:
    def _init_(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        self.quantidadeCombustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        return valor_pagar

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade


class Carro:
    def _init_(self, consumo):
        self.consumo = consumo
        self.nivel_combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro andou {distancia} km.")
        else:
            print("Combustível insuficiente para percorrer a distância desejada.")

    def obterGasolina(self):
        return self.nivel_combustivel

    def adicionarGasolina(self, quantidade):
        self.nivel_combustivel += quantidade


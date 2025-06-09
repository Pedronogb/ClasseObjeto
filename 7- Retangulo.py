class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura


retangulo1 = Retangulo(10, 5)
print(retangulo1.calcularArea())
print("Área do retangulo: ",retangulo1.calcularArea())


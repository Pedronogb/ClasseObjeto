class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valorTotal(self):
        return self.preco * self.quantidade


produto1 = Produto("Biscoito Trakinas", 2.79, 55)
print(produto1.nome)
print("Preço: ", produto1.preco)
print(produto1.quantidade, "unidades")
print()
print(f"{produto1.preco} * {produto1.quantidade}")
print("Valor total: ", produto1.valorTotal())
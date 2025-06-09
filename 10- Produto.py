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
print(f"{produto1.preco} * {produto1.quantidade}")
print("Valor total: ", produto1.valorTotal())
print()
produto2 = Produto("Café Pilão 500g", 49.99, 15)
print(produto2.nome)
print("Preço: ", produto2.preco)
print(produto2.quantidade, "unidades")
print(f"{produto2.preco} * {produto2.quantidade}")
print("Valor total: ", produto2.valorTotal())
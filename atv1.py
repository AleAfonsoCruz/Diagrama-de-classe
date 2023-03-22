class pessoa:
    def __init__(self):
        self.nome = input("Digite seu nome: ")
        self.idade = int(input("Digite sua idade: "))
        self.altura = float(input("Digite sua altura: "))

    def imprimir_informacoes (self):
        print(self.nome)
        print(self.idade) 
        print(self.altura)

pessoa1 = pessoa()
pessoa1.imprimir_informacoes()

pessoa2 = pessoa()
pessoa2.imprimir_informacoes()
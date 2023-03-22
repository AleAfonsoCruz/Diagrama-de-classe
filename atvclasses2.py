class raio:
    def __init__(self):
        print("CALCULAR ÁREA E PERÍMETRO DO CÍRCULO")
        self.raio = float(input("Digite o comprimento do raio: "))

    def res_raio(self):
        self.raio_cal = 3.14*self.raio*self.raio
        print("O resultado do raio é: ",self.raio_cal)
    def res_perimetro(self):
        self.perimetro_cal = 2*3.14*self.raio
        print("O resultado do perímetro é: ",self.perimetro_cal)

resultado = raio()
resultado.res_raio()
resultado.res_perimetro()
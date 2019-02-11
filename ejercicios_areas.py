class Figura():
    def __init__(self):
        pass

    def get_area(self):
        pass
    def get_perimetro(self):
        pass



class Rectangulo(Figura):
    def __init__(self, altura, base):
        self.base = base
        self.altura = altura
        super().__init__()


    def get_area(self):
        return self.base * self.altura
    def get_perimetro(self):
        return self.base * 2 + self.altura * 2


rectangulo1 = Rectangulo(4,5)
print(rectangulo1.get_perimetro())
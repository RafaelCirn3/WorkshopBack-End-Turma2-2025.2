import math
def calcular_raiz_quadrada(numero: float) -> float:
    return math.sqrt(numero)

def arredondamentos(numero: float) -> dict:
    return {
        "piso": math.floor(numero),
        "teto": math.ceil(numero),
        "arredondado": round(numero)
    }


class FiguraGeometrica:
    @staticmethod
    def area_circulo(raio: float) -> float:
        return math.pi * math.pow(raio, 2)

    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        return (base * altura) / 2

    @staticmethod
    def hipotenusa(cateto1: float, cateto2: float) -> float:
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))


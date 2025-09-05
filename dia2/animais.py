class Animal:
    def falar(self):
        return "Som genérico de animal"
    
    
    def apresentar(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos."
    

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"


class Zoologico:
    def __init__(self):
        self.animais = []
    
    def adicionar_animal(self, animal):
        self.animais.append(animal)
    
    def listar_animais(self):
        return [f"{a.apresentar()} Faz: {a.falar()}" for a in self.animais]
    
    def filtrar_por_tipo(self, tipo):
        return [a for a in self.animais if isinstance(a, tipo)]
class Animal:
    def __init__(self, nombre):
        # Asigna el nombre proporcionado al atributo 'nombre'
        self.nombre=nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        # Devuelve el sonido de un perro (ladrido)
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        # Devuelve el sonido de un gato (maullido)
        return "¡Miau!"
perro = Perro("Bobby")
print("El perro se llama: ", perro.nombre," y hace: ", perro.hacer_sonido())

gato = Gato("Garfield")
print("El gato se llama: ", gato.nombre," y hace: ", gato.hacer_sonido())

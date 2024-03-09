class Coche:
    def __init__(self, marca, modelo):
        # Asigna la marca proporcionada al atributo 'marca'
        self.marca="Toyota"
        # Asigna el modelo proporcionado al atributo 'modelo'
        self.modelo="Corolla"

    def conducir(self):
        return f"Conduciendo el {self.marca} {self.modelo}"

coche = Coche('Toyota', 'Corolla')
print(coche.conducir())


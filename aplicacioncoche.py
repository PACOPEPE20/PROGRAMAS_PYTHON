class Coche:
    """Abtraccion de los objetos coche"""
    def __init__(self, gasolina):           #self es el objeto y no cuenta como argumento
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")
    def arrancar(self):
        if self.gasolina > 0:
            print("Arrancar")
        else:
            print("No arrancar")
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve") 
mi_coche = Coche(5)

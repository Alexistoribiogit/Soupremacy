class Tracteur:
    def __init__(self):
        self.disponible = True

    def utiliser(self):
        self.disponible = False

    def liberer(self):
        self.disponible = True

    def est_disponible(self):
        return self.disponible

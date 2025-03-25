class Champ:
    def __init__(self):
        self.legume = None
        self.nb_arrosages_restants = 10

    def semable(self):
        return self.legume is None

    def semer(self, legume):
        self.legume = legume

    def arrosable(self):
        return self.legume is not None and self.nb_arrosages_restants != 0

    def arroser(self):
        self.nb_arrosages_restants -= 1

    def recoltable(self):
        return self.legume is not None and self.nb_arrosages_restants == 0

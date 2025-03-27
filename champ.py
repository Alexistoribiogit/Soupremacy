from legume import Legume

ARROSAGE_NECESSAIRES = {
    Legume.COURGETTE: 10,
    Legume.TOMATE: 15,
}


class Champ:
    def __init__(self):
        self.legume = None
        self.nb_arrosages_restants = 0

    def semable(self):
        return self.legume is None

    def semer(self, legume):
        self.legume = legume
        self.nb_arrosages_restants = ARROSAGE_NECESSAIRES[legume]

    def arrosable(self):
        return self.legume is not None and self.nb_arrosages_restants > 0

    def arroser(self):
        if self.arrosable():
            self.nb_arrosages_restants -= 1

    def recoltable(self):
        return self.legume is not None and self.nb_arrosages_restants == 0

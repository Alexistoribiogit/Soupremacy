class Champ:
    def __init__(self):
        self.legume = None
        self.arrose = False

    def semable(self):
        return self.legume is None

    def semer(self, legume):
        self.legume = legume

    def arrosable(self):
        return self.legume is not None and not self.arrose

    def arroser(self):
        self.arrose = True

class Champ:
    def __init__(self):
        self.legume = None

    def semable(self):
        return self.legume is None

    def semer(self, legume):
        self.legume = legume

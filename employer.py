class Employer:
    def __init__(self):
        self.occupe = False
        self.employe = None

    def embauche(self):
        self.occupe = True

    def licencie(self):
        self.occupe = False
        self.employe = None

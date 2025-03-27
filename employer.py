class Employer:
    def __init__(self):
        self.employes = []  # Liste pour stocker les employés

    def embauche(self, employe):
        if not self.est_occupe():  # Vérifie si l'employeur n'a pas déjà d'employés
            self.employes.append(employe)
        else:
            raise Exception(
                "L'employeur doit licencier l'employé actuel avant d'en embaucher un nouveau."
            )

    def licencie(self):
        if self.est_occupe():
            self.employes.pop()  # Licencie le dernier employé
        else:
            raise Exception("Aucun employé à licencier.")

    def est_occupe(self):
        return len(self.employes) > 0

from employer import Employer
import pytest


class TestEmployer:
    def test_embauche(self):
        employer = Employer()

        # Embaucher un employé
        employer.embauche("Employé 1")

        # Vérifier que l'employeur a un employé
        assert len(employer.employes) == 1
        assert employer.est_occupe()  # Vérifier que l'employeur est occupé

        # Essayer d'embaucher un deuxième employé sans licencier
        with pytest.raises(Exception) as excinfo:
            employer.embauche("Employé 2")
        assert (
            str(excinfo.value)
            == "L'employeur doit licencier l'employé actuel avant d'en embaucher un nouveau."
        )

    def test_licenciement(self):
        employer = Employer()

        # Embaucher un employé d'abord pour pouvoir le licencier
        employer.embauche("Employé 1")

        # Licencier l'employé
        employer.licencie()

        # Vérifier que l'employeur n'a plus d'employés
        assert len(employer.employes) == 0
        assert not employer.est_occupe()  # Vérifier que l'employeur n'est pas occupé

        # Essayer de licencier sans employé
        with pytest.raises(Exception) as excinfo:
            employer.licencie()
        assert str(excinfo.value) == "Aucun employé à licencier."

        # Embaucher un nouvel employé après licenciement
        employer.embauche("Employé 2")

        # Vérifier que l'employeur a un nouvel employé
        assert len(employer.employes) == 1
        assert employer.est_occupe()  # Vérifier que l'employeur est occupé

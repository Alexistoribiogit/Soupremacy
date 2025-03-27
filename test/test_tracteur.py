from tracteur import Tracteur


def test_tracteur_initialement_disponible():
    tracteur = Tracteur()
    assert tracteur.disponible == True


def test_tracteur_utilise():
    tracteur = Tracteur()
    tracteur.utiliser()
    assert tracteur.disponible == False


def test_tracteur_liberer():
    tracteur = Tracteur()
    tracteur.utiliser()
    tracteur.liberer()
    assert tracteur.disponible == True

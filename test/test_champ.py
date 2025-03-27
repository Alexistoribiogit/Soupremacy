from champ import Champ
from legume import Legume


def test_champ_semable():
    champ = Champ()
    assert champ.semable() == True


def test_champ_non_semable():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    assert champ.semable() == False


def test_champ_vide_non_arrosable():
    champ = Champ()
    assert champ.arrosable() == False


def test_champ_juste_semer_non_arrosable():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    assert champ.arrosable() == True


def test_champ_arroser():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    for _ in range(10):
        champ.arroser()
    assert champ.arrosable() == False


def test_champ_arroser_mais_pas_assez():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    for _ in range(9):
        champ.arroser()
    assert champ.arrosable() == True


def test_champ_vide_non_recoltable():
    champ = Champ()
    assert champ.recoltable() == False


def test_champ_juste_semer_non_recoltable():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    assert champ.recoltable() == False


def test_champ_pas_assez_arrose_non_recoltable():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    for _ in range(9):
        champ.arroser()
    assert champ.recoltable() == False


def test_champ_recoltable():
    champ = Champ()
    champ.semer(Legume.COURGETTE)
    for _ in range(10):
        champ.arroser()
    assert champ.recoltable() == True


def test_champ_stockable():
    pass


def test_champ_tomate_semable():
    champ = Champ()
    assert champ.semable() == True
    champ.semer(Legume.TOMATE)
    assert champ.semable() == False


def test_champ_tomate_arrosable():
    champ = Champ()
    champ.semer(Legume.TOMATE)
    assert champ.arrosable() == True
    for _ in range(15):
        champ.arroser()
    assert champ.arrosable() == False


def test_champ_tomate_recoltable():
    champ = Champ()
    champ.semer(Legume.TOMATE)
    for _ in range(14):
        champ.arroser()
    assert champ.recoltable() == False
    champ.arroser()
    assert champ.recoltable() == True

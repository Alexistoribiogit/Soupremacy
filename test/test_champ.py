from champ import Champ
from legume import Legume


def test_champ_semable():
    champ = Champ()
    assert champ.semable() == True


def test_champ_non_semable():
    champ = Champ()
    champ.semer(Legume.PATATE)
    assert champ.semable() == False

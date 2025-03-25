from employer import Employer


def test_employer_initialement_libre():
    employer = Employer()
    assert employer.occupe == False


def test_employer_embauche():
    employer = Employer()
    employer.embauche()
    assert employer.occupe == True


def test_employer_licencie():
    employer = Employer()
    employer.embauche()
    employer.licencie()
    assert employer.occupe == False

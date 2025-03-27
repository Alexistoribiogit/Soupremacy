from champ import Champ
from legume import Legume

gerant_disponible = True


def decide_commands(game_state: dict) -> list[str]:
    global gerant_disponible
    commands = []
    day = game_state.get("day", 0)

    # Jour 0 : achat premier champ + un ouvrier
    if day == 0:
        commands.append("0 ACHETER_CHAMP")
        commands.append("0 EMPLOYER")
        commands.append("0 ACHETER_TRACTEUR")

    farms = game_state.get("farms", [])
    my_farm = next((f for f in farms if f["name"] == "Soupremacy"), None)
    if not my_farm:
        return commands

    # Gestion du premier champ (COURGETTE)
    print(my_farm)
    premier_champ = my_farm["fields"][0]
    print(premier_champ)
    champ1 = Champ()
    if premier_champ["content"] == "NONE":
        champ1.legume = None
    else:
        champ1.legume = Legume.COURGETTE
    champ1.nb_arrosages_restants = premier_champ["needed_water"]

    if champ1.semable():
        commands.append("1 SEMER COURGETTE 1")
        gerant_disponible = True
    elif champ1.arrosable():
        commands.append("1 ARROSER 1")
    elif champ1.recoltable() and gerant_disponible:
        commands.append("0 VENDRE 1")
        gerant_disponible = False

    # Acheter un deuxième champ si disponible et argent suffisant
    if len(my_farm["fields"]) == 1 and my_farm["money"] >= 10000:
        commands.append("0 ACHETER_CHAMP")

    # Embaucher un 2e ouvrier s'il n'y en a qu'un et 2 champs
    if len(my_farm["fields"]) >= 2 and len(my_farm.get("employees", [])) < 2:
        commands.append("0 EMPLOYER")

    # Gestion du deuxième champ (TOMATE)
    if (
        len(my_farm["fields"]) > 1
        and my_farm["fields"][1].get("bought", True)
        and my_farm["fields"][1].get("content") is not None
    ):
        deuxième_champ = my_farm["fields"][1]
        print(deuxième_champ)

        champ2 = Champ()
        if deuxième_champ["content"] == "NONE":
            champ2.legume = None
        else:
            champ2.legume = Legume.TOMATE
        champ2.nb_arrosages_restants = deuxième_champ["needed_water"]

        if champ2.semable():
            commands.append("2 SEMER TOMATE 2")
        elif champ2.arrosable():
            commands.append("2 ARROSER 2")
        elif champ2.recoltable():
            if my_farm.get("tractors", 0) > 0:
                commands.append("2 STOCKER 2 1")
            elif gerant_disponible:
                commands.append("0 VENDRE 2")
                gerant_disponible = False

    return commands

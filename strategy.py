from champ import Champ
from legume import Legume


def decide_commands(game_state: dict) -> list[str]:
    commands = []
    day = game_state.get("day", 0)
    if day == 0:
        commands.append("0 ACHETER_CHAMP")
        commands.append("0 EMPLOYER")

    farms = game_state.get("farms", [])
    my_farm = next((f for f in farms if f["name"] == "Soupremacy"), None)
    if not my_farm:
        return commands
    premier_champ = my_farm["fields"][0]
    print(premier_champ)
    champ1 = Champ()
    if premier_champ["content"] == "NONE":
        champ1.legume = None
    else:
        champ1.legume = Legume.PATATE
    champ1.nb_arrosages_restants = premier_champ["needed_water"]
    if champ1.semable():
        commands.append("1 SEMER PATATE 1")
    elif champ1.arrosable():
        commands.append("1 ARROSER 1")
    return commands

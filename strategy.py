def decide_commands(game_state: dict) -> list[str]:
    commands = []
    day = game_state.get("day", 0)
    if day == 0:
        commands.append("0 ACHETER_CHAMP")
        commands.append("0 ACHETER_CHAMP")
        commands.append("0 ACHETER_CHAMP")
        commands.append("0 ACHETER_TRACTEUR")
        commands.append("0 EMPLOYER")
        commands.append("0 EMPLOYER")
        commands.append("1 SEMER TOMATE 1")
        commands.append("2 SEMER PATATE 2")

    farms = game_state.get("farms", [])
    my_farm = next((f for f in farms if f["name"] == "Soupremacy"), None)
    if not my_farm:
        return commands

    return commands

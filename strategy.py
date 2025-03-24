def decide_commands(game_state: dict) -> list[str]:
    commands = []
    day = game_state.get("day", 0)

    farms = game_state.get("farms", [])
    my_farm = next((f for f in farms if f["name"] == "Soupremacy"), None)
    if not my_farm:
        return commands

    employees = my_farm.get("employees", [])
    fields = my_farm.get("fields", [])

    # Répartition ouvrier → champ
    for i, field in enumerate(fields):
        if i >= len(employees):
            break  # Pas assez d’ouvriers

        worker_id = employees[i]["id"]
        field_id = field["id"]
        vegetable = field.get("vegetable")
        water = field.get("water", 0)

        if vegetable is None:
            # S'il n'y a rien de planté, on sème (on varie un peu)
            legume = ["TOMATE", "PATATE", "POIREAU", "OIGNON", "COURGETTE"][i % 5]
            commands.append(f"{worker_id} SEMER {legume} {field_id}")

        elif water < 10:
            # S’il y a une plante, on arrose si besoin
            commands.append(f"{worker_id} ARROSER {field_id}")

        elif water >= 10:
            # Si suffisamment arrosé, on vend
            commands.append(f"0 VENDRE {field_id}")

    return commands

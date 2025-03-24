from strategy import decide_commands

def test_jour_0_achat_champ():
    game_state = {"day": 0, "farms": [{"name": "Soupremacy"}]}
    commands = decide_commands(game_state)
    assert "0 ACHETER_CHAMP" in commands

def test_jour_1_employe():
    game_state = {"day": 1, "farms": [{"name": "Soupremacy"}]}
    commands = decide_commands(game_state)
    assert "0 EMPLOYER" in commands

def test_semer_patate():
    game_state = {
        "day": 2,
        "farms": [{
            "name": "Soupremacy",
            "employees": [{"id": 1}],
            "fields": [{"id": 1, "vegetable": None}]
        }]
    }
    commands = decide_commands(game_state)
    assert "1 SEMER PATATE 1" in commands

def test_arroser():
    game_state = {
        "day": 3,
        "farms": [{
            "name": "Soupremacy",
            "employees": [{"id": 1}],
            "fields": [{"id": 1, "vegetable": "PATATE", "water": 5}]
        }]
    }
    commands = decide_commands(game_state)
    assert "1 ARROSER 1" in commands

def test_vendre_si_arrosage_ok():
    game_state = {
        "day": 4,
        "farms": [{
            "name": "Soupremacy",
            "employees": [{"id": 1}],
            "fields": [{"id": 1, "vegetable": "PATATE", "water": 10}]
        }]
    }
    commands = decide_commands(game_state)
    assert "0 VENDRE 1" in commands

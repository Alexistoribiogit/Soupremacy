import pytest
from strategy import decide_commands, gerant_disponible


def test_jour_zero():
    game_state = {"day": 0}
    expected_commands = ["0 ACHETER_CHAMP", "0 EMPLOYER", "0 ACHETER_TRACTEUR"]
    assert decide_commands(game_state) == expected_commands


def test_no_farm_named_soupremacy():
    game_state = {
        "day": 1,
        "farms": [{"name": "OtherFarm", "fields": [], "money": 5000}],
    }
    expected_commands = []
    assert decide_commands(game_state) == expected_commands


def test_farm_with_empty_field():
    game_state = {
        "day": 1,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 5000,
                "fields": [{"content": "NONE", "needed_water": 0}],
            }
        ],
    }
    expected_commands = ["1 SEMER COURGETTE 1"]
    assert decide_commands(game_state) == expected_commands


def test_farm_with_field_needing_watering():
    game_state = {
        "day": 1,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 5000,
                "fields": [{"content": "COURGETTE", "needed_water": 1}],
            }
        ],
    }
    expected_commands = ["1 ARROSER 1"]
    assert decide_commands(game_state) == expected_commands


def test_farm_with_field_ready_for_harvest():
    game_state = {
        "day": 1,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 5000,
                "fields": [{"content": "COURGETTE", "needed_water": 0}],
            }
        ],
    }
    # On s'assure que le gérant est disponible pour vendre
    global gerant_disponible
    gerant_disponible = True

    expected_commands = ["0 VENDRE 1"]
    assert decide_commands(game_state) == expected_commands


def test_achat_2e_champ_si_un_seul():
    game_state = {
        "day": 2,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 10000,
                "fields": [{"id": 1, "content": "COURGETTE", "needed_water": 5}],
            }
        ],
    }
    commands = decide_commands(game_state)
    assert "0 ACHETER_CHAMP" in commands


def test_semer_tomate_sur_champ2():
    game_state = {
        "day": 2,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 5000,
                "fields": [
                    {"id": 1, "content": "COURGETTE", "needed_water": 5},
                    {"id": 2, "content": "NONE", "needed_water": 10},
                ],
            }
        ],
    }
    commands = decide_commands(game_state)
    assert "1 SEMER TOMATE 2" in commands


def test_arroser_champ2():
    game_state = {
        "day": 3,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 5000,
                "fields": [
                    {"id": 1, "content": "COURGETTE", "needed_water": 0},
                    {"id": 2, "content": "TOMATE", "needed_water": 5},
                ],
            }
        ],
    }
    commands = decide_commands(game_state)
    assert "1 ARROSER 2" in commands


def test_stocker_champ2():
    game_state = {
        "day": 4,
        "farms": [
            {
                "name": "Soupremacy",
                "money": 5000,
                "tractors": 1,
                "fields": [
                    {"id": 1, "content": "COURGETTE", "needed_water": 5},
                    {"id": 2, "content": "TOMATE", "needed_water": 0},
                ],
            }
        ],
    }
    # Gérant doit être disponible pour vendre
    global gerant_disponible
    gerant_disponible = True

    commands = decide_commands(game_state)
    assert "1 STOCKER 2 1" in commands

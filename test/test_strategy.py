import pytest
from strategy import decide_commands

def test_day_zero():
    game_state = {"day": 0}
    expected_commands = ["0 ACHETER_CHAMP", "0 EMPLOYER"]
    assert decide_commands(game_state) == expected_commands

def test_no_farm_named_soupremacy():
    game_state = {"day": 1, "farms": [{"name": "OtherFarm", "fields": []}]}
    expected_commands = []
    assert decide_commands(game_state) == expected_commands

def test_farm_with_empty_field():
    game_state = {"day": 1, "farms": [{"name": "Soupremacy", "fields": [{"content": "NONE", "needed_water": 0}]}]}
    expected_commands = ["1 SEMER PATATE 1"]
    assert decide_commands(game_state) == expected_commands

def test_farm_with_field_needing_watering():
    game_state = {"day": 1, "farms": [{"name": "Soupremacy", "fields": [{"content": "PATATE", "needed_water": 1}]}]}
    expected_commands = ["1 ARROSER 1"]
    assert decide_commands(game_state) == expected_commands

def test_farm_with_field_ready_for_harvest():
    game_state = {"day": 1, "farms": [{"name": "Soupremacy", "fields": [{"content": "PATATE", "needed_water": 0}]}]}
    expected_commands = ["0 VENDRE 1"]
    assert decide_commands(game_state) == expected_commands

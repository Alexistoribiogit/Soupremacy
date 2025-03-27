import pytest
from unittest.mock import patch, MagicMock
from sample_player_client import PlayerGameClient


@patch("sample_player_client.Client.__init__", return_value=None)
def test_add_command(mock_client_init):
    client = PlayerGameClient("localhost", 12345, "tester")
    client._commands = []
    client.add_command("0 EMPLOYER")
    assert client._commands == ["0 EMPLOYER"]


@patch("sample_player_client.Client.__init__", return_value=None)
@patch("sample_player_client.PlayerGameClient.send_json")
def test_send_commands(mock_send_json, mock_client_init):
    client = PlayerGameClient("localhost", 12345, "tester")
    client._commands = ["0 ACHETER_CHAMP", "0 EMPLOYER"]

    expected_data = {"commands": ["0 ACHETER_CHAMP", "0 EMPLOYER"]}
    copied = expected_data.copy()

    client.send_commands()

    mock_send_json.assert_called_once_with(copied)
    assert client._commands == []


@patch("sample_player_client.Client.__init__", return_value=None)
@patch("sample_player_client.PlayerGameClient.read_json")
@patch("sample_player_client.PlayerGameClient.send_json")
def test_run_one_iteration(mock_send_json, mock_read_json, mock_client_init):
    mock_read_json.return_value = {
        "day": 0,
        "farms": []
    }

    client = PlayerGameClient("localhost", 12345, "tester")
    with patch("sample_player_client.decide_commands", return_value=["0 EMPLOYER"]), \
         patch("builtins.print"), \
         patch.object(client, "send_commands") as mock_send_commands:

        game_data = client.read_json()
        commands = ["0 EMPLOYER"]
        for command in commands:
            client.add_command(command)
        client.send_commands()

        mock_send_commands.assert_called_once()

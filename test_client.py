import sys
import os

# Ajouter le dossier courant au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from sample_player_client import PlayerGameClient  # Import après modification du chemin

import pytest
from chronobio.network.client import Client
from sample_player_client import PlayerGameClient


class MockServer:
    """Simule un serveur de jeu pour tester notre client."""
    
    def __init__(self):
        self.last_received = None

    def read_json(self):
        """Simule la réception de données du serveur."""
        return {
            "day": 0,
            "farms": [{"name": "Soupremacy"}]  # Notre ferme
        }

    def send_json(self, data):
        """Capture les données envoyées par le client."""
        self.last_received = data


@pytest.fixture
def mock_client():
    """Crée une instance du client avec un serveur simulé."""
    server = MockServer()
    client = PlayerGameClient("localhost", 12345, "Soupremacy")
    client.read_json = server.read_json  # Remplace la lecture réseau
    client.send_json = server.send_json  # Capture les envois
    return client, server


def test_achat_champ(mock_client):
    """Vérifie que le client envoie bien la commande d'achat."""
    client, server = mock_client
    client.run()

    assert server.last_received is not None, "Aucune commande envoyée"
    assert "0 ACHETER_CHAMP" in server.last_received["commands"], "Commande incorrecte"

def test_semer_legume(mock_client):
    """Teste une commande de semis."""
    client, server = mock_client

    # Simule une journée 2, où on suppose qu'on a un ouvrier et un champ
    server.read_json = lambda: {
        "day": 2,
        "farms": [{
            "name": "Soupremacy",
            "fields": [{"id": 1, "vegetable": None, "water": 0}],
            "employees": [{"id": 1}],
            "money": 90000
        }]
    }

    client.run()

    assert server.last_received is not None
    assert any("SEMER" in cmd for cmd in server.last_received["commands"]), "Aucune commande de semis envoyée"

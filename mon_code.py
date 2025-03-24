# chronobio_client.py
import socket

class Farm:
    def __init__(self, initial_balance: int = 100000):
        self.balance = initial_balance
        self.fields = []  # Liste des champs achetés

    def buy_field(self) -> bool:
        """Achete un nouveau champ si le solde est suffisant.

        Returns:
            bool: True si l'achat a réussi, False sinon.
        """
        if self.balance >= 10000:
            self.balance -= 10000
            self.fields.append(len(self.fields) + 1)  # Ajoute un champ (numéroté à partir de 1)
            return True
        return False

def send_command(server_addr: str, port: int, command: str):
    """Envoie une commande au serveur."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_addr, port))
            sock.sendall(command.encode())
            response = sock.recv(1024).decode()
            print("Réponse du serveur:", response)
    except ConnectionRefusedError:
        print("Erreur de connexion : le serveur a refusé la connexion.")

def main():
    farm = Farm()
    server_addr = "127.0.0.1"  # Adresse IP du serveur
    port = 12345  # Port du serveur

    # Exemple : Acheter un champ au premier jour
    game_data = {"day": 0}  # Simule les données du jeu
    if game_data["day"] == 0:
        if farm.buy_field():
            send_command(server_addr, port, "0 ACHETER_CHAMP")
        else:
            print("Solde insuffisant pour acheter un champ.")

def test_buy_field():
    """Teste la fonctionnalité d'achat de champ."""
    # Test d'achat réussi
    farm = Farm(initial_balance=20000)
    assert farm.buy_field() is True
    assert len(farm.fields) == 1
    assert farm.balance == 10000

    # Test d'échec d'achat (solde insuffisant)
    farm = Farm(initial_balance=5000)
    assert farm.buy_field() is False
    assert len(farm.fields) == 0
    assert farm.balance == 5000

    print("Tous les tests ont réussi !")

if __name__ == "__main__":
    # Exécuter les tests
    test_buy_field()

    # Lancer le client
    main()
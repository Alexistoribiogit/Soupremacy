import argparse
from chronobio.network.client import Client

class PlayerGameClient(Client):
    def __init__(self, server_addr: str, port: int, username: str) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

    def run(self) -> None:
        while True:
            game_data = self.read_json()

            # Trouver notre ferme
            my_farm = next(farm for farm in game_data["farms"] if farm["name"] == self.username)
            print(my_farm)  # Debug : afficher les infos de la ferme

            # Jour 0 : Initialisation de la stratégie
            if game_data["day"] == 0:
=======
                self.add_command("0 EMPRUNTER 100000")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("1 SEMER TOMATE 4")
                self.add_command("2 SEMER PATATE 3")
                self.add_command("3 SEMER POIREAU 2")
                self.add_command("4 SEMER OIGNON 1")

>>>>>>> 80f6b99b573314df3dcd8f052535d1b6cc313e1c
            self.send_commands()

    def add_command(self, command: str) -> None:
        self._commands.append(command)

    def send_commands(self) -> None:
        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument("-a", "--address", type=str, default="localhost", help="Server address")
    parser.add_argument("-p", "--port", type=int, default=12345, help="Server port")
    parser.add_argument("-u", "--username", type=str, default="Soupremacy", help="Username")

    args = parser.parse_args()
    client = PlayerGameClient(args.address, args.port, args.username)
    client.run()

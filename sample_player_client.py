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
                self.add_command("0 ACHETER_CHAMP")  # Acheter un champ
                self.add_command("0 EMPLOYER")  # Embaucher un ouvrier
                self.add_command("1 SEMER TOMATE 1")  # Semer des tomates sur le champ
            
            # Arroser le champ jusqu'à la récolte
            if "champs" in my_farm:
                for champ in my_farm["champs"]:
                    if champ["arrosages"] < 10:
                        self.add_command(f"1 ARROSER {champ['id']}")
                    elif champ["arrosages"] == 10 and not champ["recoltable"]:
                        print(f"Champ {champ['id']} prêt à être récolté.")
                    elif champ["recoltable"]:
                        self.add_command("0 VENDRE {champ['id']}")
                        
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

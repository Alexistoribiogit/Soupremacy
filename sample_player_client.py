import argparse
from chronobio.network.client import Client

from strategy import decide_commands


class PlayerGameClient(Client):
    def __init__(self, server_addr: str, port: int, username: str) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

    def run(self) -> None:
        while True:
            game_data = self.read_json()
            commands = decide_commands(game_data)
            for command in commands:
                self.add_command(command)

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
    parser.add_argument(
        "-a", "--address", type=str, default="localhost", help="Server address"
    )
    parser.add_argument("-p", "--port", type=int, default=12345, help="Server port")
    parser.add_argument(
        "-u", "--username", type=str, default="Soupremacy", help="Username"
    )

    args = parser.parse_args()
    client = PlayerGameClient(args.address, args.port, args.username)
    client.run()

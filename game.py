from dataclasses import dataclass
from dataclasses import replace


@dataclass
class GameState:
    player_count: ...
    active_player: ...

    @classmethod
    def init(cls):
        return cls(player_count=2, active_player=0)

    def next_player(self):
        next_player = self.active_player + 1
        if next_player == self.player_count:
            next_player = 0
        return replace(self, active_player=next_player)


def loop(game_state):
    while True:
        print("To exit, type “done”.")
        inp = input(": ")
        if inp == "done":
            break

        game_state = game_state.next_player()


def main():
    game_state = GameState.init()
    loop(game_state)


if __name__ == "__main__":
    main()

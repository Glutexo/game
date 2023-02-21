from dataclasses import dataclass
from dataclasses import replace
from enum import auto
from enum import Enum


class Commands(Enum):
    DONE = auto()


@dataclass
class State:
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

    @property
    def description(self):
        return f"The active player is {self.active_player}\n"


def prompt():
    print("To exit, type “done”.")
    inp = input(": ")
    if inp == "done":
        return Commands.DONE


def loop(state):
    while True:
        print(state.description)

        command = prompt()
        if command is Commands.DONE:
            break

        state = state.next_player()


def main():
    state = State.init()
    loop(state)


if __name__ == "__main__":
    main()

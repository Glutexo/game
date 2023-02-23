from enum import auto
from enum import Enum

from game import State


class Commands(Enum):
    DONE = auto()


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

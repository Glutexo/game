from enum import auto
from enum import Enum

from game import State


class Commands(Enum):
    EXIT = auto()


def describe(state):
    return f"The active player is {state.active_player}\n"


def prompt():
    print("To exit, type “exit”.")
    inp = input(": ")
    if inp == "exit":
        return Commands.EXIT


def loop(state):
    while True:
        description = describe(state)
        print(description)

        command = prompt()
        if command is Commands.EXIT:
            return state

        state = state.next_player()


def main():
    state = State.init()
    loop(state)


if __name__ == "__main__":
    main()

from enum import auto
from enum import Enum

from game import State


class Commands(Enum):
    DONE = auto()


def describe(state):
    return f"The active player is {state.active_player}\n"


def prompt():
    print("To exit, type “done”.")
    inp = input(": ")
    if inp == "done":
        return Commands.DONE


def loop(state):
    while True:
        description = describe(state)
        print(description)

        command = prompt()
        if command is Commands.DONE:
            break

        state = state.next_player()


def main():
    state = State.init()
    loop(state)


if __name__ == "__main__":
    main()

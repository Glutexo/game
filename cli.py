from game import Commands
from game import loop
from game import State


def describe(state):
    return f"The active player is {state.active_player}\n"


def prompt():
    print("To exit, type “exit”.")
    inp = input(": ")
    if inp == "exit":
        return Commands.EXIT


def callback(state):
    description = describe(state)
    print(description)

    command = prompt()
    return command


def main():
    state = State.init()
    loop(state, callback)


if __name__ == "__main__":
    main()

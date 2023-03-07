from .game import Commands
from .game import loop
from .game import State


def describe_history(index, state):
    description = describe_state(state)
    return f"{index} {description}"


def describe_state(state):
    return f"The active player is {state.active_player}"


def prompt():
    print("To exit, type “exit”.")
    inp = input(": ")
    if inp == "exit":
        return Commands.EXIT


def callback(state):
    for index, state in enumerate(state.history):
        description = describe_history(index, state)
        print(description)

    command = prompt()
    return command


def main():
    state = State()
    loop(state, callback)


if __name__ == "__main__":
    main()

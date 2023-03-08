from .describe import describe_history
from ..game import Commands
from ..game import loop
from ..game import State


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

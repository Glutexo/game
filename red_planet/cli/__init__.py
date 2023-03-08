from .describe import describe_history
from .. import Commands
from .. import loop
from .. import State


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

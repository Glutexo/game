from .describe import describe_state
from .. import Commands
from .. import loop
from .. import State


def prompt():
    print("To exit, type “exit”.")
    inp = input(": ")
    if inp == "exit":
        return Commands.EXIT


def callback(state):
    description = describe_state(state)
    print(description)

    command = prompt()
    return command


def main():
    state = State()
    loop(state, callback)

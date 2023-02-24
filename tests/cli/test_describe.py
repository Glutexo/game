from cli import describe
from game import State
from dataclasses import replace


def test_active_player_0():
    state = State.init()
    state = replace(state, active_player=0)
    assert describe(state) == "The active player is 0\n"


def test_active_player_1():
    state = State.init()
    state = replace(state, active_player=1)
    assert describe(state) == "The active player is 1\n"

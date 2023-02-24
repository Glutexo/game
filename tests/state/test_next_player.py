from dataclasses import replace

from game import State

def test_0_to_1():
    state = State.init()
    state = replace(state, active_player=0)
    state = state.next_player()
    assert state.active_player == 1


def test_1_to_0():
    state = State.init()
    state = replace(state, active_player=1)
    state = state.next_player()
    assert state.active_player == 0

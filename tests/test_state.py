from game import State
from dataclasses import replace


def test_init_player_count():
    state = State.init()
    assert state.player_count == 2


def test_init_active_player():
    state = State.init()
    assert state.active_player == 0


def test_next_player_0_to_1():
    state = State.init()
    state = replace(state, active_player=0)
    state = state.next_player()
    assert state.active_player == 1


def test_next_player_1_to_0():
    state = State.init()
    state = replace(state, active_player=1)
    state = state.next_player()
    assert state.active_player == 0


def test_description_active_player_0():
    state = State.init()
    state = replace(state, active_player=0)
    assert state.description == "The active player is 0\n"


def test_description_active_player_1():
    state = State.init()
    state = replace(state, active_player=1)
    assert state.description == "The active player is 1\n"

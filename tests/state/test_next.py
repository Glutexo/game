from unittest.mock import patch

from pytest import raises

from red_planet.game import State


def test_fields():
    state = State(player_count=2, active_player=0)
    state = state._next(player_count=3, active_player=1)
    assert state.player_count == 3
    assert state.active_player == 1


def test_no_fields():
    state = State(player_count=2, active_player=0)
    state = state._next()
    assert state.player_count == 2
    assert state.active_player == 0


def test_fields_previous():
    state = State()
    with raises(TypeError):
        state._next(previous=[])


def test_previous_value():
    old_state = State()

    with patch.object(State, "history") as history:
        new_state = old_state._next()

    assert new_state.previous == history

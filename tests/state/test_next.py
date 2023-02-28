from unittest.mock import Mock

from pytest import raises

from game import State


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


def test_fields_history():
    state = State()
    with raises(TypeError):
        state._next(history=[])


def test_history_empty():
    old_state = State()
    new_state = old_state._next()
    assert new_state.history == [old_state]


def test_history_nonempty():
    history_state = Mock()
    old_state = State(history=[history_state])
    new_state = old_state._next(active_player=1)
    assert new_state.history == [history_state, old_state]


def test_history_sequence():
    first_state = State()
    second_state = first_state._next()
    third_state = second_state._next()
    assert third_state.history == [first_state, second_state]


def test_history_same_object():
    old_state = State()
    new_state = old_state._next()
    assert new_state.history[0] is old_state


def test_history_different_object():
    old_state = State()
    new_state = old_state._next()
    assert new_state.history[0] is not new_state


def test_history_default_same_object():
    old_state = State()
    new_state = State()
    assert old_state.history is new_state.history


def test_history_next_different_object():
    old_state = State()
    new_state = old_state._next()
    assert old_state.history is not new_state.history


def test_history_next_default_not_modified():
    first_state = State()
    first_state._next()

    second_state = State()
    assert second_state.history == []

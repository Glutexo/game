from unittest.mock import Mock

from game import State


def test_empty():
    state = State(previous=[])
    assert state.history == [state]


def test_one():
    first_state = State(previous=[])
    second_state = State(previous=[first_state])
    assert second_state.history == [first_state, second_state]


def test_more():
    first_state = State(previous=[])
    second_state = State(previous=[first_state])
    third_state = State(previous=[first_state, second_state])
    assert third_state.history == [first_state, second_state, third_state]


def test_mock():
    mock = Mock()
    state = State(previous=[mock])
    assert state.history == [mock, state]


def test_previous_same_object():
    state = State()
    assert state.history[0] is state


def test_previous_different_object():
    state = State()
    assert state.history is not state.previous


def test_previous_existing_not_modified():
    state = State()
    State(previous=state.history)
    assert state.previous == []


def test_previous_default_not_modified():
    first_state = State()
    State(previous=first_state.history)

    second_state = State()
    assert second_state.previous == []


def test_previous_default_not_replaced():
    first_state = State()
    State(previous=first_state.history)

    second_state = State()
    assert second_state.previous is first_state.previous

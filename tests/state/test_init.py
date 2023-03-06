from game import State


def test_default_player_count():
    state = State()
    assert state.player_count == 2


def test_default_active_player():
    state = State()
    assert state.active_player == 0


def test_previous_default_same_object():
    first_state = State()
    second_state = State()
    assert first_state.previous is second_state.previous

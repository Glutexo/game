from rain import State


def test_default_player_count():
    state = State()
    assert state.player_count == 2


def test_default_active_player():
    state = State()
    assert state.active_player == 0

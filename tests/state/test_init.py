from game import State

def test_init_player_count():
    state = State.init()
    assert state.player_count == 2


def test_init_active_player():
    state = State.init()
    assert state.active_player == 0

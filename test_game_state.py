from game import GameState
from dataclasses import replace


def test_init_player_count():
    game_state = GameState.init()
    assert game_state.player_count == 2


def test_init_active_player():
    game_state = GameState.init()
    assert game_state.active_player == 0


def test_next_player_0_to_1():
    game_state = GameState.init()
    game_state = replace(game_state, active_player=0)
    game_state = game_state.next_player()
    assert game_state.active_player == 1


def test_next_player_1_to_0():
    game_state = GameState.init()
    game_state = replace(game_state, active_player=1)
    game_state = game_state.next_player()
    assert game_state.active_player == 0

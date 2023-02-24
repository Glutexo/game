from pytest import mark

from cli import describe
from game import State


@mark.parametrize(("active_player",), [(0,), (1,)])
def test_active_player(active_player):
    state = State(player_count=2, active_player=active_player)
    assert describe(state) == f"The active player is {active_player}\n"

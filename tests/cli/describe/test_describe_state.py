from unittest.mock import Mock

from pytest import mark

from red_planet.cli.describe import describe_state
from red_planet import State


@mark.parametrize(("active_player",), [(0,), (1,)])
def test_active_player(active_player):
    state = Mock(active_player=active_player)
    assert describe_state(state) == f"The active player is {active_player}"


def test_actual():
    state = State(active_player=0)
    assert describe_state(state) == "The active player is 0"

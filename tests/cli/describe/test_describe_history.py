from unittest.mock import Mock
from unittest.mock import patch

from rain.cli.describe import describe_history
from rain import State


@patch("rain.cli.describe.describe_state")
def test_describe_state(describe_state):
    state = Mock()
    describe_history(0, state)
    describe_state.assert_called_once_with(state)


@patch("rain.cli.describe.describe_state", return_value="description")
def test_return(_describe_state):
    result = describe_history(0, Mock())
    assert result == "0 description"


def test_actual():
    state = State(active_player=0)
    result = describe_history(0, state)
    assert result == "0 The active player is 0"

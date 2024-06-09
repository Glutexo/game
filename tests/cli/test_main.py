from unittest.mock import patch

from rain.cli import callback
from rain.cli import main
from rain import State


@patch("rain.cli.loop")
def test_loop_actual(loop):
    main()

    initial_state = State()
    loop.assert_called_once_with(initial_state, callback)


@patch("rain.cli.loop")
@patch("rain.cli.State")
def test_loop_mock(state, loop):
    main()

    initial_state = state.return_value
    loop.assert_called_once_with(initial_state, callback)

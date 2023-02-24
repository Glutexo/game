from unittest.mock import patch

from cli import callback
from cli import main
from game import State


@patch("cli.loop")
def test_loop_actual(loop):
    main()

    initial_state = State()
    loop.assert_called_once_with(initial_state, callback)


@patch("cli.loop")
@patch("cli.State")
def test_loop_mock(state, loop):
    main()

    initial_state = state.return_value
    loop.assert_called_once_with(initial_state, callback)

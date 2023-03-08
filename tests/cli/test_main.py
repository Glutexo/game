from unittest.mock import patch

from red_planet.cli import callback
from red_planet.cli import main
from red_planet import State


@patch("red_planet.cli.loop")
def test_loop_actual(loop):
    main()

    initial_state = State()
    loop.assert_called_once_with(initial_state, callback)


@patch("red_planet.cli.loop")
@patch("red_planet.cli.State")
def test_loop_mock(state, loop):
    main()

    initial_state = state.return_value
    loop.assert_called_once_with(initial_state, callback)

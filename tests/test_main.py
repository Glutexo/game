from unittest.mock import patch

from game import main
from game import State


@patch("game.loop")
def test_loop_actual(loop):
    main()

    initial_state = State.init()
    loop.assert_called_once_with(initial_state)


@patch("game.loop")
@patch("game.State")
def test_loop_mock(state, loop):
    main()

    initial_state = state.init()
    loop.assert_called_once_with(initial_state)

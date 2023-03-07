from unittest.mock import call
from unittest.mock import Mock

from red_planet.game import Commands
from red_planet.game import loop


def test_callback_one():
    state = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    loop(state, callback)

    # callback.assert_called_once_with(state)
    assert callback.mock_calls == [call(state)]


def test_callback_many():
    initial_state = Mock()
    callback = Mock(side_effect=[None, Commands.EXIT])

    loop(initial_state, callback)

    final_state = initial_state.next_player.return_value
    assert callback.mock_calls == [call(initial_state), call(final_state)]


def test_return_immediate():
    initial_state = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    final_state = loop(initial_state, callback)
    assert final_state == initial_state


def test_return_late():
    initial_state = Mock()
    callback = Mock(side_effect=[None, Commands.EXIT])

    final_state = loop(initial_state, callback)
    assert final_state == initial_state.next_player.return_value


def test_next_player_none():
    state = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    loop(state, callback)
    state.next_player.assert_not_called()


def test_next_player_one():
    state = Mock()
    callback = Mock(side_effect=[None, Commands.EXIT])

    loop(state, callback)
    state.next_player.assert_called_once_with()


def test_next_player_many():
    initial_state = Mock()
    callback = Mock(side_effect=[None, None, Commands.EXIT])

    loop(initial_state, callback)

    initial_state.next_player.assert_called_once_with()

    next_state = initial_state.next_player.return_value
    next_state.next_player.assert_called_once_with()

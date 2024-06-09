from unittest.mock import call
from unittest.mock import Mock

from rain import Commands
from rain import loop


def test_callback_one():
    history = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    loop(history, callback)

    initial_state = history.last
    # callback.assert_called_once_with(initial_state)
    assert callback.mock_calls == [call(initial_state)]


def test_callback_many():
    history = Mock()
    callback = Mock(side_effect=[None, Commands.EXIT])

    loop(history, callback)

    initial_state = history.last
    final_state = history.append.return_value.last
    assert callback.mock_calls == [call(initial_state), call(final_state)]


def test_return_immediate():
    initial_history = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    final_history = loop(initial_history, callback)
    assert final_history == initial_history


def test_return_late():
    initial_history = Mock()
    callback = Mock(side_effect=[None, Commands.EXIT])

    final_history = loop(initial_history, callback)
    assert final_history == initial_history.append.return_value


def test_next_player_none():
    history = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    loop(history, callback)
    history.last.next_player.assert_not_called()


def test_next_player_one():
    history = Mock()
    callback = Mock(side_effect=[None, Commands.EXIT])

    loop(history, callback)

    initial_state = history.last
    initial_state.next_player.assert_called_once_with()


def test_next_player_many():
    history = Mock()
    callback = Mock(side_effect=[None, None, Commands.EXIT])

    loop(history, callback)

    initial_state = history.last
    initial_state.next_player.assert_called_once_with()

    final_state = history.append.return_value.last
    final_state.next_player.assert_called_once_with()

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
    final_history = Mock()
    initial_history = Mock(**{"append.return_value": final_history})
    callback = Mock(side_effect=[None, Commands.EXIT])

    loop(initial_history, callback)

    initial_history.last.next_player.assert_called_once_with()
    final_history.last.next_player.assert_not_called()


def test_next_player_many():
    final_history = Mock()
    middle_history = Mock(**{"append.return_value": final_history})
    initial_history = Mock(**{"append.return_value": middle_history})
    callback = Mock(side_effect=[None, None, Commands.EXIT])

    loop(initial_history, callback)

    initial_history.last.next_player.assert_called_once_with()
    middle_history.last.next_player.assert_called_once_with()
    final_history.last.next_player.assert_not_called()


def test_append_none():
    history = Mock()
    callback = Mock(side_effect=[Commands.EXIT])

    loop(history, callback)
    assert history.append.assert_not_called()


def test_append_one():
    final_history = Mock()
    initial_history = Mock(**{"append.return_value": final_history})
    callback = Mock(side_effect=[None, Commands.EXIT])

    loop(initial_history, callback)

    initial_next = initial_history.last.next_player.return_value
    initial_history.append.assert_called_once_with(initial_next)

    final_history.append.assert_not_called()


def test_append_many():
    final_history = Mock()
    middle_history = Mock(**{"append.return_value": final_history})
    initial_history = Mock(**{"append.return_value": middle_history})

    callback = Mock(side_effect=[None, None, Commands.EXIT])

    loop(initial_history, callback)

    initial_next = initial_history.last.next_player.return_value
    initial_history.append.assert_called_once_with(initial_next)

    middle_next = middle_history.last.next_player.return_value
    middle_history.append.assert_called_once_with(middle_next)

    final_history.append.assert_not_called()

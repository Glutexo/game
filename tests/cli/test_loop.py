from unittest.mock import call
from unittest.mock import Mock
from unittest.mock import patch

from cli import Commands
from cli import loop


@patch("cli.prompt", side_effect=[Commands.EXIT])
@patch("cli.print")
@patch("cli.describe")
def test_describe_initial(describe, _print, _prompt):
    state = Mock()
    loop(state)
    assert describe.mock_calls == [call(state)]


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
@patch("cli.print")
@patch("cli.describe")
def test_describe_next(describe, _print, _prompt):
    initial_state = Mock()
    loop(initial_state)

    next_state = initial_state.next_player.return_value
    assert describe.mock_calls == [call(initial_state), call(next_state)]


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
@patch("cli.print")
@patch("cli.describe", side_effect=["first", "second"])
def test_print(describe, print_, _prompt):
    initial_state = Mock()
    loop(initial_state)
    assert print_.mock_calls == [call("first"), call("second")]


@patch("cli.prompt", side_effect=[Commands.EXIT])
def test_prompt(prompt):
    loop(Mock())
    # prompt.assert_called_once_with()
    assert prompt.mock_calls == [call()]


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
def test_prompts(prompt):
    loop(Mock())
    assert prompt.mock_calls == [call(), call()]


@patch("cli.prompt", side_effect=[Commands.EXIT])
def test_exit_immediate(_prompt):
    initial_state = Mock()
    final_state = loop(initial_state)
    assert final_state == initial_state


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
def test_exit_late(_prompt):
    initial_state = Mock()
    final_state = loop(initial_state)
    assert final_state == initial_state.next_player.return_value


@patch("cli.prompt", side_effect=[Commands.EXIT])
def test_next_player_none(_prompt):
    state = Mock()
    loop(state)
    state.next_player.assert_not_called()


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
def test_next_player_one(_prompt):
    state = Mock()
    loop(state)
    state.next_player.assert_called_once_with()


@patch("cli.prompt", side_effect=[None, None, Commands.EXIT])
def test_next_player_many(_prompt):
    initial_state = Mock()
    loop(initial_state)

    initial_state.next_player.assert_called_once_with()

    next_state = initial_state.next_player.return_value
    next_state.next_player.assert_called_once_with()


@patch("cli.prompt", side_effect=[Commands.EXIT])
@patch("cli.describe", side_effect=["only"])
def test_stdout_one(_describe, _prompt, capsys):
    state = Mock()
    loop(state)

    out, _err = capsys.readouterr()
    assert out == "only\n"


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
@patch("cli.describe", side_effect=["first", "second"])
def test_stdout_many(_describe, _prompt, capsys):
    loop(Mock())

    out, _err = capsys.readouterr()
    assert out == "first\nsecond\n"


@patch("cli.prompt", side_effect=[None, Commands.EXIT])
def test_stderr(_prompt, capsys):
    loop(Mock())

    _out, err = capsys.readouterr()
    assert err == ""

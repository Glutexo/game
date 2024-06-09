from unittest.mock import call
from unittest.mock import Mock
from unittest.mock import patch

from rain.cli import callback


@patch("rain.cli.prompt")
@patch("rain.cli.print")
@patch("rain.cli.describe_state")
def test_describe_state(describe_state, _print, _prompt):
    state = Mock()
    callback(state)

    describe_state.assert_called_once_with(state)


@patch("rain.cli.prompt")
@patch("rain.cli.print")
def test_print_state(print_, _prompt):
    initial_state = Mock()

    state = Mock()
    with patch("rain.cli.describe_state", return_value=state):
        callback(initial_state)

    print_.assert_called_once_with(state)


@patch("rain.cli.prompt")
def test_prompt(prompt):
    callback(Mock())
    prompt.assert_called_once_with()


@patch("rain.cli.prompt")
def test_return(prompt):
    command = callback(Mock())
    assert command is prompt.return_value


@patch("rain.cli.prompt")
@patch("rain.cli.describe_state", return_value="description")
def test_stdout_one(_describe, _prompt, capsys):
    callback(Mock())

    out, _err = capsys.readouterr()
    assert out == "description\n"


@patch("rain.cli.prompt")
def test_stderr(_prompt, capsys):
    callback(Mock())

    _out, err = capsys.readouterr()
    assert err == ""

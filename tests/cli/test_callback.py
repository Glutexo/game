from unittest.mock import call
from unittest.mock import Mock
from unittest.mock import patch

from cli import callback
from game import Commands


@patch("cli.prompt")
@patch("cli.print")
@patch("cli.describe")
def test_describe(describe, _print, _prompt):
    state = Mock()
    callback(state)
    describe.assert_called_once_with(state)


@patch("cli.prompt")
@patch("cli.print")
@patch("cli.describe")
def test_print(describe, print_, _prompt):
    callback(Mock())
    print_.assert_called_once_with(describe.return_value)


@patch("cli.prompt")
def test_prompt(prompt):
    callback(Mock())
    prompt.assert_called_once_with()


@patch("cli.prompt")
def test_return(prompt):
    command = callback(Mock())
    assert command is prompt.return_value


@patch("cli.prompt")
@patch("cli.describe", side_effect=["description"])
def test_stdout_one(_describe, _prompt, capsys):
    callback(Mock())

    out, _err = capsys.readouterr()
    assert out == "description\n"


@patch("cli.prompt")
def test_stderr(_prompt, capsys):
    callback(Mock())

    _out, err = capsys.readouterr()
    assert err == ""

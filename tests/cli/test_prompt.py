from unittest.mock import patch

from pytest import mark

from rain import Commands
from rain.cli import prompt


@patch("rain.cli.input")
@patch("rain.cli.print")
def test_message(print_func, _input_func):
    prompt()
    print_func.assert_called_once_with("To exit, type “exit”.")


@patch("rain.cli.input")
def test_prompt(input_func):
    prompt()
    input_func.assert_called_once_with(": ")


@patch("rain.cli.input", side_effect=["exit"])
def test_command_exit(_input):
    command = prompt()
    assert command is Commands.EXIT


@mark.parametrize(("input_param",), [("",), ("unknown",)])
def test_command_unknown(input_param):
    with patch("rain.cli.input", side_effect=[input_param]):
        command = prompt()
        assert command is None


@patch("rain.cli.input", side_effect=[""])
def test_stdout(_input_func, capsys):
    prompt()
    out, _err = capsys.readouterr()
    assert out == "To exit, type “exit”.\n"


@patch("rain.cli.input", side_effect=[""])
def test_stderr(_input_func, capsys):
    prompt()
    _out, err = capsys.readouterr()
    assert err == ""

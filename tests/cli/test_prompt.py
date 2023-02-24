from unittest.mock import patch

from pytest import mark

from cli import Commands
from cli import prompt


@patch("cli.input")
@patch("cli.print")
def test_message(print_func, _input_func):
    prompt()
    print_func.assert_called_once_with("To exit, type “done”.")


@patch("cli.input")
def test_prompt(input_func):
    prompt()
    input_func.assert_called_once_with(": ")


@patch("cli.input", side_effect=["done"])
def test_command_done(_input):
    command = prompt()
    assert command is Commands.DONE


@mark.parametrize(("input_param",), [("",), ("unknown",)])
def test_command_unknown(input_param):
    with patch("cli.input", side_effect=[input_param]):
        command = prompt()
        assert command is None


@patch("cli.input", side_effect=[""])
def test_stdout(_input_func, capsys):
    prompt()
    out, _err = capsys.readouterr()
    assert out == "To exit, type “done”.\n"


@patch("cli.input", side_effect=[""])
def test_stderr(_input_func, capsys):
    prompt()
    _out, err = capsys.readouterr()
    assert err == ""

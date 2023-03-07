from unittest.mock import call
from unittest.mock import Mock
from unittest.mock import patch

from red_planet.cli import callback


@patch("red_planet.cli.prompt")
@patch("red_planet.cli.print")
@patch("red_planet.cli.describe_history")
def test_describe_history_one(describe_history, _print, _prompt):
    history_state = Mock()
    initial_state = Mock(history=[history_state])
    callback(initial_state)

    # describe_history.assert_called_once_with(0, history_state)
    assert describe_history.mock_calls == [call(0, history_state)]


@patch("red_planet.cli.prompt")
@patch("red_planet.cli.print")
@patch("red_planet.cli.describe_history")
def test_describe_history_many(describe_history, _print, _prompt):
    first_state = Mock()
    second_state = Mock()
    initial_state = Mock(history=[first_state, second_state])

    callback(initial_state)

    assert describe_history.mock_calls == [
        call(0, first_state), call(1, second_state)
    ]


@patch("red_planet.cli.prompt")
@patch("red_planet.cli.print")
def test_print_one(print_, _prompt):
    initial_state = Mock(history=[Mock()])

    descriptions = [Mock()]
    with patch("red_planet.cli.describe_history", side_effect=descriptions):
        callback(initial_state)

    # print_.assert_called_once_with(descriptions[0])
    assert print_.mock_calls == [call(descriptions[0])]


@patch("red_planet.cli.prompt")
@patch("red_planet.cli.print")
def test_print_many(print_, _prompt):
    initial_state = Mock(history=[Mock(), Mock()])

    descriptions = [Mock(), Mock()]
    with patch("red_planet.cli.describe_history", side_effect=descriptions):
        callback(initial_state)

    assert print_.mock_calls == [call(descriptions[0]), call(descriptions[1])]


@patch("red_planet.cli.prompt")
def test_prompt(prompt):
    callback(Mock(history=[]))
    prompt.assert_called_once_with()


@patch("red_planet.cli.prompt")
def test_return(prompt):
    command = callback(Mock(history=[]))
    assert command is prompt.return_value


@patch("red_planet.cli.prompt")
@patch("red_planet.cli.describe_history", side_effect=["description"])
def test_stdout_one(_describe, _prompt, capsys):
    callback(Mock(history=[Mock()]))

    out, _err = capsys.readouterr()
    assert out == "description\n"


@patch("red_planet.cli.prompt")
@patch(
    "red_planet.cli.describe_history",
    side_effect=["first description", "second description"]
)
def test_stdout_many(_describe, _prompt, capsys):
    callback(Mock(history=[Mock(), Mock()]))

    out, _err = capsys.readouterr()
    assert out == "first description\nsecond description\n"


@patch("red_planet.cli.prompt")
def test_stderr(_prompt, capsys):
    callback(Mock(history=[]))

    _out, err = capsys.readouterr()
    assert err == ""

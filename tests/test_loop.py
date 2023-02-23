from game import Commands
from game import loop

from unittest.mock import ANY
from unittest.mock import call
from unittest.mock import Mock
from unittest.mock import patch


@patch("game.prompt", side_effect=[Commands.DONE])
@patch("game.print")
def test_description_initial(print_, _prompt):
    state = Mock()
    loop(state)
    assert print_.mock_calls == [call(state.description)]


@patch("game.prompt", side_effect=[None, Commands.DONE])
@patch("game.print")
def test_description_next(print_, _prompt):
    initial_state = Mock()
    loop(initial_state)

    next_state = initial_state.next_player.return_value
    assert print_.mock_calls == [ANY, call(next_state.description)]


@patch("game.prompt", side_effect=[None, Commands.DONE])
@patch("game.print")
def test_descriptions(print_, _prompt):
    initial_state = Mock()
    loop(initial_state)

    next_state = initial_state.next_player.return_value
    assert print_.mock_calls == [
        call(initial_state.description),
        call(next_state.description)
    ]


@patch("game.prompt", side_effect=[Commands.DONE])
def test_prompt(prompt):
    loop(Mock())
    # prompt.assert_called_once_with()
    assert prompt.mock_calls == [call()]


@patch("game.prompt", side_effect=[None, Commands.DONE])
def test_prompts(prompt):
    loop(Mock())
    assert prompt.mock_calls == [call(), call()]


@patch("game.prompt", side_effect=[Commands.DONE])
def test_done_immediate(_prompt):
    loop(Mock())
    assert True


@patch("game.prompt", side_effect=[None, Commands.DONE])
def test_done_late(_prompt):
    loop(Mock())
    assert True


@patch("game.prompt", side_effect=[Commands.DONE])
def test_next_player_none(_prompt):
    state = Mock()
    loop(state)
    state.next_player.assert_not_called()


@patch("game.prompt", side_effect=[None, Commands.DONE])
def test_next_player_one(_prompt):
    state = Mock()
    loop(state)
    state.next_player.assert_called_once_with()


@patch("game.prompt", side_effect=[None, None, Commands.DONE])
def test_next_player_many(_prompt):
    initial_state = Mock()
    loop(initial_state)

    initial_state.next_player.assert_called_once_with()

    next_state = initial_state.next_player.return_value
    next_state.next_player.assert_called_once_with()


@patch("game.prompt", side_effect=[Commands.DONE])
def test_stdout_one(_prompt, capsys):
    state = Mock(description="Initial state")
    loop(state)

    out, _err = capsys.readouterr()
    assert out == "Initial state\n"


@patch("game.prompt", side_effect=[None, Commands.DONE])
def test_stdout_many(_prompt, capsys):
    state = Mock(**{
        "description": "Initial state",
        "next_player.return_value.description": "Next state"
    })
    loop(state)

    out, _err = capsys.readouterr()
    assert out == "Initial state\nNext state\n"


@patch("game.prompt", side_effect=[None, Commands.DONE])
def test_stderr(_prompt, capsys):
    loop(Mock())

    _out, err = capsys.readouterr()
    assert err == ""

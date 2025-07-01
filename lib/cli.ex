defmodule Game.CLI do
  def main(_) do
    end_state =
      Game.begin()
      |> turn()

    message = "Player #{end_state[:active_player]} wins!"
    IO.puts(message)
  end

  def turn(state) do
    message = "Player #{state[:active_player]}’s turn.\nAction? "
    case IO.gets(message) do
      :eof ->
        IO.puts("")
        state
      _ -> turn(state)
    end
  end
end

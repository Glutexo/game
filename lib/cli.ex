defmodule Game.CLI do
  def main(_) do
    winner =
      Game.begin()
      |> turn()

    message = "Player #{winner} wins!"
    IO.puts(message)
  end

  def turn(state) do
    message = "Player #{state[:active_player]}’s turn.\nAction? "
    case IO.gets(message) do
      :eof ->
        IO.puts("")
        Game.quit(state)
      _ -> turn(state)
    end
  end
end

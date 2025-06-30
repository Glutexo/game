defmodule Game.CLI do
  def main(_) do
    turn()
    IO.puts("Player 1 wins!")
  end

  def turn() do
    case IO.gets("Player 1’s turn.\nAction? ") do
      :eof -> IO.puts("")
      _ -> turn()
    end
  end
end

defmodule GameTest do
  use ExUnit.Case
  doctest Game

  @player 0
  @state %{active_player: @player}

  describe("Game.begin/0") do
    test("begin initializes an empty state") do
      assert Game.begin() == @state
    end
  end

  describe("Game.quit/0") do
    test("quit returns the winner") do
      assert Game.quit(@state) == @player
    end
  end
end

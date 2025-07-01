defmodule GameTest do
  use ExUnit.Case
  doctest Game

  describe("Game.begin/0") do
    test("begin initializes an empty state") do
      assert Game.begin() == %{active_player: 0}
    end
  end
end

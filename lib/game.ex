defmodule Game do
  @player 0
  
  def begin() do
    %{active_player: @player}
  end

  def quit(_state) do
    @player
  end
end

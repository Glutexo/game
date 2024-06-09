from collections import namedtuple
from enum import auto
from enum import Enum


class Commands(Enum):
    EXIT = auto()


class History(namedtuple('History', ['items'], defaults=([],))):
    @classmethod
    def initial(cls, item):
        return cls(items=[item])

    @property
    def last(self):
        return self.items[-1]

    def append(self, item):
        items = self.items + [item]
        return self._replace(items=items)


class State(
    namedtuple("State", ["player_count", "active_player"], defaults=(2, 0))
):
    def next_player(self):
        next_player = self.active_player + 1
        if next_player == self.player_count:
            next_player = 0
        return self._replace(active_player=next_player)


def loop(history, callback):
    while True:
        current_state = history.last
        command = callback(current_state)
        if command is Commands.EXIT:
            return history

        new_state = current_state.next_player()
        history = history.append(new_state)

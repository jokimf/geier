from __future__ import annotations

import random
from abc import ABC


class Player(ABC):
    def __init__(self) -> None:
        self._cards = [card for card in range(1, 16)]
        self._points = 0

    def __repr__(self) -> str:
        return f'P:{self._points}'

    def action(self, active_value: int, other_players: list[Player]):
        raise NotImplementedError

    @property
    def cards(self):
        return self._cards

    @property
    def points(self):
        return self._points


class RandomPlayer(Player):
    def action(self, active_value: int, other_players: list[Player]) -> int:
        return random.choice(self._cards)

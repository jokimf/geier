from __future__ import annotations

import random
from abc import ABC


class Player(ABC):
    def __init__(self) -> None:
        self._cards: list[int] = [card for card in range(1, 16)]
        self._points: int = 0
        # TODO: Add ID

    def __repr__(self) -> str:
        return f'P:{self._points}'

    # TODO: Currently visible to other players...
    def action(self, active_value: int, other_players: list[Player]):
        raise NotImplementedError

    def _highest_card(self) -> int:
        return max(self._cards)

    def _lowest_card(self) -> int:
        return min(self._cards)

    def _highest_but_not_higher_than(self, value: int) -> int:
        """Returns -1 if no card matches the criteria."""
        cards = [card for card in self._cards if card <= value]
        return max(cards) if cards else -1

    def _lowest_but_not_lower_than(self, value: int) -> int:
        """Returns -1 if no card matches the criteria."""
        cards = [card for card in self._cards if card >= value]
        return min(cards) if cards else -1

    # TODO: Should see the cards from the start of the round, not in the middle of the round...
    @property
    def cards(self) -> list[int]:
        return self._cards

    @property
    def points(self) -> int:
        return self._points


class RandomPlayer(Player):
    def action(self, active_value: int, other_players: list[Player]) -> int:
        return random.choice(self._cards)


class StaticPlayer(Player):
    def action(self, active_value: int, other_players: list[Player]) -> int:
        main_card = self._highest_but_not_higher_than(active_value + 5)
        return main_card if main_card != -1 else self._highest_card()

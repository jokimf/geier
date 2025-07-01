from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class PublicPlayerInfo:
    cards: list[int]
    points: int


class Player(ABC):
    def __init__(self) -> None:
        self._cards: list[int] = [card for card in range(1, 16)]
        self._points: int = 0

    def __repr__(self) -> str:
        return f'P:{self._points}'

    @abstractmethod
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

    @property
    def cards(self) -> list[int]:
        return self._cards

    @property
    def points(self) -> int:
        return self._points
    
    def opponent_info(self) -> PublicPlayerInfo:
        return PublicPlayerInfo(self._cards, self._points)
    
    def reset(self) -> None:
        self._cards: list[int] = [card for card in range(1, 16)]
        self._points: int = 0
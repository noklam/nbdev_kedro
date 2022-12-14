# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'foo', 'Card', 'CardAttrs', 'CardDataclass']

# %% ../00_core.ipynb 3
import attrs
from dataclasses import dataclass
def foo(): pass

# %% ../00_core.ipynb 4
suits = ["♣️","♦️","♥️","♠️"]
ranks = [None, "A"] + [str(x) for x in range(2,11)] + ["J", "Q", "K"]

# %% ../00_core.ipynb 5
class Card:
    "Playing Card"
    def __init__(self, suit, rank):
        self.suit, self.rank = suit, rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__ = __str__

# %% ../00_core.ipynb 6
@attrs.define
class CardAttrs:
    "Playing Card"
    suit: str
    rank: str

# %% ../00_core.ipynb 7
@dataclass
class CardDataclass:
    "Playing Card"
    suit: str
    rank: str

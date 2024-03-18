# characters.py
# api for the docs website coming soon.
# made by mindset

from typing import Optional
from dataclasses import dataclass

@dataclass
class DBLCharacter:
    name: str
    rarity: str
    charatags: Optional[str] = None
    id: Optional[int] = None

# characters, only very little for now. adding alot more!
characters = [
    DBLCharacter(name="Super Baby 2", rarity="LL", charatags="DBL69-01S", id=601),
    DBLCharacter(name="Super Vegeta", rarity="LL", charatags="DBL68-01S", id=597),
    DBLCharacter(name="Super #17", rarity="LL", charatags="DBL67-05S", id=595),
    DBLCharacter(name="GT Goku", rarity="LL", charatags="DBL67-01S", id=588),
    DBLCharacter(name="Goku & Bardock", rarity="LL TagTeam", charatags="DBL66-01S", id=583),
    DBLCharacter(name="Super Saiyan Goku (Namek)", rarity="LL", charatags="DBL62-04S", id=563),
    DBLCharacter(name="Trunks (Parasitism) Baby", rarity="SP", charatags="DBL69-02S", id=602)
]

#1/usr/bin/python3
from dataclasses import dataclass

@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"

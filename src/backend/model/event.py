from dataclasses import dataclass

@dataclass
class Event:
    name: str
    description: str
    location: str
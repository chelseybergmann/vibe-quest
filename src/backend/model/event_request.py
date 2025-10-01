from dataclasses import dataclass

@dataclass
class EventRequest:
    mood: str
    city: str = None
    date: str




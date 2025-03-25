from enum import Enum

class Choice(Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    lizard = "lizard"
    spock = "spock"

    @staticmethod
    def from_string(s: str):
        try:
            return Choice[s.lower()]
        except KeyError:
            return None
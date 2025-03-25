# Ben Vozza - Automata Technical Assessment - Rock Paper Scissors Lizard Spock (CLI)

This is **Ben Vozza's submission** for the **Automata Technical Assessment**.  
It is a Python-based command-line implementation of the extended _Rock Paper Scissors Lizard Spock_ game.

---

## Game Overview

The game extends the classic Rock-Paper-Scissors with two additional moves: **Lizard** and **Spock**, based on the version from *The Big Bang Theory*.

### Rules

| Choice    | Beats                  | Reason                           |
|-----------|------------------------|----------------------------------|
| Scissors  | Paper, Lizard          | Cuts Paper, Decapitates Lizard   |
| Paper     | Rock, Spock            | Covers Rock, Disproves Spock     |
| Rock      | Scissors, Lizard       | Crushes Scissors, Crushes Lizard |
| Lizard    | Paper, Spock           | Eats Paper, Poisons Spock        |
| Spock     | Scissors, Rock         | Smashes Scissors, Vaporises Rock |

---

## 🚀 How to Run

###  Prerequisites

- Python 3.6 or higher installed

### ▶ Run the Game

```bash
python app/main.py
```


### Features

- Interactive CLI
- Score tracking between rounds
- Game reset option
- Support for all 5 move types with reason-based win messages
- Input validation with helpful prompts


### Commands During Play

After each round, you will be prompted with:

- [y] → Play another round
- [r] → Reset the game (scores go back to 0)
- [n] → Quit and view final scores


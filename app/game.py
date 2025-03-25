from app.enums import Choice

OPPONENT_CHOICES_BEAT_BY_CHOICE = {
    Choice.scissors: {
        Choice.paper: "Cuts Paper",
        Choice.lizard: "Decapitates Lizard"
    },
    Choice.paper: {
        Choice.rock: "Covers Rock",
        Choice.spock: "Disproves Spock"
    },
    Choice.rock: {
        Choice.scissors: "Crushes Scissors",
        Choice.lizard: "Crushes Lizard"
    },
    Choice.lizard: {
        Choice.paper: "Eats Paper",
        Choice.spock: "Poisons Spock"
    },
    Choice.spock: {
        Choice.scissors: "Smashes Scissors",
        Choice.rock: "Vaporizes Rock"
    }
}


class Game:
    def __init__(self, user_1: str, user_2: str):
        self.user_1 = user_1
        self.user_2 = user_2
        self.user_1_score = 0
        self.user_2_score = 0

    def reset(self):
        self.user_1_score = 0
        self.user_2_score = 0
        print("Scores Reset!")

    def play(self, user_1_choice: Choice, user_2_choice: Choice):
        print(f"\n{self.user_1} chose {user_1_choice.value}, {self.user_2} chose {user_2_choice.value}")

        if user_1_choice == user_2_choice:
            print("It's a draw!")
            return

        user_1_wins = user_2_choice in OPPONENT_CHOICES_BEAT_BY_CHOICE[user_1_choice]
        user_2_wins = user_1_choice in OPPONENT_CHOICES_BEAT_BY_CHOICE[user_2_choice]

        if user_1_wins:
            reason = OPPONENT_CHOICES_BEAT_BY_CHOICE[user_1_choice][user_2_choice]
            self.user_1_score += 1
            print(f"{self.user_1} wins this round! {user_1_choice.value.capitalize()} {reason}")
        elif user_2_wins:
            reason = OPPONENT_CHOICES_BEAT_BY_CHOICE[user_2_choice][user_1_choice]
            self.user_2_score += 1
            print(f"{self.user_2} wins this round! {user_2_choice.value.capitalize()} {reason}")
        else:
            print("Invalid move combination.")

    def get_scoreboard(self):
        print("\n--- Scoreboard ---")
        print(f"{self.user_1}: {self.user_1_score}")
        print(f"{self.user_2}: {self.user_2_score}")
        if self.user_1_score == self.user_2_score:
            print("It's a draw overall!")
        else:
            winner = self.user_1 if self.user_1_score > self.user_2_score else self.user_2
            print(f"{winner} is winning!")
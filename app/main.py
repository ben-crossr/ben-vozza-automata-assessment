from app.enums import Choice
from app.game import Game

def prompt_choice(user: str) -> Choice:
    valid_choices = [c.value for c in Choice]
    while True:
        choice_input = input(f"{user}, enter your move ({', '.join(valid_choices)}): ").strip().lower()
        try:
            return Choice(choice_input)
        except ValueError:
            print("❌ Invalid choice, please try again.")

def main():
    print("👋 Welcome to Rock Paper Scissors Lizard Spock!\n")
    user_1 = input("Enter name for Player 1: ").strip()
    user_2 = input("Enter name for Player 2: ").strip()

    game = Game(user_1, user_2)

    while True:
        user_1_choice = prompt_choice(user_1)
        user_2_choice = prompt_choice(user_2)

        game.play(user_1_choice, user_2_choice)
        game.get_scoreboard()

        print("\nWhat would you like to do next?")
        print("  [y] Play another round")
        print("  [r] Reset game")
        print("  [n] Quit")

        next_action = input("Choice: ").strip().lower()

        if next_action == "y":
            continue
        elif next_action == "r":
            game.reset()
        elif next_action == "n":
            print("\n🎉 Final scores:")
            game.get_scoreboard()
            print("Thanks for playing!")
            break
        else:
            print("❌ Invalid input. Continuing to next round.")


if __name__ == '__main__':
    main()
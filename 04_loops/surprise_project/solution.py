"""Number Guessing Game - Solution"""

import random


def get_difficulty():
    print("\nSelect difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-500, 10 attempts)")

    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice == 1:
                return 1, 50, 10, "Easy"
            elif choice == 2:
                return 1, 100, 7, "Medium"
            elif choice == 3:
                return 1, 500, 10, "Hard"
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Enter a number (1-3).")


def get_valid_guess(low, high, attempt, max_attempts):
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: "))
            if low <= guess <= high:
                return guess
            print(f"Guess must be between {low} and {high}.")
        except ValueError:
            print("Please enter a valid number.")


def play_round(difficulty_name, low, high, max_attempts):
    secret = random.randint(low, high)
    attempt = 1

    print(f"\nGuess the number between {low} and {high}!")

    while attempt <= max_attempts:
        guess = get_valid_guess(low, high, attempt, max_attempts)

        if guess == secret:
            print(f"Correct! You guessed it in {attempt} attempts!")
            return attempt
        elif guess < secret:
            print("Higher!")
        else:
            print("Lower!")

        attempt += 1

    print(f"Out of attempts! The number was {secret}.")
    return None


def show_high_scores(scores):
    if not scores:
        print("\nNo high scores yet!")
        return

    print("\n=== HIGH SCORES ===")
    for diff in ["Easy", "Medium", "Hard"]:
        diff_scores = [s for s in scores if s[0] == diff]
        if not diff_scores:
            continue
        diff_scores.sort(key=lambda x: x[1])
        print(f"\n{diff}:")
        for rank, (_, attempts, name) in enumerate(diff_scores[:5], 1):
            print(f"  {rank}. {name} - {attempts} attempts")


def main():
    high_scores = []

    print("=== NUMBER GUESSING GAME ===")

    while True:
        low, high, max_attempts, difficulty_name = get_difficulty()
        result = play_round(difficulty_name, low, high, max_attempts)

        if result is not None:
            name = input("Enter your name: ").strip() or "Anonymous"
            high_scores.append((difficulty_name, result, name))

        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            break

    show_high_scores(high_scores)
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()

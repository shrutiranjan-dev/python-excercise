# Surprise Project: Number Guessing Game

## Objective
Build an interactive number guessing game where the player tries to guess a random number within a range, receiving hints along the way.

## Requirements

### 1. Difficulty Levels
| Level | Range | Max Attempts |
|---|---|---|
| Easy | 1-50 | 10 |
| Medium | 1-100 | 7 |
| Hard | 1-500 | 10 |

### 2. Game Flow
1. Display welcome message and ask for difficulty selection
2. Generate a random number in the appropriate range
3. Loop until the player guesses correctly or runs out of attempts
4. After each guess, tell the player "Higher!" or "Lower!"
5. Track the number of attempts
6. When guessed correctly or out of attempts, show the result
7. Store the score (attempts taken) in a high scores list
8. Ask if the player wants to play again
9. When quitting, show the high scores leaderboard

### 3. High Scores
- Store scores as tuples: `(difficulty, attempts, player_name)`
- Lower attempts = better score
- Show top 5 scores per difficulty

### 4. Input Validation
- Validate that the guess is within the range
- Handle non-numeric input gracefully
- Validate difficulty choice

## Example Run
```
=== NUMBER GUESSING GAME ===
Select difficulty:
1. Easy (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard (1-500, 10 attempts)
Enter choice (1-3): 2

Guess the number between 1 and 100!
Attempt 1/7: 50
Higher!
Attempt 2/7: 75
Lower!
Attempt 3/7: 62
Higher!
Attempt 4/7: 68
Lower!
Attempt 5/7: 65
Correct! You guessed it in 5 attempts!

Enter your name: Alice

Play again? (yes/no): no

=== HIGH SCORES ===
Medium:
1. Alice - 5 attempts
```

## Challenge Extensions
1. Add timer mode (score based on time taken)
2. Add two-player mode (alternate guessing)
3. Add hint mode (after 3 wrong guesses, reveal if number is even/odd)
4. Save high scores to a file for persistence

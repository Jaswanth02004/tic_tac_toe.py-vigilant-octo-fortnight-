# tic_tac_toe.py-vigilant-octo-fortnight-
A two-player terminal Tic-Tac-Toe game built in Python using lists, dictionaries, sets, and tuples for board rendering, move validation, and win/draw detection.

# 🐍 Python CLI Tic-Tac-Toe Game

A classic two-player (`X` vs `O`) command-line Tic-Tac-Toe game built using core Python data structures—no external libraries required. This is the sixth and final installment in a Python learning repository.

## 📌 Features & Core Concepts

The script (`TIC TAC TOE GAME.py`) brings together fundamental Python concepts in an interactive console game:

- **Board State & Rendering** – Uses a 9-element list (`1`–`9`) to represent grid positions and formats a clean 3×3 terminal board via `display_board()`.
- **Player Management** – Maps symbols (`"X"` and `"O"`) to `"Player-1"` and `"Player-2"` using a dictionary and alternates turns automatically.
- **Move Validation** – Tracks taken squares in a `set` (`occupied`) to prevent overwriting existing moves and validates that inputs stay within `1–9`.
- **Win & Draw Detection** – Checks all 8 winning index combinations stored in a tuple of tuples (`winning_combintions`) after every turn, and detects a draw once all 9 spaces are filled.

## 🚀 How to Run

1. Ensure you have **Python 3.x** installed.
2. Run the game directly from your terminal:
   ```bash
   python "TIC TAC TOE GAME.py"

   Welcome to the TIC TAC TOE GAME

1 | 2 | 3

--+---+--

4 | 5 | 6

--+---+--

7 | 8 | 9

--+---+--


Player-1-X-> Choose between 1-9: 5

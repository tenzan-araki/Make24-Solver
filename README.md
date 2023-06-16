# Make 24 Solver

There is a card game called **Make 24**, where the goal is to reach 24 by applying arithmetic operations on a set of four numbered cards. My cousin, who goes to primary school, is so good at this game that no one in the family stands a chance against her. Since I live abroad, I never challenged her to this game until this traumatic summer holiday. Long story short, I felt like a chihuahua trying to take on a bull.

Brutally defeated, I sat on my bed that night thinking about how I would never be able to win directly. But as any chihuahua would do, I had to keep barking as I retreat to look strong and less embarrassing. So here, with tears of lameness, I present to you a solver that I wrote to prove that I can still win as long as I have a computer. I used it against her later that week quite successfully, and from what I heard, she wrote an essay about it for her homework. I feel honored to be mentioned in the champion's assignment.

So the code here should be useful for those who have a smart cousin. For the sole purpose of winning, just try running the code in the notebook `Demo of Make 24 Solver.ipynb`. Solutions are found in milliseconds, so winning the game is dependent on your typing speed. So far I have no plans to improve the code algorithmically or by enabling audio or camera functionalities, because it should already be sufficiently fast to defeat most cousins. Although, I might still do it at some point when I have to procrastinate again.

## Rules
Here are "our" rules for **Make 24**. It could differ from other standard rules, but it is mostly consistent with them, well-defined, and entertaining.

1. Game Components:
   - A standard deck of 52 playing cards.
   - Each card has a rank and a suit, but suits are irrelevant here.
   - For the purposes of this version of the game:
     - Cards with ranks A, J, Q, and K are assigned values 1, 11, 12, and 13 respectively.
     - All other cards have their face value (2-10).

2. Objective:
   - The goal of the game is to be the first player to find a valid arithmetic expression using the four given cards to equal the target number 24.
   - You must use all four cards exactly once in your expression.
   - Only basic arithmetic operations (addition, subtraction, multiplication, and division) and parentheses are allowed.
   - Intermediate expressions can be fractions.

3. Setup:
   - Four cards are dealt from the deck and placed face up on the table.
   - The four cards are placed on the side so that the remaining number of cards in the deck reduces after either a 24 has been made by a player, the combination of numbers was determined to have no solutions, or neither player found a solution.

4. Gameplay:
   - Players attempt to find a valid arithmetic expression using the four cards to equal the target number 24, as quickly as possible.
   - The first player to find a valid expression scores one point.
   - If neither player finds a solution after a long time, it is a draw and no one scores.
   - If a player thinks that there is no solution given the combination of numbers, the player can call "no solution". In that case, the opponent has ten seconds to find a solution. If the opponent cannot find a solution within the time limit, the player who said "no solution" scores one point.

5. Scoring:
   - The first player to find a valid arithmetic expression that equals 24 using the given cards scores one point.
   - If a player says "no solution" and their opponent fails to find a solution within the time limit, the player who said "no solution" scores one point.
   - No one scores in a draw.

6. Winning:
   - Keep dealing four cards from the deck until there are no cards remaining.
   - The player with the highest score at the end wins.

## Installation
After cloning the repository, the `make24` package can be installed by running
```
pip install -e .
```
in the root directory. This allows us to simply import our functions, e.g., by running
```
from make24 import make24_solver
```
in Python.

## Structure
```
.
├── README.md
├── VERSION.txt
├── demos
│   ├── Demo of Make 24 Solver.ipynb
│   ├── Generate neq_eqs_TF array.ipynb
│   └── neq_eqs_TF.csv
├── make24
│   ├── __init__.py
│   ├── analysis.py
│   ├── solver.py
│   └── utils.py
├── requirements.txt
└── setup.py

```

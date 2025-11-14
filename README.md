# Make 24 Solver

There is a card game called **Make 24**, where the goal is to reach 24 very quickly by applying arithmetic operations on a set of four randomly drawn cards. My cousin, who goes to primary school, is so good at this game that no one in the family stands a chance against her. I used to be the last person who has not played against her, but I also got brutally defeated. So here, I present to you a solver that I wrote to prove that I can still win as long as I'm allowed to use a computer. Assisted by CPU, I got my revenge, and apparently she wrote an essay about it for her homework. I feel honored to be mentioned in the champion's assignment.

So the code here should be useful for those who have a smart cousin. For the sole purpose of winning, just try running the code in the notebook `Demo of Make 24 Solver.ipynb`. Solutions are found in milliseconds, so winning the game depends on your typing speed. It is a brute-force solver and I have no plans to improve the code algorithmically or by enabling audio or camera functionalities, because it should already be sufficiently fast to defeat most cousins.

## Rules
Here are "our" rules for **Make 24**, which might differ from other standard rules.

1. Objective:
   
   Given 4 cards (drawn from a standard 52-card deck), use arithmetic to make the value 24. Each card value must be used exactly once. Valid expressions may use parentheses to change evaluation order.

2. Card values:
   - Ace (A) = 1
   - 2 to 10 = their face values
   - Jack (J) = 11, Queen (Q) = 12, King (K) = 13
   - Jokers are not used
  
3. Allowed operations:
   - Addition +
   - Subtraction -
   - Multiplication ×
   - Division ÷
   - Parentheses ( ) to group operations
  
4. Example:
   
   Say the four cards were 6, 3, 2, and A. Then, a possible solution would be ( 3 - 1 ) × ( 6 × 2 ) = 24.

5. Gameplay:
   - Players attempt to find a valid arithmetic expression using the four cards to equal the target number 24, as quickly as possible.
   - The first player to find a valid expression scores one point.
   - If neither player finds a solution after some pre-specified time, it is a draw and no one scores.
   - If a player thinks that there is no solution given the combination of numbers, the player can call "no solution". In that case, the opponent has some pre-specified amount of time to find a solution. If the opponent cannot find a solution within the time limit, the player who called "no solution" scores one point.

6. Winning:
   - Keep drawing four cards from the deck until there are no cards remaining.
   - The player with the highest score in the end wins.

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

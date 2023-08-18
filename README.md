# Python_Blackjack_Game
The Python Blackjack Game project aims to develop a console-based implementation of the classic card game Blackjack, also known as 21. For ITSC1110
The Python Blackjack Game project aims to develop a console-based implementation of the classic card game Blackjack, also known as 21. Blackjack is a game where players compete against the dealer to reach a hand value as close to 21 as possible without exceeding it. This project will provide a hands-on opportunity to practice object-oriented programming, game logic, and user interaction in Python.

1. **Player Interaction:** Allow players to interact with the game by making decisions such as hitting (drawing a card), standing (ending their turn), and doubling down (doubling their bet and drawing one more card).
2. **Dealer Logic:** Implement the dealer's logic to follow a specific set of rules for drawing and standing based on their hand value.
3. **Random Numbers:** In order to get random numbers to represent cards use the following code 
```python
#at the top
import random

randomNum = random.randint(1, 11)
#randomNum now hold a random from 1 to 11 inclusive

```
4. **[BONUS]Betting System:** Introduce a basic betting system where players can place bets at the beginning of each round.
5. **Scoring and Winning Conditions:** Implement scoring mechanics to determine the winner of each round based on hand values, accounting for cases of busting (exceeding 21) and achieving a blackjack.
6. **Game Flow:** Design a game loop that guides players through the various stages of the game, including initial card dealing, player actions, dealer actions, and determining the winner.
**Coding Style:**
- Use descriptive variable names in camel case (e.g., `player_hand`, `dealer_hand`, `current_bet`).
- Apply proper indentation for readability.
- Add comments to explain the purpose and functionality of critical code sections.
- Structure your code in an organized and elegant manner, separating concerns into classes and functions.
**Submission Requirements:**
1. **Code Files:**
    - Create a Python file named `blackjack_game.py` containing the implementation.
    - Save the file in a project folder named `Blackjack`.
2. **Pseudocode or Flowchart:**
    - Create a separate text or image file named `blackjack_steps.txt` or `blackjack_steps.png`.
    - Outline the major steps and flow of your program using pseudocode or a flowchart.
3. **Project Information PDF:**
    - Create a PDF named `project_info.pdf`.
    - Describe any additional features added to the basic requirements.
    - Explain the status, any incomplete parts, and issues faced.
    - Discuss both the easy and challenging aspects of the project and how you overcame challenges.

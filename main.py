import random
from footballers import players

player_to_guess = random.choice(list(players.keys()))
hint = 0

def check_guess(user_guess):

    global hint

    if user_guess.lower() == player_to_guess.lower():
        return {
            "correct": True,
            "message": "🎉 Correct Answer!"
        }

    hint += 1

    if hint == 1:
        return {
            "correct": False,
            "message": f"Country: {players[player_to_guess]['Country']}"
        }

    elif hint == 2:
        return {
            "correct": False,
            "message": f"Club: {players[player_to_guess]['Club']}"
        }

    elif hint == 3:
        return {
            "correct": False,
            "message": f"Age: {players[player_to_guess]['Age']}"
        }

    elif hint == 4:
        return {
            "correct": False,
            "message": f"Position: {players[player_to_guess]['Position']}"
        }

    else:
        return {
            "correct": False,
            "message": f"The answer was {player_to_guess}"
        }
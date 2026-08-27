import tkinter as tk
import random
from footballers import players

player_to_guess = random.choice(list(players.keys()))
hint = 0


def check_guess():

    global hint

    user_guess = guess_entry.get().strip()

    if not user_guess:
        result_label.config(text="Please enter a player name!")
        return

    if user_guess.lower() == player_to_guess.lower():

        result_label.config(
            text=" Correct Answer!"
        )

        hint_label.config(
            text=f"The player was {player_to_guess}"
        )

        return

    hint += 1

    result_label.config(text=" Incorrect Answer!")

    if hint == 1:
        hint_label.config(
            text=f" Country: {players[player_to_guess]['Country']}"
        )

    elif hint == 2:
        hint_label.config(
            text=f" Club: {players[player_to_guess]['Club']}"
        )

    elif hint == 3:
        hint_label.config(
            text=f" Age: {players[player_to_guess]['Age']}"
        )

    elif hint == 4:
        hint_label.config(
            text=f"Position: {players[player_to_guess]['Position']}"
        )

    else:
        hint_label.config(
            text=f"Game Over! The answer was {player_to_guess}"
        )

    guess_entry.delete(0, tk.END)


root = tk.Tk()

root.title("Guess The Football Player")
root.geometry("500x400")


title = tk.Label(
    root,
    text=" GUESS THE PLAYER ",
    font=("Arial", 20, "bold")
)

title.pack(pady=30)


instruction = tk.Label(
    root,
    text="Enter the name of the football player",
    font=("Arial", 12)
)

instruction.pack()


guess_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)

guess_entry.pack(pady=15)


guess_button = tk.Button(
    root,
    text="GUESS",
    font=("Arial", 12, "bold"),
    command=check_guess
)

guess_button.pack(pady=10)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)

result_label.pack(pady=10)


hint_label = tk.Label(
    root,
    text="",
    font=("Arial", 13)
)

hint_label.pack(pady=10)


root.mainloop()
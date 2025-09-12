from random import randint

# Läser input med meddelandet prompt, försöker omvandla till int.


def input_int(prompt) -> int:
    """
    Prompts the user to enter an integer value, repeatedly asking until a valid integer is provided.

    Args:
        prompt (str): The message displayed to the user when requesting input.

    Returns:
        int: The integer value entered by the user.

    Raises:
        None: The function handles invalid input internally and does not raise exceptions.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def game_round() -> int:
    random_number = randint(1, 10)
    estimated_guesses = input_int("Hur många gissningar behöver du för att gissa rätt?")
    number_of_guesses = 0
    while True:
        guess = input_int("Gissa ett nummer mellan 1 och 10: ")
        number_of_guesses += 1

        if random_number > guess:
            print(f"Du gissade {guess}, det är för lågt.")
        elif random_number < guess:
            print(f"Du gissade {guess}, det är för högt.")
        else:
            print(f"Grattis, {guess} är rätt")
            print(f"Du räknade med att det skulle ta {estimated_guesses} gånger att gissa rätt.")
            print(f"Det tog dig {number_of_guesses} att gissa rätt.")
            round_points = abs(estimated_guesses - number_of_guesses) + 1
            print(f"Du fick {round_points} poäng denna omgång (ju lägre desto bättre).")
            return round_points

POINTS = 0
while True:
    print("Välkommen!")
    POINTS += game_round()
    print(f"Du har nu {POINTS}")
    choice = input("Vill du spela igen? [Y/n]")
    if choice.lower() == "n":
        break

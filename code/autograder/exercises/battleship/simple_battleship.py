BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

from random import randint

# Gets user input; if the number is greater than 4 it exits
number: int = input("Pick a secret boat location between 1 and 4: ")
if (number > 4):
    print(f"Error! {number} too high!")
    exit()
elif(number < 1):
    print(f"Error! {number} too low!")
    exit()


# Gets user input; if the number is greater than 4 it exits
guess_number: int = int(input("Guess a number between 1 and 4: "))
if (guess_number > 4):
    print(f"Error! {guess_number} too high!")
    exit()
elif(guess_number < 1):
    print(f"Error! {guess_number} too low!")
    exit()

# If they guessed right the box will be red, if not it will be white
if guess_number == number:
    guess_box = RED_BOX
else:
    guess_box = WHITE_BOX

emoji_str: str = ""

# Adds the red/white box if their guess is 1, adds blue box otherwise
if guess_number == 1:
    emoji_str = emoji_str + guess_box
else:
    emoji_str = emoji_str + BLUE_BOX

# Adds the red/white box if their guess is 2, adds blue box otherwise
if guess_number == 2:
    emoji_str = emoji_str + guess_box
else:
    emoji_str = emoji_str + BLUE_BOX

# Adds the red/white box if their guess is 3, adds blue box otherwise
if guess_number == 3:
    emoji_str = emoji_str + guess_box
else:
    emoji_str = emoji_str + BLUE_BOX

# Adds the red/white box if their guess is 4, adds blue box otherwise
if guess_number == 4:
    emoji_str = emoji_str + guess_box
else:
    emoji_str = emoji_str + BLUE_BOX

# Prints the string of boxes
print(emoji_str)
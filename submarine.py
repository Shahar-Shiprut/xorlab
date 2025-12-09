import random
from typing import Callable

NUM_ROWS = 10
NUM_COLS = 10

def play_submarine(num_cols: int, num_rows: int, stdin: Callable, stdout: Callable) -> None:
    """
    plays the submarine game 
    :param num_cols: the number of columns in the board
    :param num_rows: the number of rows in the board
    :param stdin: the function to call to get input
    :param stdout: the function to call to get output 
    """
    x, y = random.randint(1, num_cols), random.randint(1, num_rows)
    attempts = 0
    while True:
        try:
            row = int(stdin("הכנס שורה: "))
            col = int(stdin("הכנס עמודה: "))
        except ValueError:
            stdout("Didn't understand the input please try again")
            continue

        if (row <= 0) or (row > num_rows) or (col <= 0) or (col > num_cols):
            stdout("values are out of bounds please try again")
        
        attempts += 1

        if (row == x) and (col == y):
            stdout("בול")
            stdout("לקח", attempts, "ניסיונות")
            break
        elif (-1 <= row - x <= 1) and (-1 <= col - y <= 1):
            stdout("קרוב")
        elif (row == x) or (col == y):
            stdout("מעניין")
        else:
            stdout("תמשיך לחשוב")

def main() -> None:
    play_submarine(NUM_COLS, NUM_ROWS, input, print)

if __name__ == "__main__":
    main()

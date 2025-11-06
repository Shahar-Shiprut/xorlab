import random

NUM_ROWS = 10
NUM_COLS = 10

def play_submarine() -> None:
    """ plays the submarine game """
    x, y = random.randint(1, NUM_COLS), random.randint(1, NUM_ROWS)
    attempts = 0
    while True:
        try:
            row = int(input("הכנס שורה: "))
            col = int(input("הכנס עמודה: "))
        except ValueError:
            print("Didn't understand the input please try again")
            continue

        if (row <= 0) or (row > NUM_ROWS) or (col <= 0) or (col > NUM_COLS):
            print("values are out of bounds please try again")
        
        attempts += 1

        if (row == x) and (col == y):
            print("בול")
            print("לקח", attempts, "ניסיונות")
            break
        elif (-1 <= row - x <= 1) and (-1 <= col - y <= 1):
            print("קרוב")
        elif (row == x) or (col == y):
            print("מעניין")
        else:
            print("תמשיך לחשוב")

def main() -> None:
    play_submarine()

if __name__ == "__main__":
    main()

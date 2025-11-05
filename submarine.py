import random

def play_submarine() -> None:
    """ plays the submarine game """
    x, y = random.randint(1, 10), random.randint(1, 10)
    attempts = 0
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        attempts += 1

        if (row == x) and (col == y):
            print("בול")
            print("took", attempts, "attempts")
            break
        elif (-1 <= row - x <= 1) and (-1 <= col - y <= 1):
            print("קרוב")
        elif (row == x) or (col == y):
            print("מעניין")
        else:
            print("תמשיך לחשוב")
        

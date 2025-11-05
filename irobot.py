def is_int(s: str):
    """
    Checks if a given string can be safely converted to an integer.
    :param s: The string to check.
    :returns: True if the string can be converted to an integer, False otherwise.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

def move(x: int, y: int, dir: str) -> tuple[int, int]:
    """ 
    returns a new set of coordinates moved in direction `dir` 
    :param dir: Can be 'r' 'l' 'u' 'd'
    """
    if dir == "r":
        return (x + 1 if x < 4 else 4), y
    if dir == "l":
        return (x - 1 if x > 0 else 0), y
    if dir == "u":
        return x, (y - 1 if y > 0 else 0)
    if dir == "d":
        return x, (y + 1 if y < 4 else 4)

def main() -> None:
    floor = [["." for _ in range(5)] for _ in range(5)]
    x, y = 0, 0
    dir = "d"
    enabled = False

    # get and run instructions
    instructions = input("Instructions: ").split(" ")
    for inst in instructions:
        if inst in ("right", "left", "up", "down"):
            dir = inst[0]
        elif inst == "on":
            enabled == True
        elif inst == "off":
            enabled == False
        elif is_int(inst):
            for i in range(inst):
                x, y = move(x, y, dir)
                floor[y][x] = "X"

    # print floor
    for row in floor:
        print(" ".join(row))


if __name__ == "__main__":
    main()
            

PROMPT = """1. Get Word
2. Add Word
3. Delete Word
4. Exit
Enter Choice: """

INPUT_EXIT = 4

def get_word(dictionary: dict) -> None:
    """prints definition to a given word from `dictionary`"""
    word = input("Word to get: ")
    if word in dictionary:
        print(f"{word} means {dictionary[word]}")
    else:
        print(f"The word {word} does not exist!")


def add_word(dictionary: dict) -> None:
    """adds word to `dictionary` with definition"""
    word = input("Word to add: ")
    dictionary[word] = input(f"Meaning of {word}: ")
    print(f"{word}={dictionary[word]} was added.")


def del_word(dictionary: dict) -> None:
    """deletes word from `dictionary`"""
    word = input("Word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print(f"{word} was erased")
    else:
        print(f"Word does not exist.")

COMMANDS = [None, get_word, add_word, del_word]

def main() -> None:
    """run main event loop"""
    dictionary = dict()
    
    while (inp := input(PROMPT)) != INPUT_EXIT:
        COMMANDS[int(inp)](dictionary)
        
    print("Goodbye!")


if __name__ == "__main__":
    main()

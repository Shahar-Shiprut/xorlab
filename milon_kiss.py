PROMPT = """1. Get Word
2. Add Word
3. Delete Word
4. Exit
Enter Choice: """

INPUT_GET = 1
INPUT_ADD = 2
INPUT_DEL = 3
INPUT_EXT = 4

dictionary = dict()


def get_word(word: str) -> None:
    """prints definition to `word`"""
    if word in dictionary:
        print(f"{word} means {dictionary[word]}")
    else:
        print(f"The word {word} does not exist!")


def add_word(word: str, defi: str) -> None:
    """adds `word` to dictionary with definition `defi`"""
    dictionary[word] = defi
    print(f"{word}={dictionary[word]} was added.")


def del_word(word: str) -> None:
    """deletes `word` from dictionary"""
    if word in dictionary:
        del dictionary[word]
        print(f"{word} was erased")
    else:
        print(f"Word does not exist.")


def main() -> None:
    """run main event loop"""

    running = True
    while running:
        inp = input(PROMPT)
        
        if inp == INPUT_GET:
            word = input("Word to get: ")
            get_word(word)
            
        elif inp == INPUT_ADD:
            word = input("Word to add: ")
            add_word(word, input(f"Meaning of {word}: "))
            
        elif inp == INPUT_DEL:
            word = input("Word to delete: ")
            del_word(word)
            
        elif inp == INPUT_EXT:
            running = False
            print("Goodbye!")


if __name__ == "__main__":
    main()

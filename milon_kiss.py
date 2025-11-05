def main():
    dictionary = dict()
    running = True
    while running:
        print("1. Get Word")
        print("2. Add Word")
        print("3. Delete Word")
        print("4. Exit")

        inp = input("Enter Choice: ")
        if inp == 1:
            word = input("Word to get: ")
            if word in dictionary:
                print(f"{word} means {dictionary[word]}")
            else:
                print(f"The word {word} does not exist!")
        elif inp == 2:
            word = input("Word to add: ")
            dictionary[word] = input(f"Meaning of {word}: ")
            print(f"{word}={dictionary[word]} was added.")
        elif inp == 3:
            word = input("Word to delete: ")
            if word in dictionary:
                del dictionary[word]
                print(f"{word} was erased")
            else:
                print(f"Word does not exist.")
        elif inp == 4:
            running = False
            print("Goodbye!")

if __name__ == "__main__":
    main()

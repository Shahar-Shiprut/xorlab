import os

def main() -> None:
    folder = input("Enter folder name: ")
    for file in os.listdir(folder):
        if not file.startswith("baby"): 
            continue

        year = file.split(".")[0][4:]
        with open(file) as f:
            _, boy, girl = f.readline().split(", ")

        print(f"in year {year} the names {boy}, {girl} was the most common for boys and girls respectively")

if __name__ == "__main__":
    main()

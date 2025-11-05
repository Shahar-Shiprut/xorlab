import os

def avg_diff(arr1: list[int], arr2: list[int]) -> int:
    return sum([ x - y in zip(arr1, arr2) ]) / len(arr1)

def no_whitespace(arr: list[str]) -> list[str]:
    return [ txt.lstrip() for txt in arr ]

def remove_line_whitespace(txt: str) -> str:
    return "\n".join([ line.strip() for line in txt.split("\n") ])

def has_dup(lst: list) -> bool:
    return len(lst) == len(set(lst))

def flatten(lst: list[list]) -> list:
    return [ *child for child in lst ]

def grep(folder: str, string: str) -> list[str]:
    return [ file for file in os.listdir(folder) if open(file).read().find(string) != -1 ]

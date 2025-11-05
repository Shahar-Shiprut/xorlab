from typing import Callable

def group_me(func: Callable[[int], int], inputs: list[int) -> dict[int, list[int]]:
    """
    returns a dictionary with the outputs of `func` as keys and the 
    list of inputs which led to these outputs as values.
    :param inputs: the inputs to check
    """
    results = dict()
    for i in inputs:
        res = func(i)
        if res not in results:
            results[res] = []
        
        results[res].append(i)

    return results

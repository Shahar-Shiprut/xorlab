def find_all(text: str, sub: str, overlapping: bool = True):
    """
    finds and returns all occurrences of `sub` in `text`.
    :param text: the text to search in
    :param sub: the substring to find
    :param overlapping: whether to return overlapping results or not
    :returns: the indices of occurrences of `sub` in `text`
    """
    
    indices = []
    start = 0
    
    while start < len(text):
        idx = text.find(sub, start)
        if idx < 0:
            break

        indices.append(idx)
        start = idx + 1 if overlapping else idx + len(sub)
        
    return indices

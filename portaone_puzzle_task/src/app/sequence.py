def build_sequence(path: list[int], fragments: list[str]) -> str:
    if not path:
        return ""

    result = fragments[path[0]]

    for index in path[1:]:
        result += fragments[index][2:]

    return result

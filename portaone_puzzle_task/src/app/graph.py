def build_adjacency(fragments: list[str]) -> list[list[int]]:
    """
    Build adjacency list for every fragment.
    """
    prefixes: dict[str, list[int]] = {}

    for index, fragment in enumerate(fragments):
        prefixes.setdefault(fragment[:2], []).append(index)

    adjacency: list[list[int]] = []

    for fragment in fragments:
        adjacency.append(prefixes.get(fragment[-2:], []))

    return adjacency
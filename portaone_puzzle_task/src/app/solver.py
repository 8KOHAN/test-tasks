from .graph import build_adjacency


def dfs(
    current: int,
    adjacency: list[list[int]],
    visited: list[bool],
    current_path: list[int],
    best_path: list[int],
):
    visited[current] = True
    current_path.append(current)

    if len(current_path) > len(best_path):
        best_path.clear()
        best_path.extend(current_path)

    for next_index in adjacency[current]:
        if not visited[next_index]:
            dfs(
                next_index,
                adjacency,
                visited,
                current_path,
                best_path,
            )

    current_path.pop()
    visited[current] = False


def find_longest_chain(fragments: list[str]) -> list[int]:
    adjacency = build_adjacency(fragments)
    best_path: list[int] = []

    for start in range(len(fragments)):
        visited = [False] * len(fragments)
        current_path: list[int] = []

        dfs(
            start,
            adjacency,
            visited,
            current_path,
            best_path,
        )

    return best_path
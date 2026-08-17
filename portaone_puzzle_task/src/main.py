from app.sequence import build_sequence
from app.solver import find_longest_chain
from utils.file_loader import load_fragments

import time


def main():
    fragments = load_fragments("data/source.txt")

    best_path = find_longest_chain(fragments)

    print(f"Fragments loaded: {len(fragments)}")
    print(f"Longest chain length: {len(best_path)}")

    print("\nFragments:")
    for index in best_path:
        print(fragments[index])

    sequence = build_sequence(best_path, fragments)

    print("\nFinal sequence:")
    print(sequence)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Execution time: {end - start:.3f} s")
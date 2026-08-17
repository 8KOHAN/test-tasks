def read_lines(filename: str) -> list[str]:
    """Read all non-empty lines from a text file."""
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
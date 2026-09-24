"""Input and output patterns; input is kept behind a function for testing."""


def greeting(name: str) -> str:
    """Return a friendly greeting for a non-empty name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name cannot be empty")
    return f"Hello, {cleaned_name}!"


if __name__ == "__main__":
    print(greeting(input("What is your name? ")))

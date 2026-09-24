"""List, dictionary, and set comprehensions."""

squares = [number * number for number in range(6)]
square_lookup = {number: number * number for number in range(4)}
unique_lengths = {len(word) for word in ["python", "data", "python"]}
print(squares, square_lookup, unique_lengths)

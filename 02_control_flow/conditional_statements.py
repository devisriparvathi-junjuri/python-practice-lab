"""Conditions choose a branch based on Boolean expressions."""


def grade_for(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "Needs practice"


if __name__ == "__main__":
    print(grade_for(82))

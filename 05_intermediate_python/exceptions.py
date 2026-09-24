"""Exception handling and custom exceptions."""

class InvalidScoreError(ValueError):
    """Raised when a score is outside the accepted range."""


def validate_score(score: int) -> int:
    if not 0 <= score <= 100:
        raise InvalidScoreError("score must be between 0 and 100")
    return score


try:
    print(validate_score(88))
except InvalidScoreError as error:
    print(f"Invalid input: {error}")

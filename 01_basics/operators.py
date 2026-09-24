"""Arithmetic, comparison, logical, assignment, identity, and membership operators."""

left, right = 10, 3
print("arithmetic", left + right, left - right, left * right, left / right, left // right, left % right)
print("comparison", left > right, left == right)
print("logical", left > 0 and right > 0, left < 0 or right > 0, not left < 0)
score = 10
score += 5
print("assignment", score)
items = ["python", "sql"]
print("membership", "python" in items)
first = second = []
print("identity", first is second)

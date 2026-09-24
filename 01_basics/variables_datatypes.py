"""Variables, naming, built-in types, conversion, and formatting."""

name = "Asha"  # snake_case is the usual Python naming style.
age = 21
height_m = 1.68
is_student = True

print(f"{name} is {age} years old and {height_m:.2f} m tall.")
print(type(name).__name__, type(age).__name__, type(is_student).__name__)
print("String to integer:", int("42"), "integer to string:", str(42))

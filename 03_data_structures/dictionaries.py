"""Dictionaries map keys to values and may contain nested structures."""

student = {"name": "Asha", "marks": {"python": 88, "sql": 79}}
print(student["name"], student["marks"]["python"])
for subject, mark in student["marks"].items():
    print(subject, mark)

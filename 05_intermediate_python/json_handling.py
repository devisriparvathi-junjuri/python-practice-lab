"""JSON converts common Python data to a portable text representation."""

import json

student = {"name": "Asha", "skills": ["Python", "SQL"]}
serialized = json.dumps(student, indent=2)
print(serialized)
print(json.loads(serialized)["skills"])

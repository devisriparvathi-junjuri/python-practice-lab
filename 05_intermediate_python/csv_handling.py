"""CSV is useful for simple table-shaped data."""

import csv
from io import StringIO

buffer = StringIO()
writer = csv.DictWriter(buffer, fieldnames=["name", "score"])
writer.writeheader()
writer.writerow({"name": "Asha", "score": 88})
print(buffer.getvalue())

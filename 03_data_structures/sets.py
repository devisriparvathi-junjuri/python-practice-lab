"""Sets store unique values and support set algebra."""

python_topics = {"loops", "functions", "testing"}
job_topics = {"functions", "testing", "sql"}
print("shared:", python_topics & job_topics)
print("all:", python_topics | job_topics)

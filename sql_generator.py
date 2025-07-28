# sql_generator.py

import re

def natural_language_to_sql(query):
    query = query.lower()

    if "show all" in query or "list all" in query:
        return "SELECT * FROM students"

    elif "average" in query:
        return "SELECT AVG(score) FROM students"

    elif "count" in query:
        return "SELECT COUNT(*) FROM students"

    elif "name" in query:
        return "SELECT name FROM students"

    elif "greater than" in query:
        match = re.search(r"greater than (\d+)", query)
        if match:
            value = match.group(1)
            return f"SELECT * FROM students WHERE score > {value}"

    elif "less than" in query:
        match = re.search(r"less than (\d+)", query)
        if match:
            value = match.group(1)
            return f"SELECT * FROM students WHERE score < {value}"

    return "SELECT * FROM students"

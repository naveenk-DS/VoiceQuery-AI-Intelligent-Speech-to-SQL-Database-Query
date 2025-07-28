def natural_language_to_sql(user_input):
    user_input = user_input.lower()

    if "total students" in user_input:
        return "SELECT COUNT(*) FROM students;"
    elif "average score" in user_input:
        return "SELECT AVG(score) FROM students;"
    elif "passed" in user_input:
        return "SELECT * FROM students WHERE score >= 40;"
    elif "failed" in user_input:
        return "SELECT * FROM students WHERE score < 40;"
    elif "all students" in user_input:
        return "SELECT * FROM students;"
    else:
        return "SELECT * FROM students LIMIT 5;"  # fallback

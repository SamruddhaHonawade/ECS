def check_sql_injection(input_string):
    sql_injection_patterns = ['"', '|', '=', '--', '~','?'," ' "]
    for pattern in sql_injection_patterns:
        if pattern in input_string:
            return f"Possible SQL Injection found."
    return "No SQL Injection detected."

input_string = input("Enter a string to check for SQL injection: ")
result = check_sql_injection(input_string)
print(result)
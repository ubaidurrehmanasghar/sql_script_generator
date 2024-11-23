def sql_script_generator():
    while True:
        try:
            num = int(input("Enter the number of SQL scripts you want to generate: "))
            if num <= 0:
                raise ValueError("Number of scripts must be greater than 0")
            break
        except ValueError as e:
            print(f"Invalid Input: {e}")
    #Supported SQL Functions/Commands
    supported_sql_commands = [
        "CREATE TABLE", "ALTER TABLE", "DROP TABLE", "INSERT INTO", "UPDATE",
        "DELETE", "SELECT", "DISTINCT", "ORDER BY", "GROUP BY", "HAVING",
        "GRANT", "REVOKE", "BEGIN TRANSACTION", "COMMIT", "ROLLBACK",
        "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "COUNT",
        "AVG", "SUM", "MIN/MAX", "CREATE INDEX", "DROP INDEX"
    ]
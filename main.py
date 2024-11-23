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
        #Getting Input for SQL Scripts
    for i in range(1,num+1):
        print(f"\nSQL Script {i}:")
        print("Supported SQL Functions/Commands:", ", ".join(supported_sql_commands))
        command = input("Enter SQL Command: ").strip().upper()
        
        #Checking if the SQL Command is supported
        if command not in supported_sql_commands:
            print(f"Unsupported SQL Command {command}. Please enter a valid SQL Command. Skipping...")
            continue
        
        #Checking SQL Command and Generating SQL Script
        if command == "CREATE TABLE":
            table_name = input("Enter Table Name: ").strip()
            num_columns = int(input("Enter Number of Columns: "))
            columns = []
        for col in range(num_columns):
            column_name = input(f"Enter Column Name {col+1}:").strip()
            column_type = input(f"Enter Column Type {col+1}:").strip()
            primary_key = input(f"Is {column_name} the Primary Key? (Y/N): ").strip().upper() == "Y"
            column_def = f"{column_name} {column_type}"+(" PRIMARY KEY" if primary_key else "")
            columns.append(column_def)
            script = f"CREATE TABLE {table_name} (\n    {',\n'.join(columns)}\n);"
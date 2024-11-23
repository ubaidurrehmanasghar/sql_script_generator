def sql_script_generator():
    while True:
        try:
            num = int(input("Enter the number of SQL scripts you want to generate: "))
            if num <= 0:
                raise ValueError("Number of scripts must be greater than 0")
            break
        except ValueError as e:
            print(f"Invalid Input: {e}")

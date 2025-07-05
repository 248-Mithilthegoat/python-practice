birth_year = int(input("Enter your birth year: "))
birth_month = input("Enter your birth month: ").lower()
current_age = 2025 - birth_year # Creating a variable for if your birth month has passed
current_age2 = 2025 - birth_year - 1 # Creating a variable for if your birth month has not come to pass yet
year_100 = birth_year + 100 # Creating a variable to calculate the year you will turn 100
match birth_month: # Using the match function to check if you were born in a specific month and calulate the current age, approxiamte amount of days lived and the year you will turn 100
    case "january" | "1" | "jan":
        print(f"Your current age is {current_age}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
    case "february" | "2" | "feb":
        print(f"Your current age is {current_age}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
    case "march" | "3" | "mar":
        print(f"Your current age is {current_age}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
    case "april" | "4" | "apr":
        print(f"Your current age is {current_age}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
    case "may" | "5" | "may":
        print(f"Your current age is {current_age}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
    case "june" | "6" | "jun":
        print(f"Your current age is {current_age}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
    case _:
        print(f"Your current age is {current_age2}. You have lived for approximately {current_age * 365} days. You will turn 100 in the year {year_100}.")
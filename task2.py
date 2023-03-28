# program to determine which of the years entered are leap years

# input the year and number of years
year = int(input("Enter a year: "))
num_years = int(input("Enter number of years: "))

print(f"{num_years} years starting from {year}:")

# loop through the number of years
for i in range(num_years):
    current_year = year + i
    
    # check if the current year is a leap year
    if current_year % 4 == 0:
        if current_year % 100 == 0:
            if current_year % 400 == 0:
                print(f"{current_year} is a leap year")
            else:
                print(f"{current_year} isn't a leap year")
        else:
            print(f"{current_year} is a leap year")
    else:
        print(f"{current_year} isn't a leap year")
# Lesson 1.5: Age in Days Caluclator

# Ask for the user's name
name = input("What is your name?")

# Ask for the user's age in years and convert to integer
age_years = int(input("How old are you (in years)?"))

# Caluclate days alive (approximate, ingoring leap years)
days_alive = age_years * 365

# Calucalte days until 100 years old
days_until_100 = (100 - age_years) * 365

# Display results
print()
print("Hello", name + "!")
print("You have been alive for about", days_alive, "days.")
print("You have about", days_until_100, "days until you are 100 years old.")

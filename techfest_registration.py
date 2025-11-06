print("Welcome to SMIT TechFest!")
print("Event organized by [Your Full Name] of APPDAET [Your Section]")


try:
    num_participants = int(input("How many participants will register? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if num_participants <= 0:
    print("No participants to register.")
    exit()



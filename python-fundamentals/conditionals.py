# Age categorization
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


# ------------------------------------------------------------------------------------------------------------------

# Ticket discount system
Customer_age = int(input("Enter your age for ticket booking: "))
Day = input("What's the day : ").lower()

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

if Customer_age < 18:
    if Day in days:
        if Day in ["wednesday", "sunday"]:
            print("woah! You unlocked a discount of $2")
            print("Ticket Price after discount is $6")
        else:
            print("There are no Discounts")
            print("Ticket price is $8")
    else:
        print("Please enter a valid response")
else:
    if Day in days:
        if Day in ["wednesday", "sunday"]:
            print("woah! You unlocked a discount of $2")
            print("Ticket Price after discount is $10")
        else:
            print("There are no Discounts")
            print("Ticket price is $12")
    else:
        print("Please enter a valid response")

# ------------------------------------------------------------------------------------------------------------------

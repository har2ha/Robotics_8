#Day 8 Challenge 
#Today I learned how to combine all my knowledge from previous lessons 
print("Your Daily Afirmation!")
name = input("What is your name? ")
going = input(f"Hi {name}, how's it going? ")
if going == "good" or going == "Good" or going == "Good ":
    print("That's good! I'm glad you're doing well.")
else:
    print("I'm sorry to hear that. I hope your day gets better!")
 
day = input("What day of the week is it? ")
if day == "Monday" or day == "monday":
    print("Have a great Monday!")
elif day == "Tuesday" or day == "tuesday":
    print("Have a great Tuesday!")
elif day == "Wednesday" or day == "wednesday":
    print("Have a great Wednesday!")
elif day == "Thursday" or day == "thursday":
    print("Have a great Thursday!")
elif day == "Friday" or day == "friday":
    print("Have a great Friday!")
elif day == "Saturday" or day == "saturday":
    print("Have a great Saturday!")
elif day == "Sunday" or day == "sunday":
    print("Have a great Sunday!")
else:
    print("Huh? Did you misspell something?")



food = input("Tell me a food you've been craving! ")

print(f"I hope you have a great day {name}!")
print(f"Also, you should eat {food} today! You deserve it after working so hard!")
print(f"See ya tomorrow {name} for your daily affirmation!")

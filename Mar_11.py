# Day 5 challenge 
# Today I learned about the if and else statment
print("My Little Pony Generator: The Mane 6")
hat = input("Does she wear a hat?: ")
if hat == "Yes":
    print("Your pony is Applejack!")
else:
    fashion = input("Is your pony obessed with fashion? ")
    if fashion == "Yes":
        print("Your pony is Rarity!")
    else:
        hair = input("Does your pony have rainbow hair? ")
        if hair == "Yes":
            print("Your pony is Rainbow Dash!")
        else:
            mane = input("Does your pony have a pink mane? ")
            if mane == "Yes":
                print("Your pony is Fluttershy!")
            else:
                ener = input("Is your pony very energetic? ")
                if ener == "Yes":
                    print("Your pony is Pinkie Pie!")
                else:
                    main = input("Is your pony the main character of MLP? ")
                    if main == "Yes":
                        print("Your pony is Twilight Sparkle!")
                    else:
                        print("Your pony isn't in the Mane 6! Try Again!")

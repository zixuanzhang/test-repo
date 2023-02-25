# More if statements puzzles

# Ex1
if x < 2:
    print("Below 2")
elif x >= 2:
    print("Two or more")
else:
    print("Something else")  # this will never be evalauted

# Ex2
if x < 2:
    print()
elif x < 20:  # x > 2 and < 20
    print()
elif x < 10:  # x > 2 and x >= 20, and x < 10
    print()  # this will never be executed
else:
    print()

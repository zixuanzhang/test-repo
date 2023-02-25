# Chapter 3 Exercise

# Exercise 1&2
##hours = input('Enter Hours: ')
##rate = input('Enter Rate: ')
##
##try:
##    hours = float(hours)
##    rate = float(rate)
##    if hours > 40:
##        salary = 40 * rate + (hours-40) * 1.5 * rate
##    elif 0 < hours and hours <= 40:
##        salary = hours * rate
##    print('Pay: ', salary)
##except:
##    print('Error, please enter numeric input.')

# Exercise 3
score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Please enter numeric score")

if 0 <= score and score <= 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

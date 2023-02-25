## Chapter 5 exercise

### exercise 1
##total = 0
##count = 0
##while True:
##    line = input('Enter a number: ')
##    try:
##        total = total + float(line)
##        count = count + 1
##        average = total/count
##    except:
##        if line == 'done':
##            print(total, count, average)
##            break
##        else:
##            print('Invalid input')
##            continue

## Answer from instructor
##count = 0
##tot = 0
##while True:
##    sval = input('Enter a number: ')
##    if sval == 'done':
##        break
##    try:
##        fval = float(sval)
##    except:
##        print('Invalid input')
##    count = count + 1
##    tot = tot + fval
##print(tot, count, tot/num)


# Exercise 2
largest = None  # or set to a negative number
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    if largest is None or fval > largest:
        largest = fval
    if smallest is None or fval < smallest:
        smallest = fval
print(smallest, largest)

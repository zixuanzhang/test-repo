## Chapter 6 exercise

# print string backwards
fruit = "banana"
index = -1
while index >= (-len(fruit)):
    print(fruit[index])
    index = index - 1

# a function to count specified letter
def count(input_str, target):
    count = 0
    for char in input_str:
        if char == target:
            count = count + 1
    print(count)


# count('banana', 'a')

# compare Strings
def compstr(query, subject):
    if query < subject:
        print("Your word, " + query + ", comes before", subject)
    elif query > subject:
        print("Your word, " + query + ", comes after", subject)
    else:  # word == subject
        print("All right,", subject)


# compstr('bb', 'banana')

# exercise
str = "X-DSPAM-Confidence:0.8475"
colpos = str.find(":")
num = float(str[colpos + 1 :])
print(num)

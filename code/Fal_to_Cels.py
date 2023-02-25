# convert Fahreheit temp to Celsius

inp = input("Enter Fahrenheit Temperature: ")
try:
    fahr = float(inp)
except:  # catching an exception and print an error message
    print("Please enter a number")

cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

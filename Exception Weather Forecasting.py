#Exception Weather Forecasting

#Task 1  -Start

user_input = input("Please enter the temperature in Fahrenheit: ")

try:
    temperature = float(user_input)
    
except ValueError as e:
    print(e)
    
except NameError as e:
    print(e)

else:
    celsius = temperature - (32 * 5/9)
finally:
    print(f"{temperature} degrees Fahrenheit is {celsius: .2f} degrees Celsius")
print("Thank you for using the Weather Tracker Application.")

x = input("If temperature in Fahrentin(°F) input'F' and if in Kelvin(°K) input 'K': ").lower()
degree = int(input("Temperature is what: "))
celsius_inF = degree * (100/212)
celsius_inK = degree - 273.15

if x =='f':
    print(f"The temperature of {degree}°F is equivalent to {celsius_inF}°C")
elif x == 'k':
    print(f"The temperature of {degree}°K is equivalent to {celsius_inK}°C ")
    
# Tried the code below but there was a semantic error 😳

'''print(f"The temperature of {degree}°F is equivalent to {celsius_inF}°C") if x == "f" else print(f"The temperature of {degree}°K is equivalent to {celsius_inK}°C ")'''

"""Thw error is that I could not add the condition if x == "k" because I couldn't add anything after the 'else' sstatement. So any other thing the user inputs
other than f is going to run """

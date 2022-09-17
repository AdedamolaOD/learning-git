
x = input("If temperature in Fahrentin(°F) input'F' and if in Kelvin(°K) input 'K': ").lower()
degree = int(input("Temperature is what: "))
celsius_inF = degree * (100/212)
celsius_inK = degree - 273.15

if x =='f':
    print(f"The temperature of {degree}°F is equivalent to {celsius_inF}°C")
elif x == 'k':
    print(f"The temperature of {degree}°K is equivalent to {celsius_inK}°C ")
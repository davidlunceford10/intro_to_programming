temperature = float(input("What is the temperature? "))
fahrenheit_or_celsius = input("Fahrenheit or Celsius (F/C)? ").upper()

if fahrenheit_or_celsius == 'C':
    temperature = (temperature * (9/5) + 32)
else:
    temperature

for V in range(5, 61, 5):
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (V ** 0.16)) + (0.4275 * temperature * (V ** 0.16))
    print(f'At temperature {temperature}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F')

def convertCelsiusToFahrenheit(celsiusTemperature):
    return (celsiusTemperature * 9/5) + 32

temperatureCelsius = float(input("Enter temperature in Celsius: "))
temperatureFahrenheit = convertCelsiusToFahrenheit(temperatureCelsius)
print(f"Temperature in Fahrenheit: {temperatureFahrenheit:.2f}")


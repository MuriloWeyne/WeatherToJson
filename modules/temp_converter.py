def kelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    return '{celsius:.2f}'.format(celsius=celsius)

def kelvinToFahrenheit(kelvin):
    kelvin = (kelvin-273.15)*(9/5)+32
    return '{kelvin:.2f}'.format(kelvin=kelvin)

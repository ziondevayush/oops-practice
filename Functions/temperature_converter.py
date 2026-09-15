def temp_convert(celcius):
        farenheit = (celcius*9/5)+32
        return farenheit
degree = int(input("Enter Degree in Celcius: "))
result = temp_convert(degree)
print(result)
def even_odd(num):
    if num % 2 == 0:
        return True
    else: 
        return False

number = int(input("Enter any Number: "))
result = even_odd(number)
print(result)
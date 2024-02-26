#Desarrolla una función  NO recursiva que sume todos los dígitos
#de un número entero

def sum_digits(number):
    total_sum = 0
    
    # Convert the number to a string to iterate over its digits
    for digit in str(number):
        # Convert each digit back to an integer and add it to the total sum
        total_sum += int(digit)
    
    return total_sum

number = 12345
result = sum_digits(number)
print(f"La suma de los dígitos de {number} es: {result}")

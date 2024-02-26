#Desarrolla una función  NO recursiva que sume todos los dígitos
#de un número entero

def sum_digits(number):
    total_sum = 0 # O(1) # O(1)
    
    # Convert the number to a string to iterate over its digits
    for digit in str(number): # O(n)
        # Convert each digit back to an integer and add it to the total sum
        total_sum += int(digit) # O(1)
    
    return total_sum # O(1)

number = 12345 # O(1) # O(1)
result = sum_digits(number) 
print(f"La suma de los dígitos de {number} es: {result}") # O(1)

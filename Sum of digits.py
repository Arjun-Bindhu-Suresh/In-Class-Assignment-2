def sum_of_digits(number):
    """Returns the sum of the digits of the given integer."""
    total = 0
    number_str = str(abs(number))  
    
    for digit in number_str:  
        total += int(digit)  
    
    return total

def get_number(prompt):
    """Asks the user for a valid integer and returns it."""
    while True:
        user_input = input(prompt)  
        # Check if it's a valid integer
        if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
            return int(user_input) 
        else:
            print("Invalid input. Please enter a valid integer.") 

if __name__ == "__main__":
    # Get two integers from the user
    first_number = get_number("Enter the first integer: ")  
    second_number = get_number("Enter the second integer: ")  
    
    # Calculate the total sum of both numbers
    total_sum = first_number + second_number  
    
    # Calculate the sum of digits for both numbers
    first_sum_of_digits = sum_of_digits(first_number)  
    second_sum_of_digits = sum_of_digits(second_number)  
    
    # Print the results
    print("The sum of the digits in the first number is:", first_sum_of_digits)
    print("The sum of the digits in the second number is:", second_sum_of_digits)
    print("The total sum of the two numbers is:", total_sum)
   
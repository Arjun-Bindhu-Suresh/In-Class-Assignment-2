def is_positive(number):
    return number > 0
def get_number():
    while True:
        user_input = input("Enter a number: ")
        try:
            return float(user_input)  
        except ValueError:
            print("Invalid input. Please enter a valid number.")  

if __name__ == "__main__":
    number = get_number() 
    if is_positive(number):
        print("The number is positive.")
    else:
        print("The number is not positive.")

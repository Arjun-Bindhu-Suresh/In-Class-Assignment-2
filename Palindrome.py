def is_palindrome(s):
    
    # This will hold the cleaned version of the input string
    word = ""

    # Loop through each character in the input string
    for char in s:
        # Check if the character is a letter or a number
        if char.isalnum():
            # Convert the character to lowercase and add it to word
            word += char.lower()

    # Compare the cleaned string to its reverse
    return word == word[::-1]

def get_input(prompt):
    #Ask the user for input and return it.
    return input(prompt)

if __name__ == "__main__":
    user_input = get_input("Give an input to check if it's a palindrome or not: ")
    
    if is_palindrome(user_input):
        print(f"The input '{user_input}' you entered is a palindrome.")
    else:
        print(f"The input '{user_input}' you entered is not a palindrome.")

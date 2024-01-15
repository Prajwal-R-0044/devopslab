def is_palindrome(input_str):
    # Convert the string to lowercase and remove spaces
    cleaned_str = ''.join(input_str.lower().split())

    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Get user input
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
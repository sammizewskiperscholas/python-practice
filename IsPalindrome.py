#Ispalindrome- Given a string, write a python function to check if it is palindrome or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.
def is_palindrome(input_string):
    new_string = input_string.lower().replace(' ', '')
    reverse_string = new_string[::-1]
    print(new_string)
    print(reverse_string)
    if new_string == reverse_string:
        return True
    return False
   
   

print(is_palindrome("Never Odd Or Even"))

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def palindromchk(str1):
    revstr1 = ""
    for i in str1:
        revstr1 = i + revstr1
    if (str1 == revstr1):
        return 'Yes'
    else:
        return 'No' 

chk1 = print(palindromchk('12321'))      


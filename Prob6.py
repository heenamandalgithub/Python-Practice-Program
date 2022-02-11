#Write a function that test whether a string is a palindrome
def test():
    a = str(input("Enter a String=\n "))
    if a[::-1] == a:
        print("String is palindrome")
    else:
        print("String is not palindrome")


test()

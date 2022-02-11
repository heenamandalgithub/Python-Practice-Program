#Write a program to print cube of numbers
a = int(input("Enter Lower Limit:"))
b = int(input("Enter Upper Limit:"))
for i in range(a, b + 1):
    print(i, ":", i ** 3)

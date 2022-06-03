a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
a = a ^ b
b = a ^ b
a = a ^ b

print("Value of 1st no.:", a)
print("Value of 2nd no.:", b)
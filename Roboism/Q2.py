print("Enter ur credit card no.: ")
c = input()
l=len(c)
if l==15:
    for i in range (0,l-4):
    print("*" , end="")
print(c[-4:] , end="")
else:
print("Error")

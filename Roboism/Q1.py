list = []
n = int(input("Enter no. of elements in list:"))
for i in range(0,n):
    a = int(input("Enter value: "))
    list.append(a)
print(list)
print("How do u want to sort?")
b = input()
if b == "asc":
    list.sort()
    print(list)
if b == "desc":
    list.sort(reverse=True)
    print(list)
if b == "none":
    print(list)


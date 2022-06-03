dict = {}
list = []
n = int(input("How many elements?"))
for j in range(0,n):
    a = int(input("Enter value: "))
    list.append(a)
list1 = []
for i in range(0,n):
    b = list.count(list[i])
    list1.append(b)
key = str(list)
value = str(list1)
dict[key] = [value]
print("The highest frequency is: " , max(list1))
position = list1.index(max(list1))
print("The highest frequency element is: " , list[position])
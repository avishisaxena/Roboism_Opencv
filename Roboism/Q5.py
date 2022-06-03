list = []
for i in range(0,100):
    a = int(input("Enter value: "))
    list.append(a)
list1 = []
for j in range(0,100):
    if list[j] in list1:
        print(list[j],"is duplicate")
        break
    else:
        list1.append(list[j])
print("Enter from: ")
a = int(input())
print("Enter to: ")
b = int(input())
for i in range(a,b):
    if i>1:
        for j in range(2,i-1):
            if i % j == 0:
                break
        else:
            print(i)


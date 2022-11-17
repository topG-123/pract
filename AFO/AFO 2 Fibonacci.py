a = int(input("enter len of fibonacci series: "))
myArray = []
n1 = 0
n2 = 1
n3 = 1
myArray.append(n1)
myArray.append(n2)
myArray.append(n3)
for i in range(0, (a - 3)):
    num4 = (myArray[i+1] + myArray[i+2])
    myArray.append(num4)
print(myArray)
b = int(input("enter element to find: "))
for i in range(0, len(myArray)):
    if (myArray[i] == b):
        print("number present in fibonacci series at index:", i+1)
    else:
        print("")

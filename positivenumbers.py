l = []
l2 = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    num = int(input("Enter the element %d: "%(i+1)))
    l.append(num)

for i in range(0,n):
    if l[i] > 0:
        l2.append(l[i])
print("The original list is:")
print(l)
print("The list with positive numbers is:")
print(l2)
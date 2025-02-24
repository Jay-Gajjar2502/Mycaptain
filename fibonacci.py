n = int(input("Enter the number of terms: "))

fib = [0, 1]
for i in range(2, n):
    sum = fib[-1] + fib[-2]
    fib.append(sum)

print("Fibonacci Series: ",fib)


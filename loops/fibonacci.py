#Fibonacci series using loops
def fibonacci(n):
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = int(input("Enter the number of terms in the Fibonacci series: "))
fib_series = fibonacci(n)
print("Fibonacci series:", fib_series)

# Week 3 Assignment - Fibonacci Series

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(terms)
    print("Fibonacci Series:")
    print(" ".join(str(x) for x in result))

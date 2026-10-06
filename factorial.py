# Student Name : ASWIN D
# Register No  : 111924CB01301
# Department   : B.E. Computer Science and Engineering (Cybersecurity)
# Week 2       : Factorial of a Number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        print(f"Factorial of {num} = {factorial(num)}")

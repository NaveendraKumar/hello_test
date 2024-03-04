def fact(n):
    if n==0:
       return 1
   else:
       return n * fact(n-1)
       
number = 5
result = fact(number)
print(f"The factorial of {number} is {result}.")

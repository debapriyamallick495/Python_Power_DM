# #declaring an using function
def greet (name):
    return "Hello, "+ name + "!"
user_name = input("Enter your name : ")
print(greet(user_name))

#factorial calculation using recursion
def factorial (n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial (n-1)
    
num = int (input("Enter a positive number:"))  

if num < 0: 
    print("factorial of negative number not possible")

else :
    print(f"the factorial of {num} is {factorial(num)}")

#generate fibonacci sequence using function
prime number 


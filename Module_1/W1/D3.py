# # #declaring an using function
# def greet (name):
#     return "Hello, "+ name + "!"
# user_name = input("Enter your name : ")
# print(greet(user_name))

# #factorial calculation using recursion
# def factorial (n):
#     if n == 0 or n == 1:
#         return 1 
#     else:
#         return n * factorial (n-1)
    
# num = int (input("Enter a positive number:"))  

# if num < 0: 
#     print("factorial of negative number not possible")

# else :
#     print(f"the factorial of {num} is {factorial(num)}")

#generate fibonacci sequence using function
# def fibonacci():
#     term = int(input("Enter the number of terms: "))
#     a = 0
#     b = 1
#     i = 0  
#     print("Fibonacci Series:")
#     while i < term:
#         print(a)
#         a, b = b, a + b
#         i += 1
# fibonacci()

#prime number 
def prime(n):
    flag = 0
    for i in range(2,int(n/2)):
         if (n % i == 0):
           flag = 1
    return flag

num = int(input("Enter a positive num:"))
flag = prime (num)
if (flag == 0):
    print("prime")     
else:
    print("not prime")

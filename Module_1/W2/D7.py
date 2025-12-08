#error handling in file operation
#1. fileNotFoundErrot
#2.Permissionerror
#3.IsADirectoryError
#4.IOError

#basic tr_except block
# try:
#     file = open("nonexistance.txt",'r')
#     content = file.read()
#     file.close()
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("no permission to read")
# except Exception as e:
#     print(f"an enexpected error occured:{e}")

#complete try except else finally

# try:
#     file = open ('data.txt','r')
#     content = file.read()
# except FileExistsError:
#     print("File not found, creating a new file...")
#     file = open('data.txt','w')
#     file.write("Default content")
#     content ="hdcfiuerhfiehdiuoidjwudyufgd"
# except IOError as e:
#     print(f"Input/Output error: {e}")
# else:
#     print("file read successfully")
#     print(f"file content length : {len(content)}")
# finally:
#     if 'file' in locals() and not file.closed:
#         file.close()
#     print("Cleanup completed....")

#using with statement with error handling
try:
    with open('data.txt','r') as file:
        content = file.read()
        result = 10/0
except FileNotFoundError:
    print("File not found.")
except ZeroDivisionError:
    print("math error occured.")
except Exception as e:
    print(f"Unexcepted error.")
else:
    print("operation successful.")
    
#advanced data structures
# list
# creating a list that holds different types of data
my_list =[20, 'Python Power', 35.75,[20,40,60]]
print (my_list)

# traversing through the elements of the LIST
for i in range(0, len(my_list)):
    print(my_list)

# test mautable property by updating a value
my_list[2] =99.99
print(my_list)

# extend the list 
my_list.extend ([12,33,45])
print("extended list",my_list)

# sorting the list in ascending order
num_list = [20,44,66, 98, 54, 35, 31, 8, 17]
print ("Given List: ", num_list)
num_list.sort ()
print("Sorted List",num_list)

#reverse a list
num_list. reverse ()
print("reversed list",num_list)




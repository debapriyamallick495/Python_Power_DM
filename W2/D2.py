#python tuples 
T = (20, 'Python Power', 35.75,[20,40,60])
print("original tuple",T)

#traversing through tuple element
for i in range(0, len(T)):
    print(T)

#slicing in tuple
#syntax: tuple[start:end]
tup = ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango", "Pineapple")
print("given tuples",tup)

print("Sliced Tuple: ", tup[1:4])  
print("Sliced Tuple from index 2 to end: ", tup[2:])      
print("Sliced Tuple from start to index 3: ", tup[:3])
print("Sliced Tuple with negative indices: ", tup[-4:-1])  
print("Sliced Tuple with step: ", tup[::2])  
print("Sliced Tuple with reverse: ", tup[::-1])  
print("Sliced Tuple with start, end and step: ", tup[1:5:2])

#max and min function in tuple
t2= (34,56,89,76,34,34)
print("max",max(t2))
print("min",min(t2))
print("occurence of 34: ",t2.count(34))




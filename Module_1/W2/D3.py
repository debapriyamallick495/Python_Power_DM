#python dictionaries
Dict = {
    1:'Learn',
    2:'Python',
    3:'Debapriya',
    4:'Neha',
    5:'Tripan',
}
print("dict:",Dict)

Dict2 = {'Name': 'Alice', 
         'Age': 30, 
         'City': 'New York', 
         'Skills': ['Python', 'Data Analysis', 'Machine Learning']}
print("dict2", Dict2)

# accessing disctionary items using key
print("Name: ",Dict2['Name'])
print("Age: ", Dict2['Age'])

# accessing dictionary items using get function
print("City : ",Dict2.get("City"))
print("Skills : ",Dict2.get("Skills"))

#adding an item to the dictionary
Dict2["Country"]= "INDIA"
print("modified dictionary",Dict2)

#deleting an item
del Dict2 ["Skills"]
print("updated dictionary",Dict2)

#itarating through a dictionary
for key in Dict2:
    print(key, " : ", Dict2[key])   




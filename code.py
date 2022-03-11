Tusers = int(input("Enter number of users : "))
dict1 = {}
list1 = []

for i in range(Tusers):
    name = input("Enter user name : ")
    age  = int(input("Enter user age : "))
    dict1 = {"name":name ,
             "age":age}
    list1.append(dict1)
    
search = input("Enter name to search : ")
 
Uage = 0
for i in list1:
    
    if i["name"] == search :
        Uage = i["age"]
        
        
if Uage != 0 :
  print(Uage)        

else :
    print("There is no user with given name!")
a= [1,3,5,7,4]
#length
print (" length of a is :", len(a), type(a))
#access
print ("a[-2] is", a[-2], "and a[2] is" , a[2])
#change
a[-3]=50
print ("number at a[-5] is' , a[-3]")
print (a)
#slicing
print (a [2:4])
print (a [:-3])
print (a [-4:-1])
a.append (100)
a.insert (2, 200)
a.pop()
del a[1]
print (" after task 5 :", a)
a= a+ [2, 4, 6]
print ("after task 6: ", a)
b = a
b.sort()
print (b)
for i in b:
    if (i == 7):
        break
    else :
      print (i, end = ' ') 
print ()

print(a)
a.clear()
print(a)


#tuple
x= (1,3,5,7,4)
#length
print (" length of a is :", len(x), type(x))
a = list(x)
#access
print ("a[-2] is", a[-2], "and a[2] is" , a[2])
#change
a[-3]=50
print ("number at a[-5] is' , a[-3]")
print (a)
#slicing
print (a [2:4])
print (a [:-3])
print (a [-4:-1])
a.append (100)
a.insert (2, 200)
a.pop()
a.pop(1)
# del a[1]
print (" after task 5 :", a)
a.extend([2, 4, 6])
# a= a+ [2, 4, 6]
print ("after task 6: ", a)
b = a
b.sort()
print (b)
for i in b:
    if (i == 7):
        break
    else :
      print (i, end = ' ') 
print ()

print(a)
a.clear()
print(a)

print()
x = tuple (a)
print(a)

#set
a = {1,3,5, 8, 3, 7}
b = {0 , False, 1,5 }
# lenfth and #Type
print (len(a), type(a))
#add 10 #remove 8
a.add(10)
a.remove(8)
print(a)
#union #intersection #difference a,b
c= a|b
print ("union of a,b:", c)
c = a & b
print (" intersection of a & b:", c)
c = a-b
print (" difference of a & b:", c)
#loop
for i in a:
    if i== 5:
        break
    else:
        print(i, end='')
print()
x= [2,3,4]
x = set(x)
a = a.union(x)
print(a)

#Dictionary
Employee = { 
    "name" : "A",
    "age" : 40,
    "type" : {"developer" : ["iOS" , "android"]},
    "permanent" : True,
    "salary" : 30000,
    100 : (1, 2, 3),
    4.5 : {5,6, True,7,1}
}
print (Employee)
#1
print (len(Employee), type(Employee))
#2
print(Employee ["type"]["developer"][0])
#print(Employee ["type"]["developer"][0])
#3
Employee["permanent"]= False
#4
Employee["gender"] = "male"
#5
del Employee ["age"]
#6
for i in Employee.keys():
    print(i, end=" ")
print()
for i in Employee.values():
    print(i, end=' ')
print()
for x, y in Employee.items():
    print(x,y)



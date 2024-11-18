#1
class InvalidAgeException(Exception):
    pass

try:
    age = int(input())
    if (age<18):
        raise InvalidAgeException
    print("Age: ",age)
except InvalidAgeException:
    print("Invalid Age Exception Occured")
except:
    print("Other Exception Occured")
finally:
    print("Done")


2
class SalarynotInRangeException(Exception):
    pass
salary = [15000,20000,10000,5000]
try:
    for i in salary:
        if (i < 1000 or i>20000):
            raise SalarynotInRangeException
        print("Salary:", i)
except SalarynotInRangeException:
    print("Salary not In Range Exception Occured")
except:
    print("Other error occured")
finally:
    print("Done!")


3
class Vehicle:
    def __init__(self,color):
        self.color = color

class Taxi(Vehicle):
    def __init__(self,color):
        super().__init__(color)
        self.__capacity = 0
        self.__model = ""
        self.__variant = ""

    def setModel(self,model):
        self.__model = model

    def setCapacity(self,capacity):
        self.__capacity = capacity

    def setVariant(self, variant):
        self.__variant = variant

    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

ob = Taxi("Black")
ob.setModel("Rafi")
ob.setVariant("Chocolate")
ob.setCapacity(89789)

print(ob.getCapacity())
print(ob.getCapacity)



import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

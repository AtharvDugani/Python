# In Python OOPs, Getter and Setter methods are used to access and modify the private or protected data members of a class.

class student:
    def __init__(self,name):
        self.__name = name # here __name is the private variable

    def get_data(self): # it is the getter function used to get the private data
        return f"Hello {self.__name}" 
    
    def set_data(self, name): # it is the setter function used to set the data in private vairbale
        self.__name = name

s1 = student("Atharv")
print(s1.get_data())

s1.set_data("Akshay")
print(s1.get_data())


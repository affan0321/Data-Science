# class Factory :
#     def __init__(self,material,zip,pockets):
#         self.material = material
#         self.zip = zip
#         self.pockets = pockets

#     def Show(self):
#         print(f"There are {self.material} materials , {self.zip} zips and {self.pockets} pockets.")

# reebok = Factory("Leather",3,3)
# campus = Factory("nylon",4,2)

# reebok.Show()
            
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def Show(self):
#         print(f"Your name is {self.name}")

# class Lion(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def Show(self):
#         print(f"Your name is {self.name} and your age is {self.age}")    
        

# lion1 = Lion("Lion",21)
# animal1 = Animal("Tiger")

# lion1.Show()
# animal1.Show()        



class Demo:
    def __init__(self):
        self.name = "Public Member"
        self._age = 21
        self.__salary = 50000

    def show(self):
        print("Inside the class : ")
        print("Public : ",self.name)
        print("Protected : ",self._age)
        print("Private : ", self.__salary)

obj = Demo()
obj.show()            
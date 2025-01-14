# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         print(f"Vehicle Brand: {self.brand}")
#         print(f"Vehicle Model: {self.model}")

#     def move(self):
#         print("The vehicle is moving.")

# class Car(Vehicle):
#     def __init__(self, brand, model, car_type):
#         super().__init__(brand, model)
#         self.car_type = car_type

#     def move(self):
#         print(f"The {self.car_type} car is driving.")

#     def show_car_type(self):
#         print(f"This car is a {self.car_type}.")

# my_car = Car("Toyota", "Corolla", "Sedan")

# my_car.show_info()      
# my_car.move()          
# my_car.show_car_type() 



# ---------------------------------


# class c1:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
#   def show(self):
#     print(f"Name:{self.name} Age:{self.age}")
    
#   def title():
#     print("hello")
    

# class c2(c1):
#   def __init__(self,name,age,add):
#     super().__init__(name,age)
#     self.add = add 
    
#   def fullinfo(self):
#     print(f"Address:{self.add}")
  
#   def show_add(self):
#     print(f"Address:{self.add}")

# obj1 = c2("Mohan",20,"Delhi")
# obj1.show_add()
# obj1.show()

# single

# class c1:
#     def fun1(self):
#         print("fdsfsd")

# class c2(c1):
#     pass

# c2obj = c2()

# c2obj.fun1()

# multiple
# class c1:
#     def fun1(self):
#         print("Class1")

# class c2:
#     def fun2(self):
#         print("class2")

# class c3(c1,c2):
#     pass

# c3Obj = c3()
# c3Obj.fun1()
# c3Obj.fun2()


# multileve

# class c1:
#     def fun1(self):
#         print("clss1")
# class c2(c1):
#     def fun2(self):
#         print("Clss2")
# class c3(c2):
#     pass
# c3Obj = c3()
# c3Obj.fun1()
# c3Obj.fun2()

# heirerical

# class c1:
#     def fun1(self):
#         print("class1")
# class c2(c1):
#     def fun2(self):
#         print("class2")
# class c3():
#     pass
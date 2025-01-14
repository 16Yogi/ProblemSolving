class c1:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
    
  def show(self):
    print(f"Name:{self.name} Age:{self.age}")
    

class c2:
  def __init__(self,add):
    self.add = add
    
  def show(self):
    print(f"Address: {self.add}")
    
obj1 = c2("HP")
obj1.show()

# --------------------------------


class c1:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
    print("class1 1")
    
  def show(self):
    print("class1 ")
    print(f"Name:{self.name} Age:{self.age}")
    

class c2(c1):
  def __init__(self,name,age,add):
    super().__init__(name,age)
    self.add = add
    print("class2 1")
    
  def show(self):
    print("class2")
    print(f"Address: {self.add}")
    
obj1 = c2("Mehek",30,"Himachal")
obj1.show()


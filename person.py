class Person: 
  # Instances Attribute 
  def __init__(self, name: str, age: int, gender: str, address: str) -> None:
    self.name = name 
    self.age = age 
    self.gender = gender 
    self.address = address 

  def __str__(self) -> str: # Represent a Person 
    return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}'
  

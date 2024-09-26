import sys 

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from person import Person

class Test_Person: 
  def setup_method(self, method): # Setup method run at begging of every single test
    print(f'Running method {method}')
    self.person1 = Person('Tim', 26, 'Male', '123 st')

  def test_person(self): 
    assert self.person1.name == 'Tim'
    assert self.person1.age == 26
    assert self.person1.gender == 'Male'
    assert self.person1.address == '123 st'
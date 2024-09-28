import sys 
from datetime import datetime

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from patient import Patient
from bill import Bill 


class Test_Bill: 
  def setup_method(self, method): # setup method run at the beginning of each test
    print(f'Running method {method}')
    self.patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")
    self.bill = Bill(1, self.patient_1, 'Heart Surgery', 5000)

  def test_bill(self):
    # Check Bill for patient_1 
    assert self.bill.patient == self.patient_1
    # Check service 
    assert self.bill.services == 'Heart Surgery'
    # Check add payment function 
      # Total amount is 5000 . Pay first 1000 then still pending 4000 
    assert self.bill.add_payment(1000) == 'Pending'
      # Total amount is 4000 . Pay all 4000 
    assert self.bill.add_payment(4000) == 'Paid'

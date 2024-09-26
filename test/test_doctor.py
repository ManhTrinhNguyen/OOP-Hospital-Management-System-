import sys 

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from doctor import Doctor 
from patient import Patient

class Test_Doctor: 
  def setup_method(self, method): # Setup method run at every test 
    print(f'Running method {method}')
    self.doctor_1 = Doctor(doctor_id=101, name="Dr. Smith", age=45, gender="Male", address="123 Medical St", specialization="Cardiology")
    self.patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")

  def test_doctor(self):
    # Doctor name 
    assert self.doctor_1.name == 'Dr. Smith'

    # Doctor id  
    assert self.doctor_1.doctor_id == 101 

    # Add patient 
    assert self.doctor_1.add_patient(self.patient_1) == f'Added patient {self.patient_1} to Doctor list'
    assert len(self.doctor_1.patients) == 1
    assert self.doctor_1.patients[0] == self.patient_1

    # Remove patient 
    assert self.doctor_1.remove_patient(self.patient_1) == f'Removed {self.patient_1} from the Doctor list'
    assert len(self.doctor_1.patients) == 0
    

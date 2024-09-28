import sys 
from datetime import datetime

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from patient import Patient
from doctor import Doctor
from medical_record import Medical_Record

class Test_Medical_Record: 
  def setup_method(self, method): # Setup method run at the beggining of every test
    print(f'Running method {method}') 
    self.doctor_1 = Doctor(doctor_id=101, name="Dr. Smith", age=45, gender="Male", address="123 Medical St", specialization="Cardiology")
    self.patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")
    self.record_1 = Medical_Record(record_id=1, patient=self.patient_1, doctor=self.doctor_1, diagnosis="Heart Disease", treatment="Surgery", date=datetime.now())

  def test_medical_record(self):
    # Record for patient_1
    assert self.record_1.patient == self.patient_1
    # Record for doctor_1 
    assert self.record_1.doctor == self.doctor_1
    # Diagnosis is heart disease 
    assert self.record_1.diagnosis == 'Heart Disease'
    # Treatment 
    assert self.record_1.treatment == 'Surgery'
    # Test __str__ function 
    assert self.record_1.__str__() == f'Record {self.record_1.record_id}: {self.record_1.diagnosis} by Dr. {self.record_1.doctor.name} on {self.record_1.date}. Treatment: {self.record_1.treatment}'



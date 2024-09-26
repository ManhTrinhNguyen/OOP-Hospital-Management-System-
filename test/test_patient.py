import sys 
from datetime import datetime

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from patient import Patient
from doctor import Doctor
from appointment import Appointment
from medical_record import Medical_Record
from bill import Bill

class Test_Patient: 
  def setup_method(self, method): # Setup method run at the beggining of every test
    print(f'Running Method {method}')
    self.doctor_1 = Doctor(doctor_id=101, name="Dr. Smith", age=45, gender="Male", address="123 Medical St", specialization="Cardiology")
    self.patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")
    self.appointment_1 = Appointment(appointment_id=1, patient=self.patient_1, doctor=self.doctor_1, date=datetime.now())
    self.record_1 = Medical_Record(record_id=1, patient=self.patient_1, doctor=self.doctor_1, diagnosis="Heart Disease", treatment="Surgery", date=datetime.now())
    self.bill_1 =  Bill(1, self.patient_1, 'Heart Surgery', 5000)

  def test_patient(self):
    # Patient name
    assert self.patient_1.name == 'Alice'

    # Patient id 
    assert self.patient_1.patient_id == 201

    # Assign doctor 
    assert self.patient_1.assign_doctor(self.doctor_1) == f'Assigned doctor: {self.doctor_1}'
    assert self.patient_1.assigned_doctor == self.doctor_1

    # Add appointment 
    assert self.patient_1.add_appointment(self.appointment_1) == f'You have this appointment {self.appointment_1} coming up'
    assert len(self.patient_1.appointments) == 1
    # Appointment already added 
    assert self.patient_1.add_appointment(self.appointment_1) == f'This appointment {self.appointment_1} is already on your List'

    # Add medical record 
    assert self.patient_1.add_medical_record(self.record_1) == f'Add the record: {self.record_1} to the medical history'
    assert len(self.patient_1.medical_history) == 1

    # Add bill 
    self.patient_1.add_bill(self.bill_1)
    assert len(self.patient_1.bills) == 1
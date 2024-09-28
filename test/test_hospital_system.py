import sys 
from datetime import datetime

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from patient import Patient 
from doctor import Doctor 
from medical_record import Medical_Record 
from administrator import Administrator
from bill import Bill
from appointment import Appointment
from hospital_system import Hospital_System

class Test_Hospital_System:
  def setup_method(self, method): # Setup method run at beginning of each test
    print(f'Running method {method}')
    self.hospital = Hospital_System()
    self.admin = Administrator(admin_id=1, name="Admin John")
    self.doctor_1 = Doctor(doctor_id=101, name="Dr. Smith", age=45, gender="Male", address="123 Medical St", specialization="Cardiology")
    self.patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")
    self.record_1 = Medical_Record(record_id=1, patient=self.patient_1, doctor=self.doctor_1, diagnosis="Heart Disease", treatment="Surgery", date=datetime.now())
    self.appointment_1 = Appointment(appointment_id=1, patient=self.patient_1, doctor=self.doctor_1, date=datetime.now())

  def test_hospital_system(self):
    # register_doctor function 
    assert self.hospital.register_doctor(self.doctor_1) == f'Doctor: {self.doctor_1} has registered'

    # Check that doctor_1 exist in the hospital_system doctor list 
    assert self.hospital.doctors[0] == self.doctor_1
    
    # Register Patient 
    assert self.hospital.register_patient(self.patient_1) == f'Patient {self.patient_1} has registered'

    # Check if paiten_1 exist in the hospital_system patient list 
    assert self.hospital.patients[0] == self.patient_1

    # Schedule Appointment 
    assert self.hospital.schedule_appointment(self.appointment_1) == 'Scheduled new appointment and added to the appointment list'

    # Check if appointment_1 in the hospital_system appointment list
    assert self.hospital.appointments[0] == self.appointment_1

    # Create Bill to check generate_bill function 
    bill = Bill(len(self.hospital.bills) + 1, self.patient_1, 'Heart Surgery', 5000)
    assert self.hospital.generate_bill(self.patient_1, 'Heart Surgery', 5000) == f'Generated new bill {bill}'

    # Find doctor base on doctor id 
    assert self.hospital.find_doctor(self.doctor_1.doctor_id) == self.doctor_1
    ## Doctor not exist 
    assert self.hospital.find_doctor(102) == 'Doctor id not exist'

    # Find patient base on patient id 
    assert self.hospital.find_patient(self.patient_1.patient_id) == self.patient_1
    ## Patient not exist 
    assert self.hospital.find_patient(202) == 'Patient id not exist'


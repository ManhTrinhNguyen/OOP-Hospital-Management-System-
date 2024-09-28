import sys 
from datetime import datetime

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP-Hospital-Management-System-')

from appointment import Appointment
from doctor import Doctor 
from patient import Patient

class Test_Appointment:
  def setup_method(self, method): # Setup method run at the beggining of every test
    print(f'Running method {method}') 
    self.doctor_1 = Doctor(doctor_id=101, name="Dr. Smith", age=45, gender="Male", address="123 Medical St", specialization="Cardiology")
    self.patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")
    self.appointment_1 = Appointment(appointment_id=1, patient=self.patient_1, doctor=self.doctor_1, date=datetime.now())
    
  def test_appointment(self):
    # Create Appointment for patient 1 
    assert self.appointment_1.patient == self.patient_1
    # Assign doctor 1 
    assert self.appointment_1.doctor == self.doctor_1 
    # Check complete appointment 
    assert self.appointment_1.complete_appointment() == 'Completed Appointment'
    # Check if appointment.status == completed 
    assert self.appointment_1.complete_appointment() == f'Cannot not Complete this appointment because this appointment {self.appointment_1.status}'
    # Cancel Appointment 
    self.appointment_1.status = 'Scheduled' # Set status back to scheduled to check cancel_appointment
    assert self.appointment_1.cancel_appointment() == 'Canceled the Appointment'
    # Check if the appointment already canceled
    assert self.appointment_1.cancel_appointment() == f'Cannot not Cancel this appointment because this appointment {self.appointment_1.status}'

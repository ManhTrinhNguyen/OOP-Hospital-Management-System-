from appointment import Appointment
from bill import Bill
from administrator import Administrator
from doctor import Doctor
from patient import Patient
from medical_record import Medical_Record
from datetime import datetime
class Hospital_System:
  # Instances Attribute 
  def __init__(self) -> None:
    self.doctors = [] # List of doctors working in the hospital (list of Doctor objects).
    self.patients = [] # List of registered patients (list of Patient objects).
    self.appointments = [] # List of scheduled appointments (list of Appointment objects).
    self.bills = [] # List of all bills (list of Bill objects).

  # Method
  def register_doctor(self, doctor): # Register Doctor 
    if doctor not in self.doctors: # If doctor is not in the doctor list
      self.doctors.append(doctor)
      return f'Doctor: {doctor} has registered'
    else :
      return f'Doctor: {doctor} has already registered'
    
  def register_patient(self, patient): # Register Patient
    if patient not in self.patients: # If patient is not in the patients list 
      self.patients.append(patient)
      return f'Patient {patient} has registered'
    else: 
      return f'Patient {patient} has already registered'
    
  def schedule_appointment(self, appointment): # Schedules a new appointment for a patient with a doctor.
    if appointment not in self.appointments:
      self.appointments.append(appointment)
      appointment.patient.add_appointment(appointment)
      return f'Scheduled new appointment and added to the appointment list'
    return f'The appointment {appointment} has already scheduled'
  
  def generate_bill(self, patient, services, total_amount): # Generates a new bill for a patient based on services received.
    newBill = Bill(len(self.bills) + 1, patient, services, total_amount) # Create new bill base on Bill class
    self.bills.append(newBill) # add newbill to the bill list
    patient.add_bill(newBill) # add newbill to the patients bill list
    return f'Generated new bill {newBill}'
  
  def find_doctor(self, doctor_id): # Finds and returns a doctor by their ID.
    for doctor in self.doctors: # Iterate through doctors list
      if doctor.doctor_id == doctor_id: # If doctor id found 
        return doctor
      else :
        return f'Doctor id not exist'
      
  def find_patient(self, patient_id): # Finds and returns a patient by their ID.
    for patient in self.patients: # Iterate through the patients list 
      if patient.patient_id == patient_id: # If patient found 
        return patient
      else: 
        return f'Patient id not exist'

  def list_all_appointments(self): # List all appointments 
    for appointment in self.appointments: # Iterate through appointment
      print(appointment)

  def list_appointments_base_on_patient(self, patient):
    for appointment in self.appointments: # Iterate through the appointment 
      if appointment.patient == patient: # if patient in that appointment
        return appointment 
      else :
        return f'No appointment base on this patient: {patient}'
      


  ### Example Usage 

hospital = Hospital_System()
admin = Administrator(admin_id=1, name="Admin John")

# Add doctors
doctor_1 = Doctor(doctor_id=101, name="Dr. Smith", age=45, gender="Male", address="123 Medical St", specialization="Cardiology")
doctor_2 = Doctor(doctor_id=102, name="Dr. Doe", age=39, gender="Female", address="456 Health Ave", specialization="Dermatology")

admin.add_doctor(hospital, doctor_1)
admin.add_doctor(hospital, doctor_2)

# Add patients
patient_1 = Patient(patient_id=201, name="Alice", age=30, gender="Female", address="789 Wellness Blvd")
patient_2 = Patient(patient_id=202, name="Bob", age=25, gender="Male", address="321 Healthy Dr")

admin.add_patient(hospital, patient_1)
admin.add_patient(hospital, patient_2)

# Assign doctors
patient_1.assign_doctor(doctor_1)
patient_2.assign_doctor(doctor_2)

# Schedule appointments
appointment_1 = Appointment(appointment_id=1, patient=patient_1, doctor=doctor_1, date=datetime.now())
hospital.schedule_appointment(appointment_1)

# Add medical record
record_1 = Medical_Record(record_id=1, patient=patient_1, doctor=doctor_1, diagnosis="Heart Disease", treatment="Surgery", date=datetime.now())
patient_1.add_medical_record(record_1)
print(patient_1.medical_history[0])

# Generate bill
hospital.generate_bill(patient_1, services=["Heart Surgery", "Post-op Care"], total_amount=5000)
print(hospital.bills[0].add_payment(4000))
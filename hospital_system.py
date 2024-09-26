from appointment import Appointment
from bill import Bill
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
      

  

from person import Person
from doctor import Doctor

class Patient(Person): 
  # Instances Attribute
  def __init__(self, patient_id: int, name: str, age: int, gender: str, address: str) -> None:
    super().__init__(name, age, gender, address)
    self.patient_id = patient_id
    self.medical_history = [] # List of medical records for the patient 
    self.assigned_doctor =  None # The doctor assigned to the patient (Doctor object).
    self.appointments = [] # List of scheduled appointments (list of Appointment objects).
    self.bills = [] # List of bills generated for the patient (list of Bill objects). 

  def assign_doctor(self, doctor):
    self.assigned_doctor = doctor
    doctor.add_patient(self)
    return f'Assigned doctor: {doctor}'
  def add_appointment(self, appointment): # Adds an appointment to the patient’s list.
    if appointment not in self.appointments: # If the appointment is not in the list 
      self.appointments.append(appointment)
      return f'You have this appointment {appointment} coming up'
    return f'This appointment {appointment} is already on your List'
  
  def add_medical_record(self, record): # Adds a medical record to the patient’s history.
    self.medical_history.append(record)
    return f'Add the record: {record} to the medical history'
  
  def add_bill(self, bill): # Add bill to bill list
    self.bills.append(bill) 
    return self.bills 
  
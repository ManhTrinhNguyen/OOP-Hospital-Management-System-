from person import Person

class Doctor(Person):
  # Instances Attribute 
  def __init__(self, doctor_id: int, name: str, age: int, gender: str, address: str, specialization: int) -> None:
    super().__init__(name, age, gender, address)
    self.doctor_id = doctor_id 
    self.specialization = specialization
    self.patients = [] # List of patients assign to Doctor 

  # Method 
  def add_patient(self, patient): # Assigns a patient to the doctor’s patient list.
    if patient not in self.patients: 
      self.patients.append(patient) 
      return f'Added patient {patient} to Doctor list'
    return f'Patient {patient} already in the Doctor list'
  
  def remove_patient(self, patient): # Removes a patient from the doctor’s list.
    if patient in self.patients:
      self.patients.remove(patient)
      return f'Removed {patient} from the Doctor list'
    return f'Patient {patient} is not in the list' 
  






  
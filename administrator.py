class Administrator: 
  def __init__(self, admin_id: int, name: str):
    self.admin_id = admin_id 
    self.name = name

  def add_doctor(self, doctor, hospital):
    hospital.register_doctor(doctor)

  def add_patient(self, patient, hospital):
    hospital.gegister_patient(patient)
    
class Medical_Record: 
  def __init__(self, record_id: int, patient, doctor, diagnosis: str, treatment: str, date) -> None:
    self.record_id = record_id
    self.patient = patient
    self.doctor = doctor
    self.diagnosis = diagnosis
    self.treatment = treatment
    self.date = date 

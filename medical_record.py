class Medical_Record: 
  def __init__(self, record_id: int, patient, doctor, diagnosis: str, treatment: str, date) -> None:
    self.record_id = record_id
    self.patient = patient # The patient associated with the record (Patient object).
    self.doctor = doctor # The doctor responsible for the diagnosis/treatment (Doctor object).
    self.diagnosis = diagnosis # The diagnosis provided by the doctor (string).
    self.treatment = treatment # The treatment prescribed (string).
    self.date = date # Date of the diagnosis/treatment (datetime object). 



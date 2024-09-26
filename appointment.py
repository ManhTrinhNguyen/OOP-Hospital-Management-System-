class Appointment: 
  # Instances Attribute
  def __init__(self, appointment_id: int, patient, doctor, date, status='Scheduled') -> None:
    self.appointment_id = appointment_id
    self.patient = patient 
    self.doctor = doctor 
    self.date = date 
    self.status = status

  def complete_appointment(self): #  Marks the appointment as completed. 
    if self.status == 'Scheduled': # If Scheduled  it can cancel
      self.status = 'Completed'
      return f'Completed Appointment'
    return f'Cannot not Complete this appointment because this appointment {self.status}'
  
  def cancel_appointment(self): # Cancels the appointment.
    if self.status == 'Scheduled': # If Scheduled  it can cancel 
      self.status = 'Canceled' 
      return 'Canceled the Appointment'
    return f'Cannot not Cancel this appointment because this appointment {self.status}'
  



  
    
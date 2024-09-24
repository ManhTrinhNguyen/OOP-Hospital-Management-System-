class Bill: 
  # Class Attribute
  paid_amount = 0

  # Instances Attribute 
  def __init__(self, bill_id, patient, services, total_amount: float) -> None:
    self.bill_id = bill_id
    self.patient = patient 
    self.services = services
    self.total_amount = total_amount
    self.status = ''

  def __str__(self) -> str:
    return f'The total amount of {self.patient} with {self.services}: {self.total_amount}'

  def add_payment(self, amount): # Adds a payment to the bill and updates the status.
    if amount == self.total_amount: # If amount paid == total amount own
      self.status = 'Paid'
      return 'Paid'
    else: 
      self.status = 'Pending'
      amount_left = self.total_amount - amount
      print(f'{self.patient} is still have {amount_left} left')
      return 'Pending'
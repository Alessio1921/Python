from turtle import pos
from unicodedata import name

# creation of class
class Person:
  def __init__(self,name,lastName,yearBirth,residence):
    # pass
    self.name = name
    self.lastName = lastName
    self.yearBirth = yearBirth
    self.residence = residence

  def personal_profile(self):
    print(self.name.capitalize() , self.lastName.capitalize() , self.yearBirth, self.residence)

  def __str__(self):
    return self.name.capitalize() + " "+ self.lastName.capitalize() 

class Developer(Person):
  def __init__(self, name, lastName, yearBirth, residence, position, annualPay):
    super().__init__(name, lastName, yearBirth, residence)
    self.position = position
    self.annualPay = annualPay

  def profile_employed(self):
    super().personal_profile()
    print(self.position, self.annualPay)

  def __str__(self):
    return  self.position + " " + super().__str__()

# creation of instances

newPerson = Person("lorena", "milano", 1999, "milano")
newPerson.personal_profile()
print(str(newPerson))

newDeveloper = Developer("Francesco", "Di Biaggio", 1990, "Roma", "Front-end" , 30000)
newDeveloper.profile_employed()
print(str(newDeveloper))


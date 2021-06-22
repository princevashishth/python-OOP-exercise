#https://github.com/nrorabaugh/python-oop-exercise


class member:
  def __init__(self, name):
    self.name = name

  def introduce(self):
    print("Hi, My name is ",self.name)

class Student(member):
  def __init__(self,name,reason):
    super().__init__(name)
    self.name = name
    self.reason = reason
  def xx(self):
    print("reason is",self.reason)


class Instructor(member):
  def __init__(self,name,bio):
    super().__init__(name)
    self.name = name
    self.bio = bio
    self.skills = []
  
  def add_skill(self, skill):
    self.skills.append(skill)

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

class Workshop:
  def __init__(self,date,subject):
    self.date = date
    self.subject = subject
    self.students = []
    self.instructors = []

  def add_participant(self, member):
    if(isinstance(member,Student) == True):
      self.students.append(member)
    else:
      self.instructors.append(member)

  def print_details(self):
    print(self.date, " ",self.subject)
    print("Students")
    for x in self.students:
      print(x.name," ",x.reason)
    print("Instructors")
    for x in self.instructors:
      print(x.name," ",x.bio)

x = Workshop("12/03/2014", "Shutl")
x.add_participant(jane)
x.add_participant(lena)
x.add_participant(vicky)
x.add_participant(nicole)
x.print_details()










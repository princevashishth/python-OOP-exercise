class Instructors:
  companyname = "Blueline"
  

  def __init__(self,course,duration):
    self.course = course
    self.duration = duration
  
  def printinfo(self):
    print("My company name is ", Instructors.companyname)


elearning = Instructors("python for beginners",8)   #creating an object for the class
bls = Instructors("Django for beginners",9)  

bls.printinfo()
print(bls.course)

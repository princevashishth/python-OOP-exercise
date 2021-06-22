
class person:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

florist = person("Jane","flowers")    #making object from  the class
florist.printname()
						#one function name is printname() while other's name is printinfo()
class lawyers(person):
  pass

happy_lawyers = lawyers("Jack", "Smiley")
happy_lawyers.printname()


class lawyers2(person):
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname

  def printinfo(self):
    print(self.firstname, self.lastname)

happy_lawyers = lawyers2("Jack", "Smiley")
happy_lawyers.printinfo()

#If we want the derived class to also have a init function, there is a specific way to do that, otherwise it will overwrite init function of base class

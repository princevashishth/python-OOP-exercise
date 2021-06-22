from abc import ABC, abstractmethod

class shape(ABC):
  @abstractmethod    # to make entire class abstract
  def area(self):
    pass
  @abstractmethod
  def perimeter(self):
    pass

class square(shape):
  def __init__(self,side):
    self.side = side

  def area(self):
    return self.__side*self.__side

  def perimeter(self):
    return 4*self.__side


#myshape = shape()   #cannot instantiate an abstract method

myshape = square(5)

print(myshape.area())

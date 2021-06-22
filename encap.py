class cars:
  def __init__(self,speed,color):
    self.__speed = speed           #double underscore to make it private
    self.__color = color

  def set_speed(self,value):
    self.__speed = value

  def get_speed(self):
    return self.__speed

ford = cars(250, "green")
nissan = cars(300, "red")
toyota = cars(350, "blue")

ford.set_speed(450)

ford.speed = 500  #I cannot do this as i cannot access the variable directly since it is private. I would have to use getters(to get value of variable) and setters (to set value of variable)

print(ford.get_speed())

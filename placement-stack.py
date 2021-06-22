
class stack:
  def __init__(self):
    self.ls = []
    self.size =0
  def push(self, num):
    self.ls.append(num)
    self.size = self.size +1
  def pop(self):
    if(self.size == 0):
      print("stack is empty")
    else:
      self.size = self.size-1
  def mysize(self):
    print("My size is ",self.size)
  def elements(self):
    for i in range(self.size):
      print(self.ls[i])

st = stack()

while(1):
  print("push ")
  print("pop ")
  print("size ")
  print("elements ")
  x = input()
  if(x == '1'):
    y = input()
    st.push(y)
  if(x == '2'):
    st.pop()
  if(x == '3'):
    st.mysize()
  if(x == '4'):
    st.elements()
    



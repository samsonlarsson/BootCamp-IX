class Car():
  def __init__(self, model='', name='', make=''):
    self.make = make
     # if model='':
     #   self.make = 'GM' #type

    self.name = name
     # if name = '':
     #  self.name = 'General'

    self.model = model
    #self.wheels = wheels
    
  def checkMake(self):
    
    return self.make
    
  def checkModel(self):
    
    return self.model
    
  def checkName(self):
    
    return self.name
    
  def checkWheels(self):
    
    return self.wheels
    
  def getCarAttributes(self):
    
    return self.make, self.model, self.name

Mycar = Car('buggatti', 'sports', 'Jcar')
# opel = Car('Opel', 'Omega 3')

print (Mycar.checkMake())
print (Mycar.checkModel())
print (Mycar.checkName())
#print (Mycar.checkWheels())
print (Mycar.getCarAttributes())
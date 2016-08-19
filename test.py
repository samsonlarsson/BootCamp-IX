
class PrimeChecker:
  #defining a prime number checker for the integer
  #number = abs(int(number))
  def __init__(self, number = ""):
    self.number = number
    
    #number = int(number)
  
  def is_prime(self):
    # number = 0
    if self.number == '':
      return False
    else:
      number = int(self.number)
       #0 < int(self.number)
    if number == 1:
      return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
prime = PrimeChecker('101')
print(prime.is_prime())

prime2 = PrimeChecker('68')
print(prime2.is_prime())
    
prime3 = PrimeChecker('')
print(prime3.is_prime())
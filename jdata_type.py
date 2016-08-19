def data_type(n):
  ''' 
  this function checks data types parsed in and returns a value, f_back as appropriate.
  '''
  if isinstance(n,str):
    f_back = len(n)
  elif n is None:
    f_back = 'no value'
  elif isinstance(n,bool):
    f_back = n
  elif isinstance(n,int):    
    if n<100:
      f_back = 'less than 100'
    elif n>100:
      f_back = 'more than 100'
    else:
      f_back = 'equal to 100'
  elif isinstance(n,list):
    if len(n)>=3:
      f_back = n[2]
    else:
      f_back = None
  return f_back

print (data_type(True))
####notes###
# an alternative to the isinstance() function is type()
#tricky bit, bool data type is a sub class of the int. Condition check for bool to come before the integer check

def reverse_string(s):
  
  n = len(s)
  reverse=[]
  
  while n>0:
    reverse.append(s[n-1])
    n-=1
  
  if ''.join(reverse) == s:
    
    return True
    
  else:
    
    return ''.join(reverse)
    
print(reverse_string('jodom'))
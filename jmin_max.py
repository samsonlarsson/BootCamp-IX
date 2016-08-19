def find_max_min(l):
  
  mn = min(l)
  mx = max(l)
  min_max = []
  
  if mn==mx:
    
    min_max = [len(l),]
  
  else:
    print('do nothing')
    min_max = [mn,mx]
    
  return min_max

print(find_max_min([1,2,3,1,2,1,3,5,4,6,8,7]))
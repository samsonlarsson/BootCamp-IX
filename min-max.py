# def find_max_min_one(num):
#     num = []

#     while (number != int(-1)):
#         num_list.append(number)
#         high = max(num_list)
#         low = min(num_list)
        
def find_max_min(list):
 
    min = list[0]

    for elm in list[1:]:
      
      if elm < min:                            
        min = elm 
    return elm

def max(list):
    max = list[0] 
    for elm in list[1:]:        
      if elm > max:
        max = elm

    return max

  

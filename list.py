
# def list_compare(list1, list2):
# 	# list1 = []
# 	# list2 = []
# 	for value in list1:
# 	  if val in list2:
# 			  return True
#     return False


#       	# if [item for item in list1 if item in list2]:
#  #    return item
#   # else:
def find_missing(list1, list2):
	if len(list1) == 0 and len(list2) == 0 or len(list1) == len(list2):
		return 0
	else:
		if len(list1) > len(list2):
			for i in list1:
				if i not in list2:
					return i
		elif len(list2) > len(list1):
			for i in list2:
				if i not in list1:
					return i


# list1 = [1,2,3]
# list2 = [1,2,3,4]
# print(find_missing(list1, list2))

list3 = [14, 10]
list4 = [77, 66, 13]
print(find_missing(list3,list4))

print(find_missing([],[]))
print(find_missing([1],[2]))
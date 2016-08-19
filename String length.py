def string_length(str_arg):
	output_list = []
	# check to see if str_arg is a string
	if type(str_arg) == str:
		output_list.append(len(str_arg))
	#  check to see if str_arg is a list
	elif type(str_arg) == list:
		for i in range(len(str_arg)):
			output_list.append(len(str_arg[i]))
	return output_list

def string_length(string):
  r = []

  if type(string) == str:
  	r.append(len(string))
  elif type(string) == list:
    for i in string:
      r.append(len(string))
  return r
  
def accumulating():
  list = []
  list = strings.split("")
  return list

#assuming that the string entered ends with a \0, which would make it the C-style string
def reverser(something):
	real_length = (len(something)-2)
	print real_length
	i = real_length - 1
	formatted_string = ""
	while i >= 0:
		formatted_string += something[i]
		i -= 1
	formatted_string += "\\0"
	return formatted_string
	

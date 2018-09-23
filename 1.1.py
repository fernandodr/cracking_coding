str = raw_input("type a string")

def is_unique(str):
	for char in str:
		if str.count(char) > 1:
			return False
	return True


if is_unique(str):
	print "True"
else:
	print "False"
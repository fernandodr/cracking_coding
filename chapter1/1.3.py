def rem_duplicates(string):
	without_duplicates = ""
	for char in string:
		if char not in without_duplicates:
			without_duplicates += char
	return without_duplicates
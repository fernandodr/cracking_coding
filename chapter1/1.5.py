def replacer(to_be_transformed):
	replaced = ""
	for char in to_be_transformed:
		if char != " ":
			replaced += char
		else:
			replaced += "%20"
	return replaced

#assuming that the string entered ends with a \0, which would make it the C-style string

something = raw_input("Enter a string: ")

real_length = (len(something)-2)

print real_length

i = real_length - 1
reversed = ""
while(i>=0):
	reversed = reversed + something[i]
	i = i - 1
reversed = reversed + "\\0"

print reversed
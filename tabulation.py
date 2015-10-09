import sys
import io
import string

#level >= 0 if using smart, None otherwise
level = None

def smart():
	return (level is not None) and (level >= 0)

def enable_smart():
	global level
	level = 0

def disable_smart():
	global level
	level = None

def convert(s):
	return s.replace("\\t", "\t")

if sys.argv[1] == "-s":
	enable_smart()

if smart():
	dot_pos = sys.argv[-3].rfind(".")
	# a dot as the first character usually indicates a hidden file
	if dot_pos > 0:
		file_type = sys.argv[-3][dot_pos + 1:]
		if file_type not in ["py", "java", "c", "cpp"]:
			print("File extension not supported. Not using smart mode.")
			disable_smart()
	else:
		print("File extension could not be detected. Not using smart mode.")
		disable_smart()

f = open(sys.argv[-3], "rt")
remove = convert(sys.argv[-2])
add = convert(sys.argv[-1])

s = ""
for line in f:
	index = 0
	while line.find(remove) == index:
		line = line.replace(remove, add, 1)
		index += len(add)
	s += line

print(s)

f.close()
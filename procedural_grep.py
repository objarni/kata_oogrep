# 'procedural_grep.py' is a quick thrown-together "traditional procedural style" implementation
# of the simplistic grep of this kata.
#
# The idea is being able to compare the two versions (oo grep.py and procedural_grep.py) side
# by side to see what London School code looks like in relation to a more traditional approach.

def grep(substring):

	def grep_file(file, substring):
		f = open(file, 'r')
		for number, content in enumerate(f):
			if substring in content:
				msg = file + ":" + str(number + 1) + ":" + content
				print(msg)

	import os
	files = os.listdir('.')
	for file in files:
		if os.path.isfile(file):
			grep_file(file, substring)


if __name__ == "__main__":
	import sys
	if len(sys.argv) != 2:
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")
	else:
		grep(substring=sys.argv[1])

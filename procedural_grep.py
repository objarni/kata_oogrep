# procedural_grep is a quick thrown-together "traditional procedural style" implementation
# of the simplistic grep of this kata.
# The idea is being able to compare what the two versions side by side to see what
# London School code looks like in relation to a more traditional approach.

def grep(substring):
	pass



if __name__ == "__main__":
	import sys
	if len(sys.argv) != 2:
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")
	else:
		grep(substring=sys.argv[1])

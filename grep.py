class HelpDisplayer:
	def display_help(self):
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")

class Grep: pass

class GrepCommandLineInterpreter:
	def __init__(self, helpdisplayer=HelpDisplayer(), grep=Grep()):
		self.helpdisplayer = helpdisplayer
		self.grep = grep

	def run(self, args):
		if len(args)==1:
			self.grep.run(args[0])
		else:
			self.helpdisplayer.display_help()

if __name__ == '__main__':
	import sys
	GrepCommandLineInterpreter().run(sys.argv[1:])
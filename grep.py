class HelpDisplayer:
	def display_help(self):
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")

class CurrentDirFileSearcher: pass
class MatchPrinter: pass

class Grep:
	def __init__(self, searcher=CurrentDirFileSearcher(), printer=MatchPrinter()):
		self.searcher = searcher
		self.printer = printer

	def run(self, substring):
		self.searcher.search_using_substring(substring)

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
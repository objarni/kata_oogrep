class HelpDisplayer:
	def display_help(self):
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")

class CurrentDirFileSearcher: pass

class Console:
	def print(self, line):
		print(line)

class Printer:
	def __init__(self, console=Console()):
		self.console = console

	def register_hit(self, file, line_number, line_content):
		self.console.print(file + ":" + str(line_number) + ": " + line_content)

class Grep:
	def __init__(self, searcher=CurrentDirFileSearcher(), printer=Printer()):
		self.searcher = searcher
		self.printer = printer

	def search_for(self, substring):
		self.searcher.send_hits_to(self.printer)
		self.searcher.search_using_substring(substring)

class GrepCommandLineInterpreter:
	def __init__(self, helpdisplayer=HelpDisplayer(), grep=Grep()):
		self.helpdisplayer = helpdisplayer
		self.grep = grep

	def run(self, args):
		if len(args)==1:
			self.grep.search_for(args[0])
		else:
			self.helpdisplayer.display_help()

if __name__ == '__main__':
	import sys
	GrepCommandLineInterpreter().run(sys.argv[1:])
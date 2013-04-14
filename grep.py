class HelpDisplayer:
	def display_help(self):
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")

class Console: pass

class MatchPrinter:
	def __init__(self, console=Console()):
		self.console = console

	def register_hit(self, file, line_number, line_content):
		self.console.print(file + ":" + str(line_number) + ": " + line_content)

class FileGrepper: pass
class FileLister: pass

class Grep:
	def __init__(self, file_grepper=FileGrepper(), file_lister=FileLister()):
		self.grepper = file_grepper
		self.lister = file_lister

	def search_for(self, substring):
		self.grepper.grep_for(substring)
		self.lister.list_files_to(self.grepper)

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
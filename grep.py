class HelpDisplayer:
	def display_help(self):
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")

class GrepFileProcessor: pass
class CurrentDirFileSource: pass

class Grep:
	def __init__(self, file_processor=GrepFileProcessor(), file_source=CurrentDirFileSource()):
		self.file_processor = file_processor
		self.file_source = file_source

	def run(self, substring):
		for file in self.file_source.find_files():
			self.file_processor.process_file(file)

class GrepCommandLineInterpreter:
	def __init__(self, helpdisplayer=HelpDisplayer(), grep=Grep()):
		self.helpdisplayer = helpdisplayer
		self.grep = grep

	def run(self, args):
		if len(args)==1:
			self.grep.run(args[0])
		else:
			self.helpdisplayer.display_help()


	void Run(List<string> args) {
		if(args.Count == 1)
			grep.Run(args[0]);
		else
			HelpDisplayer.display_help();
	}

if __name__ == '__main__':
	import sys
	GrepCommandLineInterpreter().run(sys.argv[1:])
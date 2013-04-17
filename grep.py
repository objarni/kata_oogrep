class HelpDisplayer:

	def display_help(self):
		print("Usage: python proc_grep.py <substring>")
		print(".. will list all rows containing <substring>")
		print("looking in all files in the current directory.")


class Console:

	def print(self, msg):
		print(msg)


class MatchPrinter:

	def __init__(self, console=Console()):
		self.console = console

	def register_hit(self, file, line_number, line_content):
		self.console.print(file + ":" + str(line_number) + ": " + line_content)


class LineGrepper:

	def __init__(self, match_printer=MatchPrinter()):
		self.match_printer = match_printer

	def looking_in_file(self, filename):
		self.filename = filename

	def grep_for(self, substring):
		self.substring = substring

	def receive_row(self, line_number, line_content):
		if self.substring in line_content:
			self.match_printer.register_hit(self.filename, line_number, line_content)

class RowReader:

	def read_rows(file):
		for row in open(file):
			yield row

	def __init__(self, get_all_rows=read_rows):
		self.get_all_rows = get_all_rows

	def enumerate_file(self, filename, target):
		for linenum, content in enumerate(self.get_all_rows(filename)):
			target.receive_row(linenum + 1, content)


class FileGrepper:

	def __init__(self, row_reader=RowReader(), line_grepper=LineGrepper()):
		self.row_reader = row_reader
		self.line_grepper = line_grepper

	def receive_file(self, file):
		self.line_grepper.looking_in_file(file)
		self.row_reader.enumerate_file(file, self.line_grepper)

	def grep_for(self, substring):
		self.line_grepper.grep_for(substring)

class FileLister:

	def dirfiles():
		import os
		for candidate in os.listdir('.'):
			if os.path.isfile(candidate):
				yield candidate

	def __init__(self, dirfiles=dirfiles):
		self.dirfiles = dirfiles

	def list_files_to(self, target):
		for file in self.dirfiles():
			target.receive_file(file)


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
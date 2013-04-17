from mockito import *
from grep import *


### GrepCommandLineInterpreter ###
# .. is responsible for interpreting input from command line
def test_GrepCommandInterpreter_on_zero_arguments_displays_help():
	verify_help_displayed_with_arglist([])

def test_GrepCommandInterpreter_on_two_arguments_displays_help():
	verify_help_displayed_with_arglist([1, 2])

def test_GrepCommandInterpreter_calls_grep_if_one_argument():
	grep = mock()
	interpreter = GrepCommandLineInterpreter(grep=grep)
	interpreter.run(['abc'])
	verify(grep).search_for('abc')

def verify_help_displayed_with_arglist(arglist):
	helpdisplayer = mock()
	interpreter = GrepCommandLineInterpreter(helpdisplayer=helpdisplayer)
	interpreter.run(arglist)
	verify(helpdisplayer).display_help();


### Grep ###
# Grep has one command: search_for(substring).
# It collaborates with a FileLister, responsible
# for listing files in current directory (in simplest
# case), and a FileGrepper, which does Grep on a single
# file.
def test_Grep_uses_substring_in_grepper():
	grepper = mock()
	grep = Grep(file_grepper=grepper, file_lister=mock())
	grep.search_for('abcdef')
	verify(grepper).grep_for('abcdef')

def test_Grep_uses_grepper_as_output_of_file_lister():
	grepper = mock()
	file_lister = mock()
	grep = Grep(file_grepper=grepper, file_lister=file_lister)
	grep.search_for('abcdef')
	verify(file_lister).list_files_to(grepper)


### FileLister ###
# .. is responsible for listing files and sending them
# forward to another object.
def test_FileLister_sends_all_found_files_to_target():
	def dirfiles():
		return ['a', 'b', 'c']
	file_lister = FileLister(dirfiles=dirfiles)
	target = mock()
	file_lister.list_files_to(target)
	verify(target).receive_file('a')
	verify(target).receive_file('b')
	verify(target).receive_file('c')


### FileGrepper ###
# .. is responsible for looking for a substring in a file,
# and reporting the result to a match printer.
# It does this by ordering a RowReader to send all
# enumerated rows in a file to a LineGrepper.
# So it's actually only responsible for linking the RowReader
# and LineGrepper together.
def test_FileGrepper_uses_line_grepper_as_target_of_rowreader():
	row_reader = mock()
	line_grepper = mock()
	file_grepper = FileGrepper(row_reader=row_reader, line_grepper=line_grepper)
	file_grepper.receive_file('somefile')
	verify(row_reader).enumerate_file('somefile', line_grepper)

def test_FileGrepper_tells_line_grepper_what_file_is_being_searched():
	row_reader = mock()
	line_grepper = mock()
	file_grepper = FileGrepper(row_reader=row_reader, line_grepper=line_grepper)
	file_grepper.receive_file('somefile')
	verify(line_grepper).looking_in_file('somefile')

def test_FileGrepper_tells_line_grepper_which_substring_to_search_for():
	row_reader = mock()
	line_grepper = mock()
	file_grepper = FileGrepper(row_reader=row_reader, line_grepper=line_grepper)
	file_grepper.grep_for('abc')
	file_grepper.receive_file('somefile')
	verify(line_grepper).grep_for('abc')


### RowReader ###
# ... is responsible for enumerating the rows of a file
def test_RowReader_enumerates_correctly():
	def get_all_rows(file):
		yield 'abc'
		yield 'def'
		yield 'ghi'
	target = mock()
	row_reader = RowReader(get_all_rows=get_all_rows)
	row_reader.enumerate_file('somefile', target)
	verify(target).receive_row(1, 'abc')
	verify(target).receive_row(2, 'def')
	verify(target).receive_row(3, 'ghi')


### MatchPrinter ###
# .. receives hits (grep matches), which are printed to a console.
def test_MatchPrinter_output():
	console = mock()
	printer = MatchPrinter(console=console)
	printer.register_hit('File1.txt', 10, 'abc')
	verify(console).print('File1.txt:10: abc')


### LineGrepper ###
# .. which is responsible for finding a substring in a line,
# and sending it forward if it finds it
def test_LineGrepper_sends_correct_information_on_hit():
	target = mock()
	line_grepper = LineGrepper(match_printer=target)
	line_grepper.grep_for('abc')
	line_grepper.looking_in_file('somefile')
	line_grepper.receive_row(3, 'yo abc yo')
	verify(target).register_hit('somefile', 3, 'yo abc yo')

if __name__ == '__main__':
	import pytest
	pytest.main()

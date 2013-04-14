from mockito import *

from grep import *

# GrepCommandLineInterpreter tests
def test_on_zero_arguments_displays_help():
	verify_help_displayed_with_arglist([])

def test_on_two_arguments_displays_help():
	verify_help_displayed_with_arglist([1, 2])

def verify_help_displayed_with_arglist(arglist):
	helpdisplayer = mock()
	interpreter = GrepCommandLineInterpreter(helpdisplayer=helpdisplayer)
	interpreter.run(arglist)
	verify(helpdisplayer).display_help();

def test_calls_grep_if_one_argument():
	grep = mock()
	interpreter = GrepCommandLineInterpreter(grep=grep)
	interpreter.run(['abc'])
	verify(grep).search_for('abc')

# Grep tests
# Grep has one command: search_for(substring).
# It collaborates with a FileLister, responsible
# for listing files in current directory (in simplest
# case), and a FileGrepper, which does Grep on a single
# file.
def test_uses_substring_in_grepper():
	grepper = mock()
	grep = Grep(file_grepper=grepper, file_lister=mock())
	grep.search_for('abcdef')
	verify(grepper).grep_for('abcdef')

def test_uses_grepper_as_output_of_file_lister():
	grepper = mock()
	file_lister = mock()
	grep = Grep(file_grepper=grepper, file_lister=file_lister)
	grep.search_for('abcdef')
	verify(file_lister).list_files_to(grepper)

def test_filelister_sends_all_found_files_to_target():
	def dirfiles():
		return ['a', 'b', 'c']
	file_lister = FileLister(dirfiles=dirfiles)
	target = mock()
	file_lister.list_files_to(target)
	verify(target).receive_file('a')
	verify(target).receive_file('b')
	verify(target).receive_file('c')

# The printer receives hits, which are printed to stdout.
def test_printer_output():
	console = mock()
	printer = MatchPrinter(console=console)
	printer.register_hit('File1.txt', 10, 'abc')
	verify(console).print('File1.txt:10: abc')

if __name__ == '__main__':
	import pytest
	pytest.main()

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
# On technical regard, grep.run(substring) searches all files
# in current directory for occurances of 'substring'. All hits
# are reported nicely to stdout.
# 
# Implementationwise, Grep collaborates with a Searcher,
# responsible for finding matches, and a Printer,
# responsible for printing matches nicely to the console.

# make sure the substring is used for searching
def test_grep_searches_using_substring():
	searcher = mock()
	grep = Grep(searcher=searcher)
	grep.search_for('substring')
	verify(searcher).search_using_substring('substring')

# make sure grep uses the Printer in the Searcher
def test_grep_uses_printer_in_searcher():
	searcher = mock()
	printer = mock()
	grep = Grep(searcher=searcher, printer=printer)
	grep.search_for('yoyo')
	verify(searcher).send_hits_to(printer)

if __name__ == '__main__':
	import pytest
	pytest.main()

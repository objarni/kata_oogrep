from mockito import *

from grep import *

# having more or less than one argument to grep
# causes usage message to be displayed, and
# app to quit


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
	verify(grep).run('abc')

# Grep tests
# On technical regard, grep.run(substring) searches all files
# in current directory for occurances of 'substring'. All hits
# are reported nicely to stdout.
# 
# Implementationwise, Grep collaborates with a Searcher,
# responsible for finding matches, and a Printer,
# responsible for printing matches nicely to the console.

# - make sure grep uses the Printer in the Searcher
def test_grep_searches_using_substring():
	searcher = mock()
	grep = Grep(searcher=searcher)
	grep.run('substring')
	verify(searcher).search_using_substring('substring')

def test_grep_tells

if __name__ == '__main__':
	import pytest
	pytest.main()

from mockito import *

from grep import *

# having more or less than one argument to grep
# causes usage message to be displayed, and
# app to quit


def test_on_zero_arguments_displays_help():
	verify_help_displayed_with_args()

def test_on_two_arguments_displays_help():
	verify_help_displayed_with_args(1, 2)

def verify_help_displayed_with_args(*args):
	helpdisplay = mock()
	grep = Grep(helpdisplay)
	grep.run(args)
	verify(helpdisplay).display_help();


if __name__ == '__main__':
	import pytest
	pytest.main()

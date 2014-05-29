Kata: OO grep
=============

The purpose of this kata is to try and implement a "London School Grown" (simple) grep implementation in Python3.



Dependencies
------------
* Python3 (for running grep)
* mockito (for running tests)
* py.test (for running tests)

Running grep
------------
    /home/objarni/kata_oogrep/exampledir$ python grep.py somestring

.. or, which should produce identical output

    /home/objarni/kata_oogrep/exampledir$ python procedural_grep.py somestring

... which is supposed to produce this output:

    File1.txt:1: This is a line with somestring in it.
    File1.txt:2: The second line also contains somestring!
    File2.txt:10: Line 10 in File2.txt features a somestring also.

Running tests
-------------
    /home/objarni/kata_oogrep$ python test_grep.py
    




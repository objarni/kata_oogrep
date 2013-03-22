Kata: OO grep
=============

The purpose of this kata is to try and implement a "London School Grown" (simple) grep implementation in Python3.

It uses mockito for test doubles (i.e. stubs, fakes, spies or mocks) and py.test to run the tests.

Running oogrep
--------------
    /home/kata_oogrep$ python grep.py somestring
    
    File1.txt:1: This is a line with somestring in it.
    File1.txt:2: The second line also contains somestring!
    File2.txt:10: Line 10 in File2.txt features a somestring also.

Running tests
-------------
    /home/kata_oogrep$ py.test




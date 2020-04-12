# 42 push_swap checker

## Intro
This is a custom checker script for _Push_swap_ project which students of [42 Programming School](https://en.wikipedia.org/wiki/42_(school)) learn after _Print-f_ project on branch of algorithms. 

## OS compatability
Right now, Python script adapted only for School's iMacs and similar Macs with OS Sierra or Catalina. 

Script was not tested for Linux OS family.

Script was not adapted for Windows.

## Script how-to

All you need to do:
1. Clone a script in root of your _push_swap_ project repo:

		git clone https://github.com/orsk-moscow/42_push_swap_checker.git

2. Execute this command in root of your _push_swap_ project repo:

		python3 42_push_swap_checker/test_it.py

3. Answer this questions by typing 'yes' or 'no':

_Do you have any errors or bugs?_

## Covered cases
Script checks all base cases, excluding memory leaks and Norme:
1. Error management for _checker_ binary as well as for _push_swap_ binary
- Test of error arguments: duplicates in arguments 
- Test of error arguments: non-numbers in arguments
- Test of error arguments: int overflow detection
2. Valid tests for _checker_ binary:
- Array sorted
- Array not sorted
- Test of instructions execution: array sorted after execution
- Test of instructions execution: array _not_ sorted after execution
3. Test for no arguments for _checker_ binary
4. Test of pipeline from _push_swap_ and _checker_
- For arrays of 1-5 numbers for all permutations
- For arrays of 10-500 numbers

## TODO
- More description coming soon.
- Add _author_ file checking
- Show feedback question only in case of failed tests
- Add success message at the end of script

## Feature requests
If you have a feature request or you just found uncovered case, do not hesitate open an Issue

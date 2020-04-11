# 42 push_swap checker

## Intro
This is a custom checker script for _Push_swap_ project which students of [42 Programming School](https://en.wikipedia.org/wiki/42_(school)) learn after _Print-f_ project on branch of algorithms. 

## Requirements
Right now, Python script adapted only for School's IMacs and similar Macs with Mac OS Sierra or Catalina. 
Script was not tested for Linux OS family.
Script was not adapted for Windows.

## Covered cases
Script checks all base cases, excluding memory leaks and Norme:
1. Error management for _checker_ binary as well as for _push_swap_ binary
- Test of error arguments: duplicates in arguments 
- Test of error arguments: non-numbers in arguments
- Test of error arguments: int overflow detection
2. Valid tests for _checker_ binary:
- Array sorted
- Array not sorted
- Test of instructions execution: - array sorted after execution
- Test of instructions execution: - array _not_ sorted after execution
3. Test for no arguments for _checker_ binary
4. Test of pipeline from push_swap ands checker
- For arrays of 1-5 numbers
- For arrays of 10-500 numbers

## TODO
More description coming soon.

#!/usr/bin/env python
# coding: utf-8

# 0. Libraries import
import os

try:import numpy
except:os.system("pip3 install -q numpy --user")

import io
import sys
import subprocess

from numpy import arange
from numpy import array
from numpy.random import MT19937, RandomState, SeedSequence, shuffle, randint, choice
from itertools import permutations, combinations

# 1. Local variables and functions definition
INT_MAX = 2**31-1
INT_MIN = -2**31

def make_test_checker(array, stdin_input, errors_test = False, silent = True, success = False):
    l = len(array)
    argv = " ".join(map(str,array))
    args = "/checker " + argv
    args = os.path.abspath(".") + args
    args = args.split()
    p = subprocess.run(args,
                       input = stdin_input,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    if errors_test:
        if bytes.decode(p.stderr) != "Error\n":
            if not silent: print("Test failed with %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%(l,argv,
                                  bytes.decode(p.stdout),
                                  bytes.decode(p.stderr)))
            return -1
        if bytes.decode(p.stdout) != "":
            if not silent: print("Test failed with %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%(l,argv,
                                  bytes.decode(p.stdout),
                                  bytes.decode(p.stderr)))
            return -2
        if success: print("Test passed correctly, your checker program detected mistakes in argv properly")
        return 1
    if bytes.decode(p.stderr) != "":
        if not silent: print("Test failed with %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%(l,argv,
                              bytes.decode(p.stdout),
                              bytes.decode(p.stderr)))
        return -1
    if bytes.decode(p.stdout) == "KO\n":
        if not silent: print("Array do NOT sorted after execution all your instructions with %i arguments: %s"%(l,argv))
        return 1        
    if bytes.decode(p.stdout) == "OK\n":
        if success: print("Array sorted after execution all your instructions with %i arguments"%(l))
        return 2
    if not silent: print("There is an exception occured for %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%                         (l,argv,
                          bytes.decode(p.stdout),
                          bytes.decode(p.stderr)))
    return -10

def make_test_push_swap(array, errors_test = False, silent = True, success = False):
    l = len(array)
    argv = " ".join(map(str,array))
    args = "/push_swap " + argv
    args = os.path.abspath(".") + args
    args = args.split()
    p = subprocess.run(args,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    if errors_test:
        if bytes.decode(p.stderr) != "Error\n":
            if not silent: print("Test failed with %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%(l,argv,bytes.decode(p.stdout),bytes.decode(p.stderr)))
            return -1
        if bytes.decode(p.stdout) != "":
            if not silent: print("Test failed with %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%(l,argv,bytes.decode(p.stdout),bytes.decode(p.stderr)))
            return -2
        if success: print("Test passed correctly, your push_swap program detected mistakes in argv properly")
        return 1
    if bytes.decode(p.stderr) != "":
        if not silent: print("Test failed with %i arguments:\n%s\nSTDOUT output:\n%s\nSTDERR output:\n%s"%(l,argv,bytes.decode(p.stdout),bytes.decode(p.stderr)))
        return -1
    return p.stdout


def feedback():
	print("\nDo you have any errors or bugs?\nType \'yes\' or \'no\':")
	orig_out = sys.stdout
	while True:
		sys.stdout = io.StringIO()
		inp = input()
		sys.stdout = orig_out
		if inp == 'yes' or inp == 'no':
			break
	if inp == "yes":
		print("\nPlease, fix bugs/errors and welcome back\nGood luck!\n")
		sys.exit()
	return None


# 2. Making necessary compilations
cwd = os.getcwd()
try:
	os.system("cd libft && make re && make clean")
finally:os.chdir(cwd)
try:os.system("make re && make clean")
finally:os.chdir(cwd)

# 3. Base tests for all permutations of ints in range 5
#All tests for this chapter should be passed as correct
array_sizes = range(1,6)
print("_________________________________________")
print("1. Test of error args: duplicates in argv")
print("1.1 Test for CHECKER binary")
i1 = 0
i2 = 0
i3 = 0
for size in array_sizes:
    for arr in permutations(arange(size), size):
        arr = list(arr) + [arr[randint(0,len(arr))]]
        shuffle(arr)
        res = make_test_checker(arr,"",errors_test = True, silent = True)
        if res == 1:i1+=1
        elif res == -1:i2+=1
        elif res == -2:i2+=1
        elif res == -10:i3+=1
    for arr in permutations(arange(1, size + 1), size):
        arr = list(arr) + [arr[randint(0,len(arr))]]
        shuffle(arr)
        res = make_test_checker(arr,"",errors_test = True, silent = True)
        if res == 1:i1+=1
        elif res == -1:i2+=1
        elif res == -2:i2+=1
        elif res == -10:i3+=1
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))
print("1.2 Test for PUSH_SWAP binary")
i1 = 0
i2 = 0
i3 = 0
for size in array_sizes:
    for arr in permutations(arange(size), size):
        arr = list(arr) + [arr[randint(0,len(arr))]]
        shuffle(arr)
        res = make_test_push_swap(arr,errors_test = True, silent = True)
        if res == 1:i1+=1
        elif res == -1:i2+=1
        elif res == -2:i2+=1
        elif res == -10:i3+=1
    for arr in permutations(arange(1, size + 1), size):
        arr = list(arr) + [arr[randint(0,len(arr))]]
        shuffle(arr)
        res = make_test_push_swap(arr,errors_test = True, silent = True)
        if res == 1:i1+=1
        elif res == -1:i2+=1
        elif res == -2:i2+=1
        elif res == -10:i3+=1
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

# 5. Test of non-numbers detection
array_mistakes = ['a', 'one', '1-', 'tt', '@',  '1\\n', '\\n','\\n\\n\\n1']
print("__________________________________________")
print("2. Test of error args: non-numbers in argv")
print("2.1 Test for CHECKER binary")
i1 = 0
i2 = 0
i3 = 0
for mistake in array_mistakes:
    for size in array_sizes:
        for arr in permutations(arange(size), size):
            arr = list(arr) + [mistake]
            shuffle(arr)
            res = make_test_checker(arr,"",errors_test = True, silent = True)
            if res == 1:i1+=1
            elif res == -1:i2+=1
            elif res == -2:i2+=1
            elif res == -10:i3+=1
        for arr in permutations(arange(1, size + 1), size):
            arr = list(arr) + [mistake]
            shuffle(arr)
            res = make_test_checker(arr,"",errors_test = True, silent = True)
            if res == 1:i1+=1
            elif res == -1:i2+=1
            elif res == -2:i2+=1
            elif res == -10:i3+=1
                
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))
print("2.2 Test for PUSH_SWAP binary")
i1 = 0
i2 = 0
i3 = 0
for mistake in array_mistakes:
    for size in array_sizes:
        for arr in permutations(arange(size), size):
            arr = list(arr) + [mistake]
            shuffle(arr)
            res = make_test_push_swap(arr,errors_test = True, silent = True)
            if res == 1:i1+=1
            elif res == -1:i2+=1
            elif res == -2:i2+=1
            elif res == -10:i3+=1
        for arr in permutations(arange(1, size + 1), size):
            arr = list(arr) + [mistake]
            shuffle(arr)
            res = make_test_push_swap(arr,errors_test = True, silent = True)
            if res == 1:i1+=1
            elif res == -1:i2+=1
            elif res == -2:i2+=1
            elif res == -10:i3+=1          
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

# 6. Test of ints sizes detection
array_sizes = [1, 2, 3, 4, 5, 100, 500]
print("_____________________________________________")
print("3. Test of error args: int overflow detection")
print("3.1 Test for CHECKER binary")
i1 = 0
i2 = 0
i3 = 0
for size in array_sizes:
    arr = [randint(2*INT_MIN, INT_MIN - 1)] + list(randint(INT_MIN, INT_MAX, size))
    shuffle(arr)
    res = make_test_checker(arr,"",errors_test = True, silent = True)
    if res == 1:i1+=1
    elif res == -1:i2+=1
    elif res == -2:i2+=1
    elif res == -10:i3+=1
        
for size in array_sizes:
    arr = [randint(INT_MAX + 1, 2*INT_MAX)] + list(randint(INT_MIN, INT_MAX, size))
    shuffle(arr)
    res = make_test_checker(arr,"",errors_test = True, silent = True)
    if res == 1:i1+=1
    elif res == -1:i2+=1
    elif res == -2:i2+=1
    elif res == -10:i3+=1
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

print("3.2 Test for PUSH_SWAP binary")
i1 = 0
i2 = 0
i3 = 0
for size in array_sizes:
    arr = [randint(2*INT_MIN, INT_MIN - 1)] + list(randint(INT_MIN, INT_MAX, size))
    shuffle(arr)
    res = make_test_push_swap(arr,errors_test = True, silent = True)
    if res == 1:i1+=1
    elif res == -1:i2+=1
    elif res == -2:i2+=1
    elif res == -10:i3+=1
for size in array_sizes:
    arr = [randint(INT_MAX + 1, 2*INT_MAX)] + list(randint(INT_MIN, INT_MAX, size))
    shuffle(arr)
    res = make_test_push_swap(arr,errors_test = True, silent = True)
    if res == 1:i1+=1
    elif res == -1:i2+=1
    elif res == -2:i2+=1
    elif res == -10:i3+=1        
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

# 7. Test of random numbers
print("________________________________________________")
print("4. Valid tests for program Checker: array sorted")
i1 = 0
i2 = 0
i3 = 0
cnt = 0
while cnt < 10:
    for size in array_sizes:
        arr = list(randint(INT_MIN, INT_MAX + 1, size))
        arr.sort()
        res = make_test_checker(arr,"",errors_test = False, silent = True)
        if res == 2:i1+=1
        elif res == 1:i2+=1
        elif res == -2:i2+=1
        elif res == -10:i3+=1
    cnt += 1
print("\nDo you have any bugs?\nType \'yes\' or \'no\':")
orig_out = sys.stdout
while True:
    sys.stdout = io.StringIO()
    inp = input()
    sys.stdout = orig_out
    if inp == 'yes' or inp == 'no':
        break
if inp == "yes":sys.exit()
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))
array_sizes = [2, 3, 4, 5, 100, 500]
print("____________________________________________________")
print("5. Valid tests for program Checker: array not sorted")
i1 = 0
i2 = 0
i3 = 0
cnt = 0
while cnt < 10:
    for size in array_sizes:
        arr = list(randint(INT_MIN, INT_MAX + 1, size))
        arr.sort(reverse=True)
        res = make_test_checker(arr,"",errors_test = False, silent = True, success=True)
        if res == 1:i1+=1
        elif res == 2:
            i2+=1
        elif res == -1:
            i2+=1
        elif res == -10:i3+=1
    cnt += 1
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

# 8. Test of instructions (for checker binary)
pairs = [
        [[21, 0, 564, 666, 8239], 'sa\n'],
        [[21, 0, 564, 666, 8239], 'pb\npb\nsb\npa\npa\n'],
        [[21, 0, 666, 564, 8239], 'pb\npb\nss\npa\npa\n'],
        [[8239, 0, 21, 564, 666], 'ra\n'],
        [[21, 564, 0, 666, 8239], 'pb\npb\npb\nrb\npa\npa\npa\n'],
        [[21, 564, 0, 8239, 666], 'pb\npb\npb\nrr\npa\npa\npa\n'],
        [[21, 564, 666, 8239, 0], 'rra\n'],
        [[8239, 0, 21, 564, 666], 'pb\npb\npb\npb\npb\nrrb\npa\npa\npa\npa\npa\n'],
        [[8239, 0, 21, 564, 666, 89363250, 98363250, 8956325], 'pb\npb\npb\npb\npb\nrrr\npa\npa\npa\npa\npa\n'],
        ]
print("________________________________________________")
print("6. Test of instructions exections (for checker binary)")
print("All instructions correct")
i1 = 0
i2 = 0
i3 = 0
for array, command in pairs:
    command = bytes(command,encoding = 'ascii')
    res = make_test_checker(array, command, errors_test = False, silent = False, success=False)
    if res == 2:i1+=1
    elif res == 1:i2+=1
    elif res == -1:i2+=1
    elif res == -10:i3+=1
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

pairs = [
        [[21, 0, 564, 666, 8239], 'sa\npb\n'],
        [[21, 0, 564, 666, 8239], 'pb\npb\nsb\npa\n'],
        [[21, 0, 666, 564, 8239], 'pb\npb\nss\npa\n'],
        [[8239, 0, 21, 564, 666], 'ra\npb\n'],
        [[21, 564, 0, 666, 8239], 'pb\npb\npb\nrb\npa\npa\npa\npb\n'],
        [[21, 564, 0, 8239, 666], 'pb\npb\npb\nrr\npa\npa\n'],
        [[21, 564, 666, 8239, 0], 'rra\npb\npb\npa\n'],
        [[8239, 0, 21, 564, 666], 'pb\npb\npb\npb\npb\nrrb\npa\npa\npa\npa\npa\npb\n'],
        [[8239, 0, 21, 564, 666, 89363250, 98363250, 8956325], 'pb\npb\npb\npb\npb\nrrr\npa\npa\npa\npa\n'],
        ]
print("________________________________________________")
print("7. Test of instructions executions (for checker binary)")
print("All instructions NOT correct")
i1 = 0
i2 = 0
i3 = 0
for array, command in pairs:
    command = bytes(command,encoding = 'ascii')
    res = make_test_checker(array, command, errors_test = False, silent = True, success=False)
    if res == 1:i1+=1
    elif res == 2:i2+=1
    elif res == -1:i2+=1
    elif res == -10:i3+=1
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

# 9. Test with no args
array_nothing = []
instructions = [
                'sa\n',
                'sb\n',
                'ss\n',
                'ra\n',
                'rb\n',
                'rr\n',
                'rra\n',
                'rrb\n',
                'rrr\n',
                'pa\n',
                'pb\n',
                ]
print("________________________________________________")
print("8. Test for no argv (for checker binary)")
i1 = 0
i2 = 0
i3 = 0
for command in instructions:
    command = bytes(command,encoding = 'ascii')
    res = make_test_checker(array_nothing, command, errors_test = False, silent = True, success=False)
    if res == 1:i2+=1
    elif res == 2:i2+=1
    elif res == -2:i2+=1
    elif res == -10:i1+=1

sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))

feedback()

# 10. Test of pipeline from push_swap ands checker for array of 1-5 numbers
array_sizes = range(1,6)
print("__________________________________________")
print("9. Test of pipeline from push_swap ands checker for array of 1-5 numbers")
i1 = 0
i2 = 0
i3 = 0
list_amounts = []
for size in array_sizes:
    cnt = 0
    sum_instructions = 0
    for arr in permutations(arange(size), size):
        instructions = make_test_push_swap(arr,errors_test = False, silent = True)
        if instructions == -1:i3+=1
        else:
            cnt+=1
            res = make_test_checker(arr,instructions, silent = False)
            if res == 2:i1+=1
            else:i2+=1
            sum_instructions+=len(bytes.decode(instructions).split('\n')[:-1])
    list_amounts.append(sum_instructions//cnt)

sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))
for size, amount in zip(array_sizes, list_amounts):
    print("\nAverage amount of instructions for array size %4i:%-5i"%(size,amount))

feedback()

# 11. Test of pipeline from push_swap and checker for array of 10-500 numbers
array_sizes = [10,20,30,40,50,75,100,200,300,400,500]
print("____________________________________________________________________________")
print("10. Test of pipeline from push_swap ands checker for array of 10-500 numbers\n")
i1 = 0
i2 = 0
i3 = 0
list_amounts = []
for i, size in enumerate(array_sizes):
    cnt = 0
    cnt2 = 0
    sum_instructions = 0
    while cnt2 < 50:
        arr = choice(arange(-size, size), size,replace = False)
        shuffle(arr)
        instructions = make_test_push_swap(arr,errors_test = False, silent = True)
        if instructions == -1:i3+=1
        else:
            cnt+=1
            res = make_test_checker(arr,instructions, silent = False)
            if res == 2:i1+=1
            else:i2+=1
            sum_instructions+=len(bytes.decode(instructions).split('\n')[:-1])
        cnt2+=1
    list_amounts.append(sum_instructions//(cnt if cnt != 0 else 1))
sum_ = i1+i2+i3
print("Resume:\n%4i/%-4i tests passed\n%4i/%-4i tests failed\n%4i/%-4i tests finished unexpectedly"%(i1,sum_,i2,sum_,i3,sum_,))
for size, amount in zip(array_sizes, list_amounts):
    print("\nAverage amount of instructions for array size %4i:%-5i"%(size,amount))

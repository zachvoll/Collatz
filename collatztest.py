'''
Author: Zachary Vollen
a test file for collatz.py
for testing the visual graphics just run it and look at it.
'''
#TODO add more tests for collatz, node generation, and vertex generation

import unittest
from collatz import *

'''
int -> bool
tests if collatz function works.
'''
def test_collatz(n):
    testdict = collatz(n)

    #check if all values from 1 to n are in the dictionary
    missingvals = []
    for i in range(1, n+1):
        if (not (i in testdict)):
            missingvals.append(i)

    #check if all values are in dictionary as keys as well
    missingkeys = []
    for key, value in testdict.items():
        if (not (value in testdict)):
            missingkeys.append(value)

    #check all key: value relationships are correct
    badevens = []
    badodds  = []
    for key, value in testdict.items():
        if(key != 1):
            if((key % 2 == 0) and key//2 != value):
                badevens.append((key,value))
            elif((key % 2 != 0) and (3*key+1) != value):
                badodds.append((key,value))

    testpassed = True
    if missingvals:
        print("missing values", missingvals)
        testpassed = False
    if missingkeys:
        print("missing keys", missingkeys)
        testpassed = False
    if badevens:
        print("bad evens", badevens)
        testpassed = False
    if badodds:
        print("bad odds", badodds)
        testpassed = False

    return testpassed


class CollatzTests(unittest.TestCase):
    #check errors
    def test_ltone_scatter(self):
        self.assertRaises(collatz_scatter(0))

    def test_ltone_tree(self):
        self.assertRaises(collatz_tree(0))

    #check collatz
    def test_collatz_one(self):
        self.assertTrue(test_collatz(1))

    def test_collatz_ten(self):
        self.assertTrue(test_collatz(10))

    def test_collatz_hundred(self):
        self.assertTrue(test_collatz(100))

    #check points
    def test_genpoints_one(self):
        reldict = collatz(1)
        actpoints = gen_points(reldict)
        exppoints = {1: 0}
        self.assertEquals(actpoints, exppoints)

    def test_genpoints_five(self):
        reldict = collatz(5)
        actpoints = gen_points(reldict)
        exppoints = {1:0, 2:1, 3:7, 4:2, 5:5, 8:3, 10:6, 16:4}
        self.assertEquals(actpoints, exppoints)

    #check lines
    def test_genlines_one(self):
        reldict = collatz(1)
        points = gen_points(reldict)
        actlines = gen_lines(points, reldict)
        explines = list()
        self.assertEquals(actlines, explines)

    def test_genlines_five(self):
        reldict = collatz(5)
        points = gen_points(reldict)
        actlines = gen_lines(points, reldict)
        print("actlines", list(actlines))
        explines = [(2, 1, 1, 0), (3, 10, 7, 6), (10, 5, 6, 5), (5, 16, 5, 4),
                    (16, 8, 4, 3), (8, 4, 3, 2), (4, 2, 2, 1)]
        self.assertEquals(len(list(actlines)), len(explines))
        self.assertEquals(set(list(actlines)), set(explines))

if __name__ == '__main__':
    unittest.main()
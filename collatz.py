'''
Author: Zachary Vollen
Motivation: I wanted to generate a visual representation of the collatz conjecture using Python.
Usage: TODO
'''
#TODO fix tree grapher
#TODO add usage
#TODO update for cython usage

import matplotlib.pyplot as plt
import networkx as nx
import sys, argparse

#suppress deprecated warning errors
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    #change ignore to always if you want to see them
    warnings.simplefilter("ignore")
    fxn()

'''
int -> int:int dictionary
collatz takes in a number and generates collatz sequeunces for numbers [1,n].
It utilizes a memoization dictionary to avoid having to repeat solving for previously found sequences.
e.g. if you already solved for 8 with the solution being 8:4, 4:2, 2:1, 1:1 and wanted 16 you'd
generate just 16:8, add it to the dictionary, and already have the answer for 8.
'''
def collatz(n):
    reldict = {1: 1}
    oldn = 1
    for i in range(2, n+1):
        while (i not in reldict):
            oldn = i
            if (i % 2 == 0):
                i //= 2
            else:
                i = 3 * i + 1
            if (oldn not in reldict):
                reldict[oldn] = i
    return reldict

'''
int:int dictionary -> int:int dictionary
get all of the number:steps points to be plotted
'''
def gen_points(reldict):
    points = dict()
    for key in reldict.keys():
        theval = key
        steps = 0
        while (key != 1):
            key = reldict[key]
            steps += 1
        points[theval] = steps
    return points

'''
int:int dictionary -> int:int dictionary -> (int*int*int*int) list
generates all of the lines between points to be plotted
'''
def gen_lines(points, reldict):
    del reldict[1]
    for key,value in reldict.items():
        yield (key, value, points[key], points[value])

'''
int -> None
does all of the graphing and calls the other functions
'''
def collatz_scatter(n):
    if(n <= 0):
        raise ValueError("int must be greater than zero.")

    #initialize graph
    plt.xlabel('Number')
    plt.ylabel('Steps')

    # get points
    reldict = collatz(n)
    points = gen_points(reldict)
    pls = list(points.items())
    xs = list()
    ys = list()
    for (x, y) in pls:
        xs.append(x)
        ys.append(y)

    # add points
    plt.scatter(xs, ys, s=5)

    #get lines
    lines = gen_lines(points,reldict)

    #place lines
    for (x1, x2, y1, y2) in lines:
        plt.plot([x1,x2], [y1,y2], '-k')

    plt.show()

'''
int -> None
creates a tree of collatz sequences with 1 as the root
'''
def collatz_tree(n):
    if (n <= 0):
        raise ValueError("int must be greater than zero.")

    #initialize tree
    Tree = nx.DiGraph()

    reldict = collatz(n)

    del reldict[1]
    for key,value in reldict.items():
        Tree.add_edge(key, value)

    t = nx.drawing.nx_pydot.to_pydot(Tree)
    #TODO fix graphing as a tree
    #t.write_png('collatz_tree.png')

    nx.draw(Tree)
    plt.show()

if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=int, default=1, help='provide a number greater than zero')
    parser.add_argument('--y', type=str, default='t', help='do you want a scatter or tree? (s or t)')
    args = parser.parse_args()
    '''

    gtype = ''
    data  = ''
    while(True):
        data = input('q to quit, t for tree, s for scatter: ')
        if(data == 'q'):
            sys.exit(0)
        elif(data == 't'):
            gtype = 't'
            break
        elif(data == 's'):
            gtype = 's'
            break
        else:
            print('invalid input, you entered: ', data)

    n = 1
    while(True):
        data = input('q to quit, n for number you want: ')
        if(data == 'q'):
            sys.exit(0)
        else:
            try:
                n = int(data)
                break
            except:
                print('invalid input, you entered: ', data)

    if(gtype == 't'):
        collatz_tree(n)
    elif(gtype == 's'):
        collatz_scatter(n)
    else:
        raise ValueError('function type wasn\'t set properly.')
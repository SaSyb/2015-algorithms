# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:45:02 2015

@author: Thinkerbell
"""
#import unittest
#import incidence_matrix
import board.py

def main():
    myBoard = board.Board(10, 10, [])
    print(myBoard.representation())

    # create Incidence Matrixi

    # find a covering
    # count it
    # return total covering number


#suite = unittest.TestLoader().loadTestsFromTestCase(CoveringWithPentominos)

if __name__ == '__main__':
    main()
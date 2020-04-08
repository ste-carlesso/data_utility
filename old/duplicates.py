# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:23:48 2020

@author: Carlesso
"""


def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

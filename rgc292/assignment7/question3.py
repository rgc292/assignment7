'''
Created on Nov 3, 2015

@author: Rafael Garcia (rgc292)
'''

import numpy as np

class Question3(object):
    '''
    This class is intended to compute the calculations for
    question 3
    '''


    def __init__(self):
        pass
    
    #Generate a 10 x 3 array of random numbers in the range  [0,1]
    def generate_array_10_3(self):
        array_10_3 = np.random.rand(10,3)
        return array_10_3

    #Print out a 1D array containing 10 values, each value is the number
    #closest to 0.5 from the corresponding row of the array_10_3
    def pick_closest_per_row(self, array1):
        array_10_3 = (np.abs(array1-.5)).argsort()
        selection = array_10_3[:,0:1]
        array_selection = list()
        x = -1
        try:
            for index in selection:
                x += 1
                array_selection.append(array1[x][index[0]])
        except IndexError:
            pass
            
        array_selection = np.asarray(array_selection)    
        return array_selection

        
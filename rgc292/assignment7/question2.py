'''
Created on Nov 3, 2015

@author: Rafael Garcia (rgc292)
'''

import numpy as np

class Question2(object):
    '''
    This class is intended to compute the calculations for
    question 2
    '''

    #create the 2D array
    def __init__(self):
        pass
        
        
    #Create array X and divide each column elementwise with Y
    def divide_element_wise(self):
        try:
            matrix = np.arange(25).reshape(5,5)
            array = np.array([1., 5, 10, 15, 20])
            result = matrix/array
        except IndexError:
            pass
        return result  
    
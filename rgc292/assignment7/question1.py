'''
Created on Nov 3, 2015

@author: Rafael Garcia (rgc292)
'''
import numpy as np

class Question1(object):
    '''
    This class is intended to compute the calculations for
    question 1
    '''

    def __init__(self):
        pass
    
    
    def create_2darray(self): 
        first_row = np.arange(1,12,5)
        second_row = np.arange(2,13,5)
        third_row = np.arange(3,14,5)
        fourth_row = np.arange(4,15,5)
        fifth_row = np.arange(5,16,5)
        matrix = np.matrix([first_row,second_row,third_row,fourth_row,fifth_row]) 
        return matrix 
    
    #Generate a new array containing the 2nd and 4th rows
    def create_array_2nd_4th_rows(self, matrix):
        new_matrix = np.delete(matrix,[0,2,4,5],0)
        return new_matrix
        
    #Generate a new array that contains the 2nd column
    def create_array_2nd_column(self, matrix):
        new_array = matrix[:5,1:2]
        return new_array
    
    #Generate a new array that contains all the elements in the rectangular 
    #section between the coordinates  [1,0] and  [3,2]
    def create_array_from_section(self, matrix):
        new_array = matrix[1:4,:]
        return new_array
    
    #Generate a new array that contains only elements with values that are 
    #between 3 and 11
    def create_array_between_3_11(self, matrix):
        new_array = np.ravel(matrix)
        new_array = list(new_array)
        array_list = list()
        
        values_check = list(range(4, 11))
        for item in new_array:
            for value in values_check:
                if item == value:
                    array_list.append(item)
        new_array = np.asarray(np.sort(array_list))
        return new_array        
        
        
        
        
        
     

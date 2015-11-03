'''
Created on Nov 3, 2015

@author: Rafael Garcia (rgc292)
'''

import numpy as np

class Question4(object):
    '''
    This class is intended to compute the calculations for
    question 4
    '''


    def __init__(self):
        pass
        
    #Compute the Mandelbrot fractal set using the Mandelbrot iteration      
    def compute_mandelbrot_fractal(self):
        N_max = 50
        some_threshold = 50
        x = np.arange(-2,1)
        y = np.arange(-1.5,1.5)
        #Cross-multiply x and y for obtaining a cartesian product
        cross_multiplication = np.meshgrid(x,y)
        cartesian_product = np.append(cross_multiplication[0].reshape(-1,1),
                                 cross_multiplication[1].reshape(-1,1),axis=1)
        #Set both array to c32 type to avoid overflowing
        c = np.array([10],dtype='c32')
        z = np.array([10],dtype='c32')
        #Separates left and right columns
        cartesian_left = np.asarray(cartesian_product[:,0:1])
        cartesian_right = np.asarray(cartesian_product[:,1:2]) 
        #build the complex number
        c = cartesian_left + 1j*cartesian_right
        z = c
        mandelbrot_set = list()
        np.seterr(all='ignore')
        #Apply the iteration 
        try:
            for index in np.arange(9):
                for v in range(N_max):
                    z[index] = (z[index]**2) + (c[index])
            
                if abs(z[index]) < some_threshold:
                    mandelbrot_set.append(cartesian_product[index])
                else:
                    continue    
        except (OverflowError, RuntimeWarning, FloatingPointError):
            pass 
              
        state = np.asarray(mandelbrot_set) 
        test = np.asanyarray(cartesian_product)
        #Evaluate the boolean mask with the desired values against the whole set 
        mask = np.in1d(test, state).reshape(test.shape)
        return mask
  
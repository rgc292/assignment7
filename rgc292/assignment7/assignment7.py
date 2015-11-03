'''
Created on Nov 3, 2015

@author: Rafael Garcia (rgc292)
'''

import matplotlib.pyplot as plt
import question1 as q1
import question2 as q2
import question3 as q3
import question4 as q4

"""This main module is intended to implement the solutions for all 
    questions on assignment7"""

if __name__ == '__main__':
    pass

try:
    question1 = q1.Question1()
    question2 = q2.Question2()
    question3 = q3.Question3()
    question4 = q4.Question4()

    #Answers for question 1
    print "Question 1."
    array_2d = question1.create_2darray()
    print array_2d
    print "\n" 

    print "a) "
    array_2nd_4th_rows = question1.create_array_2nd_4th_rows(array_2d)
    print array_2nd_4th_rows
    print "\n"

    print "b) "
    array_2nd_column = question1.create_array_2nd_column(array_2d)
    print array_2nd_column
    print "\n"

    print "c) "
    array_from_section = question1.create_array_from_section(array_2d)
    print array_from_section
    print "\n"

    print "d)"
    array_between_3_11 = question1.create_array_between_3_11(array_2d)
    print array_between_3_11
    print "\n"

    #Answer for question 2
    print "Question 2"
    elementwise_division = question2.divide_element_wise()
    print elementwise_division
    print "\n"

    #Answer for question 3
    print "Question 3 "
    array_10_3 = question3.generate_array_10_3()
    pick_closest_per_row = question3.pick_closest_per_row(array_10_3)
    print pick_closest_per_row
    print "\n"

    #Answer for question 4
    print "Question 4"
    mandelbrot_fractal = question4.compute_mandelbrot_fractal()
    mask = mandelbrot_fractal
    print "mandelbrot.png figure saved on file!"

    plt.imshow(mask.T, extent=(-2,1,-1.5,1.5))
    plt.gray()
    plt.savefig('mandelbrot.png')    
except (KeyboardInterrupt, RuntimeError, RuntimeWarning, ValueError, TypeError):
    pass






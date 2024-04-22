"""functions.py - Adlab Lab 6

Author: Ricky Gonzales
Version: April 22nd, 2024

This code contains various functions related to the radiation lab
"""


import numpy as np
from scipy.optimize import curve_fit


def lin_curve(x,b,m):
    """This function defines a linear curve for curve-fitting a set of data
    
    Inputs:
        x (list): An array of x-values
        m (float): The slope of the data
        b (flaot): The y-intercept of the data
        
    Returns:
        m*x + b (float): The graph of a fitted linear curve
        
    """
    return m*x + b


def decay_const(time, counts):
    """This function approximates the decay-constant for the radioactive decay of a radioacitve source from
        counts and time arrays.
        
    Inputs:
        time (list): An array of time-intervals from the radioactive decay
        counts (list): An array of counts from the radioactive decay
        
    Returns:
        lambda (float): The decay constant
        
    """
    ln_time = np.log(time) #Take the natural log of the time data
    ln_counts = np.log(counts) #Take the natural log of the counts data
    rd_fit, rd_cov = curve_fit(lin_curve, ln_time, ln_counts) #Curve-fit to a linear graph
    lamb = -rd_fit[0] #Extract the slope of the linear graph
    
    #Once the lambda value has been extracted, this function then returns the value.
    return lamb
    
    

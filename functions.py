"""functions.py - Adlab Lab 6

Author: Ricky Gonzales
Version: April 22nd, 2024

This code contains various functions related to the radiation lab
"""


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def stats(counts, length):
    """This function prints and calculates statistics for the Adlab radiation lab
    
    Inputs:
        counts (array): The array of the counts
        length (float): The length of the distance from the source to the geiger tube
        
    Returns:
        error (float): The percentage of the approximated Error using Poissons Equation
        
    """
    print(f"\nThe number of counts taken for {length} m is: {sum(counts)}")
    error = 1/np.sqrt(sum(counts))
    print(f"Error for {length} m is: {error*100:.5f}%\n")
    return error


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


def log_fix(num):
    """This function defines the method of making sure that all values in a data-set are real when taking
        the natural log
        
    Inputs:
        num (list): A list of numbers
        
    Returns:
        num (int): Zero if the natural log of the number is undefined
        np.log(num): A value if the natural log is defined.
        
    """
    new_list = np.zeros(len(num)) #Create an empty array to store the new values
    
    for i in range(len(num)): #Iterate through the array
        if np.log(num[i]) < 0: #If the natural log is undefined, replace with a zero
            new_list[i] = 0
            
        elif np.log(num[i]) > 0: #Else it is defined, replace with the value
            new_list[i] = np.log(num[i])
            
    #Then return the natural log list
    return new_list
    
    
def decay_const(time, counts):
    """This function approximates the decay-constant for the radioactive decay of a radioacitve source from
        counts and time arrays.
        
    Inputs:
        time (list): An array of time-intervals from the radioactive decay
        counts (list): An array of counts from the radioactive decay
        
    Returns:
        lambda (float): The decay constant
        
    """
    ln_time = log_fix(time) #Take the natural log of the time data
    ln_counts = log_fix(counts) #Take the natural log of the counts data
    rd_fit, rd_cov = curve_fit(lin_curve, ln_time, ln_counts) #Curve-fit to a linear graph
    lamb = -rd_fit[0] #Extract the slope of the linear graph
    
    #Once the lambda value has been extracted, this function then returns the value.
    return lamb
    

def plot_counts(time, counts, length):
    """This function plots the counts vs time for a radiactive decay
    
    Inputs:
        time (list): Time values
        counts (list): Counts values
        length (float): The length of the distance from the source to the detector
        
    Returns:
        None
        
    """
    
    title = f"The Counts vs Time for the {length} length"
    plt.figure(figsize=(7,5))
    plt.plot(time, counts,label='Activity')
    plt.title(title)
    plt.xlabel('Time (sec)')
    plt.ylabel("Counts")
    plt.legend()
    plt.grid()
    plt.show()
    

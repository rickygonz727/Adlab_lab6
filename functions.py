"""functions.py - Adlab Lab 6

Author: Ricky Gonzales
Version: April 22nd, 2024

This code contains various functions related to the radiation lab
"""


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



def true_counts(array_count,background):
    """This function defines the method to obtain the true radiation count array for a specific array
    
    Inputs:
        array_count (array): The original array of radiation counts
        background (array): The background radiation counts
        
    Return:
        new_array (array): The radiation array when considering background radiation
        
    """
    
    avg_background = np.round(np.average(background)) #Take the average of the radiation counts
    #After the average is computed, we want a new array that is the same size as the original array
    new_array = np.zeros(len(array_count))
    #With this, we then begin a loop that subtracts all of the elements by this average value.
    for i in range(len(array_count)):
        #If the value ends up negative, then we replace with a zero in the new array
        if array_count[i] - avg_background < 0:
            new_array[i] = 0
        #If the value is non-negative or zero, then we simply replace with the actual value.
        elif array_count[i] - avg_background >= 0:
            new_array[i] = array_count[i] - avg_background
    #After the new array is built, we then return the new array
    return new_array            
    
def stats(counts, length,condition):
    """This function prints and calculates statistics for the Adlab radiation lab
    
    Inputs:
        counts (array): The array of the counts
        length (float): The length of the distance from the source to the geiger tube
        condition (bool): The condition of where or not to print the values within this function
        
    Returns:
        values (list): A list of the error and the summation of all the counts. 
        
    """
    sigma = np.sqrt(sum(counts))
    error = sigma / sum(counts)

    if condition:
        print(f"\nThe number of counts taken for {length} m is: {sum(counts)}")
        print(f"Error for {length} m is: {error*100:.5f}%\n")
    
    values = [error, sum(counts)]
    return values


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
    

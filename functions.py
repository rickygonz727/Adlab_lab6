"""functions.py - Adlab Lab 6

Author: Ricky Gonzales
Version: April 22nd, 2024

This code contains various functions related to the radiation lab
"""


import numpy as np
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
    sigma = np.sqrt(sum(counts)) #Take the square root of the total counts
    error = sigma / sum(counts) #Calculate the possions error by dividing by the total counts
    
    #If our condition to print is true, then we print the statistics
    if condition:
        print(f"\nThe number of counts taken for {length} m is: {sum(counts)}")
        print(f"Error for {length} m is: {error*100:.5f}%\n")
    
    #Afterwards, we then define a list with the remaining values and return by the function. 
    values = [error, sum(counts)]
    return values


def plot_counts(distance, counts, group):
    """This function plots the counts vs distance for a radiactive decay
    
    Inputs:
        distance (list): Time values
        counts (list): Counts values
        group (int): The group number
        
    Returns:
        None
        
    """
    
    title = f"Counts vs Distance of Group #{group}"
    plt.figure(figsize=(7,5))
    plt.scatter(distance, counts,label='Data')
    plt.title(title)
    plt.xlabel('Distance (m)')
    plt.ylabel("Counts")
    plt.legend()
    plt.grid()
    plt.show()
    
    
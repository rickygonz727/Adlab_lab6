"""Statistics python calculator for Radiation Data

Authors: Ad-Lab 3 Spring 24 Semester
Version" April 19th, 2024

"""

import numpy as np


time1, counts1 = np.genfromtxt("rad_70cm.txt",skip_header=7, unpack=True)
time2, counts2 = np.genfromtxt("rad_60cm.txt",skip_header=7, unpack=True)
time3, counts3 = np.genfromtxt("rad_50cm.txt",skip_header=7, unpack=True)
time4, counts4 = np.genfromtxt("rad_40cm.txt",skip_header=7, unpack=True)
time5, counts5 = np.genfromtxt("rad_30cm.txt",skip_header=7, unpack=True)
time6, counts6 = np.genfromtxt("rad_25cm.txt",skip_header=7, unpack=True)
time7, counts7 = np.genfromtxt("rad_20cm.txt",skip_header=7, unpack=True)
time8, counts8 = np.genfromtxt("rad_15cm.txt",skip_header=7, unpack=True)
time9, counts9 = np.genfromtxt("rad_10cm.txt",skip_header=7, unpack=True)
time10, counts10 = np.genfromtxt("rad_05cm.txt",skip_header=7, unpack=True)


def stats(counts, length):
    """This function prints and calculates statistics for the Adlab radiation lab
    
    Inputs:
        counts (array): The array of the counts
        length (float): The length of the distance from the source to the geiger tube
        
    Returns:
        error (float): The percentage of the approximated Error using Poissons Equation
        
    """
    print(f"\nThe number of counts taken for {length} m is: {sum(counts)}")
    error = np.sqrt(sum(counts))
    print(f"Error for {length} m is: {error*100:.5f}%\n")
    return error



if __name__ == "__main__":
    stats(counts1,0.7)
    stats(counts2,0.6)
    stats(counts3,0.5)
    stats(counts4,0.4)
    stats(counts5,0.3)
    stats(counts6,0.25)
    stats(counts7,0.2)
    stats(counts8,0.15)
    stats(counts9,0.1)
    stats(counts10,0.05)
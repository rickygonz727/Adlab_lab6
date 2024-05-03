"""Code for the Radiation Lab - Adlab Lab 6

Authors: Ad-Lab 3 Spring 24 Semester
Version" April 19th, 2024

"""

import numpy as np
import functions as fn
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#%% Import Data

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
time1h, counts1h = np.genfromtxt("measurement_1_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time1h, counts19h = np.genfromtxt("measurement_19_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time1h, counts37h = np.genfromtxt("measurement_37_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time1h, counts55h = np.genfromtxt("measurement_55_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time1h, counts69h = np.genfromtxt("measurement_69_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time1h, counts84h = np.genfromtxt("measurement_84_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time1h, counts98h = np.genfromtxt("measurement_98_holedown.csv", delimiter=',', skip_header=1,unpack=True)
timebg, countsbg = np.genfromtxt("background.csv",delimiter=',', skip_header=1, unpack=True)


#%% Main Function
if __name__ == "__main__":
    
    #%% Radiation Counts Definitions.
    
    
    
    counts1 = fn.true_counts(counts1,countsbg)
    counts2 = fn.true_counts(counts2,countsbg)
    counts3 = fn.true_counts(counts3,countsbg)
    counts4 = fn.true_counts(counts4,countsbg)
    counts5 = fn.true_counts(counts5,countsbg)
    counts6 = fn.true_counts(counts6,countsbg)
    counts7 = fn.true_counts(counts7,countsbg)
    counts8 = fn.true_counts(counts8,countsbg)
    counts9 = fn.true_counts(counts9,countsbg)
    counts10 = fn.true_counts(counts10,countsbg)
    
    counts1h = fn.true_counts(counts1h,countsbg)
    counts19h = fn.true_counts(counts19h,countsbg)
    counts37h = fn.true_counts(counts37h,countsbg)
    counts55h = fn.true_counts(counts55h,countsbg)
    counts69h = fn.true_counts(counts69h,countsbg)
    counts84h = fn.true_counts(counts84h,countsbg)
    counts98h = fn.true_counts(counts98h,countsbg)


    #%% Distance Array
    #May have to edit this
    distance = np.zeros(10)
    distance[0] = 0.7
    distance[1] = 0.6
    distance[2] = 0.5
    distance[3] = 0.4
    distance[4] = 0.3
    distance[5] = 0.25
    distance[6] = 0.2
    distance[7] = 0.15
    distance[8] = 0.1
    distance[9] = 0.05

    #Counts Array
    #This section creates an array for the sum of the counts for each interval while also returning the uncertainty
    sum_counts = np.zeros(10)
    sum_counts[0] = fn.stats(counts1,0.7,True)[1]
    sum_counts[1] = fn.stats(counts2,0.6,True)[1]
    sum_counts[2] = fn.stats(counts3,0.5,True)[1]
    sum_counts[3] = fn.stats(counts4,0.4,True)[1]
    sum_counts[4] = fn.stats(counts5,0.3,True)[1]
    sum_counts[5] = fn.stats(counts6,0.25,True)[1]
    sum_counts[6] = fn.stats(counts7,0.2,True)[1]
    sum_counts[7] = fn.stats(counts8,0.15,True)[1]
    sum_counts[8] = fn.stats(counts9,0.1,True)[1]
    sum_counts[9] = fn.stats(counts10,0.05,True)[1]
    
    #%% Radiation Sheilding Plot
    #This plots Counts vs Distance
    plt.figure(1)
    plt.figure(figsize=(7,5))
    plt.title("The Relationship between Counts and Distance")
    plt.xlabel("Distance (m)")
    plt.ylabel("Counts")
    plt.scatter(distance, sum_counts,label='Shielding Trend')
    x = np.linspace(0.05,1,1000)
    plt.plot(x,16/((x**2)), label='Inverse Square')
    plt.legend()
    plt.grid()
    plt.show()
    
    #%% Radiation Counts vs Time
    #This section plots the counts vs time, which is what we had originally gotten on loggerpro during the lab.
    #We can probably null this out for now. 
    fn.plot_counts(time1,counts1,0.7)
    fn.plot_counts(time2,counts2,0.6)
    fn.plot_counts(time3,counts3,0.5)
    fn.plot_counts(time4,counts4,0.4)
    fn.plot_counts(time5,counts5,0.3)
    fn.plot_counts(time6,counts6,0.25)
    fn.plot_counts(time7,counts7,0.2)
    fn.plot_counts(time8,counts8,0.15)
    fn.plot_counts(time9,counts9,0.1)
    fn.plot_counts(time10,counts10,0.05)

#%% Finding Area of the Detector

    intensity_array = np.zeros(10)
    int1 = np.average(counts1) / np.average(time1)
    int2 = np.average(counts2) / np.average(time2)
    int3 = np.average(counts3) / np.average(time3)
    int4 = np.average(counts4) / np.average(time4)
    int5 = np.average(counts5) / np.average(time5)
    int6 = np.average(counts6) / np.average(time6)
    int7 = np.average(counts7) / np.average(time7)
    int8 = np.average(counts8) / np.average(time8)
    int9 = np.average(counts9) / np.average(time9)
    int10 = np.average(counts10) / np.average(time10)
    intensity_array[0] = int1
    intensity_array[1] = int2
    intensity_array[2] = int3
    intensity_array[3] = int4
    intensity_array[4] = int5
    intensity_array[5] = int6
    intensity_array[6] = int7
    intensity_array[7] = int8
    intensity_array[8] = int9
    intensity_array[9] = int10
    
    int_fit, int_cov = curve_fit(fn.lin_curve,intensity_array, 1/(distance**2))
    
    plt.figure(2)
    plt.figure(figsize=(7,5))
    plt.scatter(intensity_array, 1/(distance**2), label='Strength')
    plt.plot(intensity_array, fn.lin_curve(intensity_array, int_fit[1],int_fit[0]), label='Fitted Curve')
    plt.xlabel("Intensity (C/s)")
    plt.ylabel("1 / r^2")
    plt.legend()
    plt.grid()
    plt.show()
    
    S = int_fit[0] * 2 * np.pi
    C = np.average(intensity_array)
    area = np.zeros(10)
    area1 = (C / S) * 2 * np.pi*((distance[0])**2)
    area2 = (C / S) * 2 * np.pi*((distance[1])**2)
    area3 = (C / S) * 2 * np.pi*((distance[2])**2)
    area4 = (C / S) * 2 * np.pi*((distance[3])**2)
    area5 = (C / S) * 2 * np.pi*((distance[4])**2)
    area6 = (C / S) * 2 * np.pi*((distance[5])**2)
    area7 = (C / S) * 2 * np.pi*((distance[6])**2)
    area8 = (C / S) * 2 * np.pi*((distance[7])**2)
    area9 = (C / S) * 2 * np.pi*((distance[8])**2)
    area10 = (C / S) * 2 * np.pi*((distance[9])**2)
    area[0] = area1
    area[1] = area2
    area[2] = area3
    area[3] = area4
    area[4] = area5
    area[5] = area6
    area[6] = area7
    area[7] = area8
    area[8] = area9
    area[9] = area10

    print(np.average(area))

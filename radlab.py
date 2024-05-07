"""Code for the Radiation Lab - Adlab Lab 6

Authors: Ad-Lab 3 Spring 24 Semester
Version" April 19th, 2024

"""

import numpy as np
import functions as fn
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#%% Import Data

#Importing data from two different groups.
#This chunk of data came from the group without the lego stand.
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

#This next chunk imports the code from the lego setup. 
time1h, counts1h = np.genfromtxt("measurement_1_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time19h, counts19h = np.genfromtxt("measurement_19_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time37h, counts37h = np.genfromtxt("measurement_37_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time55h, counts55h = np.genfromtxt("measurement_55_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time69h, counts69h = np.genfromtxt("measurement_69_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time84h, counts84h = np.genfromtxt("measurement_84_holedown.csv", delimiter=',', skip_header=1,unpack=True)
time98h, counts98h = np.genfromtxt("measurement_98_holedown.csv", delimiter=',', skip_header=1,unpack=True)

#This imports the background radiation, which will be used to obtain the true counts for each trial. 
timebg, countsbg = np.genfromtxt("background.csv",delimiter=',', skip_header=1, unpack=True)


#%% Main Function
if __name__ == "__main__":
    
    #%% Radiation Counts with respect to Background radiation
    
    #In order to get the actual counts for each radiation trial, we run this true_counts function with the original
    #data-sets with the background radiation.
    #For each of these lines, it redefines the radiation counts array into a new array.
    #The true_counts process is explained in functions.py
    
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
    
    #With our counts-values organized, we then work towards building an array of distance values from the different radiation
    #measurements. These values are ordered from group 1 to group 2.
    
    distance = np.zeros(17)
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
    distance[10] = 0.792
    distance[11] = 0.648
    distance[12] = 0.504
    distance[13] = 0.36
    distance[14] = 0.248
    distance[15] = 0.128
    distance[16] = 0.016

    #%%Counts Array
    #This section creates an array for the sum of the counts for each interval while also returning the uncertainty
    #It creates a new array of to store the values that were created from the stats function
    sum_counts = np.zeros(17)
    
    sum_counts[0] = fn.stats(counts1h,0.792,True)[1]
    sum_counts[1] = fn.stats(counts1,0.7,True)[1]
    sum_counts[2] = fn.stats(counts19h,0.648,True)[1]
    sum_counts[3] = fn.stats(counts2,0.6,True)[1]
    sum_counts[4] = fn.stats(counts37h,0.504,True)[1]
    sum_counts[5] = fn.stats(counts3,0.5,True)[1]
    sum_counts[6] = fn.stats(counts4,0.4,True)[1]
    sum_counts[7] = fn.stats(counts55h,0.36,True)[1]
    sum_counts[8] = fn.stats(counts5,0.3,True)[1]
    sum_counts[9] = fn.stats(counts6,0.25,True)[1]
    sum_counts[10] = fn.stats(counts69h,0.248,True)[1]
    sum_counts[11] = fn.stats(counts7,0.2,True)[1]
    sum_counts[12] = fn.stats(counts8,0.15,True)[1]
    sum_counts[13] = fn.stats(counts84h,0.128,True)[1]
    sum_counts[14] = fn.stats(counts9,0.1,True)[1]
    sum_counts[15] = fn.stats(counts98h,0.016,True)[1]
    sum_counts[16] = fn.stats(counts10,0.05,True)[1]
    
    #%% Radiation Sheilding Plot
    #This plots Counts vs Distance from the overall count and its respecitve distance. 
    #We also fixed a scaled inverse square curve using arbitrary data and had them on both the same graph. 
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
    #This section plots the counts vs time for each trial, which is what we had originally gotten on loggerpro during the lab.
    #This section is based off the function plot_counts defined in functions.py
    
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
    fn.plot_counts(time1h,counts1h,0.792)
    fn.plot_counts(time19h,counts19h,0.648)
    fn.plot_counts(time37h,counts37h,0.504)
    fn.plot_counts(time55h,counts55h,0.36)
    fn.plot_counts(time69h,counts69h,0.248)
    fn.plot_counts(time84h,counts84h,0.128)
    fn.plot_counts(time98h,counts98h,0.016)

    #%% Calculating the Intensity of Radioactive Decay
    
    #This part of the code begins working towards approximating the area of the detector.
    #Basing off of how accurate these calculations would be, from the uncertainty values we had calculated from the stats function,
    #we decided to truncate much of the values since we cannot trust that many decimal places from these approximations.
    #We first start off by defining an array to store counts per second values, and then calcualte the rate of decay and store 
    #into the array.

    intensity_array = np.zeros(17)
    int1 = sum(counts1) / sum(time1)
    int2 = sum(counts2) / sum(time2)
    int3 = sum(counts3) / sum(time3)
    int4 = sum(counts4) / sum(time4)
    int5 = sum(counts5) / sum(time5)
    int6 = sum(counts6) / sum(time6)
    int7 = sum(counts7) / sum(time7)
    int8 = sum(counts8) / sum(time8)
    int9 = sum(counts9) / sum(time9)
    int10 = sum(counts10) / sum(time10)
    int11 = sum(counts1h)/sum(time1h)
    int12 = sum(counts19h)/sum(time19h)
    int13 = sum(counts37h)/sum(time37h)
    int14 = sum(counts55h)/sum(time55h)
    int15 = sum(counts69h)/sum(time69h)
    int16 = sum(counts84h)/sum(time84h)
    int17 = sum(counts98h)/sum(time98h)

    #These two parts are really the same parts of the code, we define the Intensity array, based on multiple divisions.
    #In order to accomodate the machine error, we truncated much of the decimal places when storing into the array.
    
    intensity_array[0] = float(f"{int1:.2f}")
    intensity_array[1] = float(f"{int2:.2f}")
    intensity_array[2] = float(f"{int3:.6f}")
    intensity_array[3] = float(f"{int4:.2f}")
    intensity_array[4] = float(f"{int5:.2f}")
    intensity_array[5] = float(f"{int6:.2f}")
    intensity_array[6] = float(f"{int7:.4f}")
    intensity_array[7] = float(f"{int8:.4f}")
    intensity_array[8] = float(f"{int9:.4f}")
    intensity_array[9] = float(f"{int10:.6f}")
    intensity_array[10] = float(f"{int11:.6f}")
    intensity_array[11] = int12
    intensity_array[12] = int13
    intensity_array[13] = int14
    intensity_array[14] = int15
    intensity_array[15] = int16
    intensity_array[16] = int17
    
    #%% Intensity vs Inverse Square Fitting
    #In order to obtain our constant, S, we defined the inverse_sqr variable using the data.
    inverse_sqr = 1 / (distance**2)
    #After creating the inverse square data, we then curve fit to get the slope between Intensity and 1/r^2
    int_fit, int_cov = curve_fit(fn.lin_curve, intensity_array, inverse_sqr)
     
    #We then plot the Intensity vs 1/r^2
    #We decided not to include the fitted curve because there was one value that skewed a bit of the data. 
    plt.figure(2)
    plt.figure(figsize=(7,5))
    plt.scatter(intensity_array, inverse_sqr, label='Strength')
    #plt.plot(intensity_array, fn.lin_curve(intensity_array, int_fit[1],int_fit[0]), label='Fitted Curve')
    plt.title("Plotting Intensity vs Inverse Square")
    plt.xlabel("Intensity (C/s)")
    plt.ylabel("1 / r^2")
    plt.legend()
    plt.grid()
    plt.show()
    
    #%% Approximating the area of the Detector
    #In order to find the detector, we need the slope of the intensity vs inverse sqr plot.
    #We accomplish this by indexing the curve_fitting calculation, and multiplying by 4pi.
    #Then, we redefine the intensity_array as a different variable to be more concise. 
    S = float(f"{(int_fit[0] *(4) * np.pi):.2f}")
    C = intensity_array
    
    #After obbtaining our values, we then define an array to store the area calculations. 
    areal = np.zeros(17)
    #Then, for the first 10 values, which are the farthest away, we input our 1/12 method into calculating the area
    #And then we truncate to 6 or 8 decimal places depending on the distance. 
    
    for kj in range(10):
        areal[kj] = (C[kj]) *(distance[kj]**2) / 12
        areal[kj] = float(f'{areal[kj]:.6f}')
        
    for kj in range(10,17):
        areal[kj] = (C[kj]) * (distance[kj]**2) / 3
        areal[kj] = float(f'{areal[kj]:.8f}')
        
    #After all of the values are stored, we then multiply into the array all of the constant values.
    #We also determine the uncertainty from the standard deviation
    areal *= (4*np.pi)/S
    d_error = np.std(areal)
    
    #These prints then print the final results. 
    print(f"The Approximate Area of the Detector is: {((sum(areal))*(10000)):.3f} cm^2")
    print(f"The error in this approximation is: +/- {(d_error*10000):.2f} cm^2")
    
"""Physics 346 Advanced Lab 3 - Lab 6

Author: Ricky Gonzales
Version: May 9th, 2024

This code is built to accomodate the Radiation Lab. 
"""

#%% Modules

import numpy as np
import functions as fn
from lmfit import Model, Parameters

#%% Main

#We first define our section for the main series of computations.
if __name__ == "__main__":
            
    #%% Background Radation
    
    #One of the first arrays that we will add is the one that corresponds to the background radiation in 2378. 
    #This array is important to acquire in order to calculate the true number of radiation counts for each subsequent array.
    
    timebg, countsbg = np.genfromtxt("background.csv",delimiter=',', skip_header=1, unpack=True)
    
    #%% Group 2's Data-sets
    
    #Next we bring in our first set of data (or actually second).
    #This group used the ring-stand for their setup with a collection sereis of 0.01 seconds for each trial. 
    #Each of these are text files, so the following lines look pretty redudant. 
    
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
    
    #After we have imported our measured data, we then use our background radiation data-set to strip down the number of counts for
    #each trial.
    #This is accomplished using the true_counts function, where it averages the background radiation and subtracts each element
    #in each of the radiation counts arrays by that average. 
    
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
    
    #Following along with our radiation data, we then build our distance values array using the measurements that
    #group 2 had made for each trial.
    #The units of this array are in meters, and are ordered from top down.
    
    g2d = np.zeros(10)
    
    g2d[0],g2d[1],g2d[2],g2d[3],g2d[4],g2d[5],g2d[6],g2d[7],g2d[8],g2d[9] = 0.7,0.6,0.5,0.4,0.3,0.25,0.2,0.15,0.1,0.05
    
    #%% Group 2 Activity (Counts per Second)
    
    #After all of our data has been imported and we define our distance array, we then build our activity array in order
    #to obtain the counts per second for this data-set. 
    #We start off by defining an array and then summing all corresponding arrays and dividing the counts by time. 
    g2I = np.zeros(10)
    
    g2I[0] = sum(counts1) / sum(time1)
    g2I[1] = sum(counts2) / sum(time2)
    g2I[2] = sum(counts3) / sum(time3)
    g2I[3] = sum(counts4) / sum(time4)
    g2I[4] = sum(counts5) / sum(time5)
    g2I[5] = sum(counts6) / sum(time6)
    g2I[6] = sum(counts7) / sum(time7)
    g2I[7] = sum(counts8) / sum(time8)
    g2I[8] = sum(counts9) / sum(time9)
    g2I[9] = sum(counts10) / sum(time10)
    
    #%% Summation of all Counts per trial
    
    #In order to be able to plot the relationship between the number of counts and the distance in order to view
    #the inverse square law trend, we build our radiaiton counts array by summing all values and inputting them into the 
    #corresponding array.
    #This step depended heavily on the stats function in functions.py, where it calculates the uncertainty from Poissons
    #Distribution and obviously, the summation of the radiation counts array.
    #In order to view excessive printing in the python kernel, we set the printing condition as False.
    
    sum_counts2 = np.zeros(10)
    
    sum_counts2[0] = fn.stats(counts1,0.7,False)[1]
    sum_counts2[1] = fn.stats(counts2,0.6,False)[1]
    sum_counts2[2] = fn.stats(counts3,0.5,False)[1]
    sum_counts2[3] = fn.stats(counts4,0.4,False)[1]
    sum_counts2[4] = fn.stats(counts5,0.3,False)[1]
    sum_counts2[5] = fn.stats(counts6,0.25,False)[1]
    sum_counts2[6] = fn.stats(counts7,0.2,False)[1]
    sum_counts2[7] = fn.stats(counts8,0.15,False)[1]
    sum_counts2[8] = fn.stats(counts9,0.1,False)[1]
    sum_counts2[9] = fn.stats(counts10,0.05,False)[1]
    
    #%% Plotting Group 2 Data
    
    #In order to gain a sense for what the counts vs distance data looks like, we plot them using matplotlib.pyplot.
    #The function plot_counts was built in order to accomodate for the redudancy in making multiple branches in order to graph trends.
    fn.plot_counts(g2d,sum_counts2,2)
    
    #%% Group 1's Data-sets
    
    #After all of group 2's data has been imported and organized, we then conduct the same process using the data-sets from 
    #group 1, which included the LEGO stand setup. 
    #In order to avoid redudancy in commenting code, this process works exactly the same as the information for group 2's data.
    
    time1h, counts1h = np.genfromtxt("measurement_1_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    time19h, counts19h = np.genfromtxt("measurement_19_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    time37h, counts37h = np.genfromtxt("measurement_37_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    time55h, counts55h = np.genfromtxt("measurement_55_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    time69h, counts69h = np.genfromtxt("measurement_69_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    time84h, counts84h = np.genfromtxt("measurement_84_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    time98h, counts98h = np.genfromtxt("measurement_98_holedown.csv",delimiter=',', skip_header=7, unpack=True)
    
    counts1h = fn.true_counts(counts1h,countsbg)
    counts19h = fn.true_counts(counts19h,countsbg)
    counts37h = fn.true_counts(counts37h,countsbg)
    counts55h = fn.true_counts(counts55h,countsbg)
    counts69h = fn.true_counts(counts69h,countsbg)
    counts84h = fn.true_counts(counts84h,countsbg)
    counts98h = fn.true_counts(counts98h,countsbg)
    
    g1d = np.zeros(7)
    
    g1d[0],g1d[1],g1d[2],g1d[3],g1d[4],g1d[5],g1d[6] = 0.792,0.648,0.504,0.36,0.248,0.128,0.016
    
    #%% Group 1 Activity (Counts per Second)
    
    g1I = np.zeros(7)
    
    g1I[0] = sum(counts1h) / sum(time1h)
    g1I[1] = sum(counts19h) / sum(time19h)
    g1I[2] = sum(counts37h) / sum(time37h)
    g1I[3] = sum(counts55h) / sum(time55h)
    g1I[4] = sum(counts69h) / sum(time69h)
    g1I[5] = sum(counts84h) / sum(time84h)
    g1I[6] = sum(counts98h) / sum(time98h)
    
    #%% Summation of all Counts per Trial
    sum_counts1 = np.zeros(7)
    
    sum_counts1[0] = fn.stats(counts1h,0.792,False)[1]
    sum_counts1[1] = fn.stats(counts19h,0.648,False)[1]
    sum_counts1[2] = fn.stats(counts37h,0.504,False)[1]
    sum_counts1[3] = fn.stats(counts55h,0.36,False)[1]
    sum_counts1[4] = fn.stats(counts69h,0.248,False)[1]
    sum_counts1[5] = fn.stats(counts84h,0.128,False)[1]
    sum_counts1[6] = fn.stats(counts98h,0.016,False)[1]

    #%% Plotting Group 1 Data
    
    fn.plot_counts(g1d,sum_counts1,1)

#%% Transition
    #%% Initialize Model
    
    #With all of our data imported and organized, we then work towards using a model to approximate the area of the detector. 
    #From functions.py, we created a function that calculates the strength of a radioactive source, which depends on
    #the intensity, distance, and the Area.
    #Since we are trying to solve for area, this was the obvious function to use. 
    #From our importation of lmfit, we create a model out of our strength equation.
    model = Model(fn.strength,independent_vars=['I','r']) 
    #Following the creation of our model, we then build our parameters or, our initial guesses, for this 
    #Non-Linear Least Squares method.
    params = Parameters()
    #Since we are only approximating one value, we initialize it with our initial guess, which must be of the order of 10E-5. 
    params.add('A',value=0.0001)
    
    #%% Group 1 Data Fit using lmfit

    #With our model created, we then fit group 1's data to this model in order to extract its approximation of the area
    #Keep in mind that ALL of these approximations are in standard units, so the area will initially be in m^2. 
    #Since we have defined our independent variables, we must include them into our fit call.
    fit1 = model.fit(sum_counts1, params,I=g1I,r=g1d)
    
    #Following our fitting of group 1's data, we then print the best values along with the uncertainties associated
    #with this approximation. 
    print(f"{fit1.best_values}\n\n")
    print(f"{fit1.fit_report()}\n\n")
    
    #%% Group 2 Data Fit using lmfit
    
    #The same process was conducted for group 2's data. 
    fit2 = model.fit(sum_counts2, params,I=g2I,r=g2d)
    print(f"{fit2.best_values}\n\n")
    print(f"{fit2.fit_report()}\n\n")
    
    
    #%% Obtaining Best Values
    
    #After iterating through our model in seeking to minimize the Strength of the radioactive source, we then obtain
    #an approximation of the area of the detector. 
    #We extract these area values from each respecitve fit, and multiply by 10,000 to get it into cm^2. 
    area1 = (fit1.best_values['A'] ) * 10000
    area2 = (fit2.best_values['A'] ) * 10000
    
    #With our area values extracted, we then create an array for the associated errors.
    #These errors were read in from what the fitting model returns, by reading what it displayed in the python kernel
    errors = np.zeros(2)
    errors[0], errors[1] = 4.0020E-5, 6.4729E-4
    #After adding to our array, we transfer it to cm^2. 
    total_error = np.average(errors * 10000)
    
    #With our area values extracted, we create an array to store and average. 
    area = np.zeros(2)
    area[0], area[1] = area1, area2
    total_area = np.average(area)
    
    #With our calcualtions complete, we then print to the user our Approximation of the Area of the Detector. 
    print(f"The approximated area of the detector is: {total_area:.5f} cm^2")
    print(f"The error in this approximation is: +/- {total_error:.5f} cm^2")
    
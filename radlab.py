"""Physics 346 Advanced Lab 3 - Lab 6

Author: Ricky Gonzales
Version: May 9th, 2024

This code is built to accomodate the Radiation Lab. 
"""


import numpy as np
import functions as fn
import matplotlib.pyplot as plt
#from lmfit.models import ExponentialModel
from lmfit import Model


if __name__ == "__main__":
        
    #Import Data, Radiation Counts and Time
    
    #Background Radation
    timebg, countsbg = np.genfromtxt("background.csv",delimiter=',', skip_header=1, unpack=True)
    
    #Group 2's Data-sets
    
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

    g2d = np.zeros(10)
    
    g2d[0],g2d[1],g2d[2],g2d[3],g2d[4],g2d[5],g2d[6],g2d[7],g2d[8],g2d[9] = 0.7,0.6,0.5,0.4,0.3,0.25,0.2,0.15,0.1,0.05
    
    #Group 2 Activity (Counts per Second)
    
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

    
    #Group 1's Data-sets
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
    
    #Group 1 Activity (Counts per Second)
    
    g1I = np.zeros(7)
    
    g1I[0] = sum(counts1h) / sum(time1h)
    g1I[1] = sum(counts19h) / sum(time19h)
    g1I[2] = sum(counts37h) / sum(time37h)
    g1I[3] = sum(counts55h) / sum(time55h)
    g1I[4] = sum(counts69h) / sum(time69h)
    g1I[5] = sum(counts84h) / sum(time84h)
    g1I[6] = sum(counts98h) / sum(time98h)

    
    #%% Group 1 Data Fit
    
    sum_counts1 = np.zeros(7)
    
    sum_counts1[0] = fn.stats(counts1h,0.792,False)[1]
    sum_counts1[1] = fn.stats(counts19h,0.648,False)[1]
    sum_counts1[2] = fn.stats(counts37h,0.504,False)[1]
    sum_counts1[3] = fn.stats(counts55h,0.36,False)[1]
    sum_counts1[4] = fn.stats(counts69h,0.248,False)[1]
    sum_counts1[5] = fn.stats(counts84h,0.128,False)[1]
    sum_counts1[6] = fn.stats(counts98h,0.016,False)[1]
    
    model1 = Model(fn.strength)
    fit1 = model1.fit(sum_counts1,x=g1d,g1I,0.001)
    print(f"{fit1.best_values}\n\n")
    print(f"{fit1.fit_report()}\n\n")
    
    #%% Group 2 Data Fit
    
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
    
    model2 = Model(fn.strength)
    fit2 = model2.fit(sum_counts2,x=g2d,g2I,0.001)
    print(f"{fit2.best_values}\n\n")
    print(f"{fit2.fit_report()}\n\n")
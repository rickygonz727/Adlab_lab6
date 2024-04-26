"""Code for the Radiation Lab - Adlab Lab 6

Authors: Ad-Lab 3 Spring 24 Semester
Version" April 19th, 2024

"""

import numpy as np
import functions as fn
import matplotlib.pyplot as plt


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


if __name__ == "__main__":
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
    
    lambdas = np.zeros(10)
    lambdas[0] = fn.decay_const(time1, counts1)
    lambdas[1] = fn.decay_const(time2, counts2)
    lambdas[2] = fn.decay_const(time3, counts3)
    lambdas[3] = fn.decay_const(time4, counts4)
    lambdas[4] = fn.decay_const(time5, counts5)
    lambdas[5] = fn.decay_const(time6, counts6)
    lambdas[6] = fn.decay_const(time7, counts7)
    lambdas[7] = fn.decay_const(time8, counts8)
    lambdas[8] = fn.decay_const(time9, counts9)
    lambdas[9] = fn.decay_const(time10, counts10)
    
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


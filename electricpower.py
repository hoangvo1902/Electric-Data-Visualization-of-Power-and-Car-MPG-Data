# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


############################## Your code for loading and preprocess the data ##
df = pd.read_table('household_power_consumption.txt', sep=';', low_memory=False)
# Preprocessing by making datetime has the value
df['datetime'] = df['Date'] + ' ' + df['Time']   
df.datetime = pd.to_datetime(df.datetime, infer_datetime_format=True)
# Preprocessing by replacing missing value by 0 index
df = df.replace({'?': 0}) 
# Transform Global_active_power from string type to numeric type
df['Global_active_power'] = df['Global_active_power'].apply(lambda x: pd.to_numeric(x, errors='coerce'))
# Transform Global_reactive_power from string type to numeric type
df['Global_reactive_power'] = df['Global_reactive_power'].apply(lambda x: pd.to_numeric(x, errors='coerce'))
# Transform Voltage from string type to numeric type
df['Voltage'] = df['Voltage'].apply(lambda x: pd.to_numeric(x, errors='coerce'))
# Transform Sub_metering_1 from string type to numeric type
df['Sub_metering_1'] = df['Sub_metering_1'].apply(lambda x: pd.to_numeric(x, errors='coerce'))
# Transform Sub_metering_2 from string type to numeric type
df['Sub_metering_2'] = df['Sub_metering_2'].apply(lambda x: pd.to_numeric(x, errors='coerce'))
# Create a dataframe including the 2 researching date
data = df[df.Date.isin(['1/2/2007','2/2/2007'])]
data = data.set_index('datetime')
############################ Complete the following 4 functions ###############
def plot1():
    plt.hist(data['Global_active_power'], edgecolor='black', color='red', bins=np.arange(0, 8, 0.5));
    plt.ylabel("Frequency")
    plt.xlabel("Global Active Power (kilowatts)")
    plt.title(r"$\bf{Global\ active\ power}$")
    plt.xticks([0, 2, 4, 6]);
    plt.savefig('Plot1.png')
    # pass

def plot2():
    fig,ax1 = plt.subplots()
    data['Global_active_power'].plot(ax=ax1, color='black')
    ax1.set_xticklabels(['Thu','Fri','Sat'])
    ax1.set_ylabel('Global Active Power (kilowatts)')
    plt.savefig('Plot2.png')
    # pass

def plot3():
    fig,ax = plt.subplots()
    data['Sub_metering_1'].plot(color='black',ax=ax)
    data['Sub_metering_2'].plot(color='red',ax=ax)
    data['Sub_metering_3'].plot(color='blue',ax=ax)
    ax.set_xticklabels(['','Thu','','Fri','','Sat',''])
    plt.legend()
    plt.ylabel('Energy sub metering')
    plt.savefig('Plot3.png')
    # pass



def plot4():
    fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(14,6))

    # Plot a
    data['Global_active_power'].plot(ax=ax1, color='black')
    ax1.set_xticklabels(['Thu','Fri','Sat'])
    ax1.set_ylabel('Global active power')

    # Plot b
    data['Voltage'].plot(ax=ax2, color='black')
    ax2.set_xticklabels(['Thu','Fri','Sat'])
    ax2.set_ylabel('Voltage')

    # Plot c
    data['Sub_metering_1'].plot(color='black',ax=ax3)
    data['Sub_metering_2'].plot(color='red',ax=ax3)
    data['Sub_metering_3'].plot(color='blue',ax=ax3)
    ax3.set_xticklabels(['Thu','Fri','Sat'])
    ax3.set_ylabel('Energy sub metering')
    ax3.legend()

    # Plot d
    data['Global_reactive_power'].plot(ax=ax4, color='black')
    ax4.set_xticklabels(['Thu','Fri','Sat'])
    ax4.set_ylabel('Global_reactive_power')
    plt.tight_layout()
    plt.savefig('Plot4.png')
    # pass
    
plot1()
plot2()
plot3()
plot4()

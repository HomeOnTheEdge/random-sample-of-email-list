#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:56:35 2019

@author: John D. Evans

Is there a way to integrate prior work in 'firststeps.py' and SQL
into this one file? Might be worthwhile for the skills-dev
"""
import datetime
import time
import os
import pandas as pd
import glob
import numpy as np
from random import sample

filename = 'AMh2o_HIST.csv'

def import_am_water_HIST(filename=filename):             #  https://stackoverflow.com/a/36416258
    ## SET UP
    time_start = datetime.datetime.now()
    header = [
        "County_Code",
        "Voter_ID",
        "Election_Date",
        "Election_Type",
        "History_Code"]
    print('Reading file: ' + filename + '\n'
          + 'Time start: ' + str(datetime.datetime.now()))

    path = '/Users/smginterns/Desktop/'                     # use your path

    ## MAIN
    am_water_HIST = pd.read_csv(path+filename, sep=',', header=0, dtype=str) #Importing file
    # Data cleaning: Dates into machine readable format
    am_water_HIST['Election_Date'] = \
        pd.to_datetime(am_water_HIST['Election_Date'], format='%m/%d/%Y')

    ## SANITY CHECKS
    print('\n\n'+str(filename)+'.info')
    print(am_water_HIST.info())

    print('\n\n'+str(filename)+'.head')
    print(am_water_HIST.head())

    time_end = datetime.datetime.now()
    time_execute = time_end - time_start
    print('\n\nDone! ' + 'Time end: ' + str(datetime.datetime.now()))
    print('Time elapsed: ' + str(time_execute))

    ## end the function, and return the dataframe
    return am_water_HIST

#%%



def explore(df):
    '''output a list of stats of an input dataframe'''
    print("\nPrinting first ten rows:")
    print(df.head(10))
    print("\nRows per county:")
    print(df['County_Code'].value_counts())
    print("\nNumber of unique Voter ID's:")
    print(df['Voter_ID'].nunique())
    print("\nNumber of rows per year:")
    # .value_counts(sort=False) sorts by YEAR instead of by FREQUENCY!
    print(df['Election_Date'].dt.year.value_counts(sort=False))
    print("\nNumber of rows per election type:")
    print(df['Election_Type'].value_counts())
    print("\nNumber of rows per vote type:")
    print(df['History_Code'].value_counts())
    #Instead of printing, I might output these to dfs or dicts all their own

# HOW TO DROP: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
    # https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
def drop_stuff(df, earliest_year=2014, minimum_votes=7):
    '''Slicing up the voter history file to find SuperVoters. DEFAULTS: earliest_year = 2014, minimum_votes = 7'''
    df['Year'] = df['Election_Date'].dt.year
    # building an index of years to be dropped
    dropping_years = df[df['Year'] < earliest_year].index
    # dropping those years
    SV = df.drop(dropping_years)
    #doing same for frequency of votes per voter
    SV['Freq'] = SV.groupby('Voter_ID')['Voter_ID'].transform('size')
    dropping_freq = SV[SV['Freq'] < minimum_votes].index
    SV = SV.drop(dropping_freq)    
    # This counts the number of times a Voter ID appears,
    # and puts that number in a new column called 'Freq' for each row.
    # this can be used to find the supervoters
    print("\nNumber of voters per number of times voted:")
    print(SV['Freq'].value_counts(sort=False))
    return SV

## Consider dropping:
    # YEARS prior to (less than) 2014
    # History_Code == 'N'
    # Are there election types that are droppable?
    # IMPORTANT NOTE: The list will further reduce when we consider \
        # the intersection between Voter_ID's that also have emails. \
        # but we don't have to worry about this for now.
def output_supervoter_ids(df):
    supervoters_5_2014_7 = df.Voter_ID.unique()
    np.savetxt("supervoters_5_2014_7.txt",supervoters_5_2014_7,delimiter=',', fmt='%s')
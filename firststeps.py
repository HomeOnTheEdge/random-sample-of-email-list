#%% Introduction
# -*- coding: utf-8 -*-

#In the latest version (1.36) of VS Code (Python):
#CTRL+A then hit SHIFT+Enter to run your code in interactive IPython Shell.

#%% Importing packages
import datetime
time_00 = datetime.datetime.now()
import time
import os
import pandas as pd
import glob
import numpy as np
from random import sample

# some of this code can be cleaned up - like the convenience functions - 
## Import Python Script Into Another:
##       https://stackoverflow.com/questions/15696461/import-python-script-into-another
## Main takeaway: You can import other python scripts
## as if they were just another package IF
## they are in the same directory as your current script
## SEE ALSO: https://scipy-lectures.org/intro/language/reusing_code.html

#%% Declaring variables and functions
date_voterfile = str(20191008)
path_voterfile = str(
    '/Users/smginterns/Documents/Voter File/'
    + date_voterfile+'_VoterDetail/') 
list_voterfiles = os.listdir(path=path_voterfile)
outputdir = str("/Users/smginterns/Desktop/Python code/!OUTPUT/")
sample_size = 20000
slice_size = 5000
county_single = "GLA"
county_path = str(
    "/Users/smginterns/Documents/Voter File/"
    + date_voterfile+"_VoterDetail/"
    + county_single+"_"+date_voterfile+".txt")
header_voterfile = [
    "County_Code", 
    "Voter_ID", 
    "Name_Last", 
    "Name_Suffix",
    "Name_First",
    "Name_Middle",
    "Requested_public_records_exemption",
    "Residence_Address_Line_1",
    "Residence_Address_Line_2",
    "Residence_City_(USPS)",
    "Residence_State",
    "Residence_Zipcode",
    "Mailing_Line_1",
    "Mailing_Line_2",
    "Mailing_Line_3",
    "Mailing_City",
    "Mailing_State",
    "Mailing_Zipcode",
    "Mailing_Country",
    "Gender",
    "Race",
    "Birth_Date",
    "Registration_Date",
    "Party_Affiliation",
    "Precinct",
    "Precinct_Group",
    "Precinct_Split",
    "Precinct_Suffix",
    "Voter_Status",
    "Congressional_District",
    "House_District",
    "Senate_District",
    "County_Commission_District",
    "School_Board_District",
    "Daytime_Area_Code",
    "Daytime_Phone_Number",
    "Daytime_Phone_Extension",
    "Email_Address"
    ]
lookup_sachsregions = {    # Dictionaries can be used analogously to vlookup tables!
    'ALA':'North Central',
    'BAK':'North East',
    'BAY':'North West',
    'BRA':'North East',
    'BRE':'Central East',
    'BRO':'South East',
    'CAL':'North West',
    'CHA':'South West',
    'CIT':'North Central',
    'CLA':'North East',
    'CLL':'South West',
    'CLM':'North Central',
    'DAD':'South East',
    'DES':'Central West',
    'DIX':'North Central',
    'DUV':'North East',
    'ESC':'North West',
    'FLA':'North East',
    'FRA':'North West',
    'GAD':'North West',
    'GIL':'North Central',
    'GLA':'South West',
    'GUL':'North West',
    'HAM':'North Central',
    'HAR':'Central West',
    'HEN':'South West',
    'HER':'Central West',
    'HIG':'Central West',
    'HIL':'Central West',
    'HOL':'North West',
    'IND':'Central East',
    'JAC':'North West',
    'JEF':'North West',
    'LAF':'North Central',
    'LAK':'Central East',
    'LEE':'South West',
    'LEO':'North West',
    'LEV':'North Central',
    'LIB':'North West',
    'MAD':'North Central',
    'MAN':'Central West',
    'MRN':'North Central',
    'MRT':'Central East',
    'MON':'South East',
    'NAS':'North East',
    'OKA':'North West',
    'OKE':'Central East',
    'ORA':'Central East',
    'OSC':'Central East',
    'PAL':'South East',
    'PAS':'Central West',
    'PIN':'Central West',
    'POL':'Central West',
    'PUT':'North East',
    'SAN':'North West',
    'SAR':'Central West',
    'SEM':'Central East',
    'STJ':'North East',
    'STL':'Central East',
    'SUM':'Central West',
    'SUW':'North Central',
    'TAY':'North Central',
    'UNI':'North East',
    'VOL':'Central East',
    'WAK':'North West',
    'WAL':'North West',
    'WAS':'North West'
    }
lookup_county_code_to_name = {
   'ALA':'Alachua',
   'BAK':'Baker',
   'BAY':'Bay',
   'BRA':'Bradford',
   'BRE':'Brevard',
   'BRO':'Broward',
   'CAL':'Calhoun',
   'CHA':'Charlotte',
   'CIT':'Citrus',
   'CLA':'Clay',
   'CLL':'Collier',
   'CLM':'Columbia',
   'DAD':'Miami-Dade',
   'DES':'Desoto',
   'DIX':'Dixie',
   'DUV':'Duval',
   'ESC':'Escambia',
   'FLA':'Flagler',
   'FRA':'Franklin',
   'GAD':'Gadsden',
   'GIL':'Gilchrist',
   'GLA':'Glades',
   'GUL':'Gulf',
   'HAM':'Hamilton',
   'HAR':'Hardee',
   'HEN':'Hendry',
   'HER':'Hernando',
   'HIG':'Highlands',
   'HIL':'Hillsborough',
   'HOL':'Holmes',
   'IND':'Indian River',
   'JAC':'Jackson',
   'JEF':'Jefferson',
   'LAF':'Lafayette',
   'LAK':'Lake',
   'LEE':'Lee',
   'LEO':'Leon',
   'LEV':'Levy',
   'LIB':'Liberty',
   'MAD':'Madison',
   'MAN':'Manatee',
   'MRN':'Marion',
   'MRT':'Martin',
   'MON':'Monroe',
   'NAS':'Nassau',
   'OKA':'Okaloosa',
   'OKE':'Okeechobee',
   'ORA':'Orange',
   'OSC':'Osceola',
   'PAL':'Palm Beach',
   'PAS':'Pasco',
   'PIN':'Pinellas',
   'POL':'Polk',
   'PUT':'Putnam',
   'SAN':'Santarosa',
   'SAR':'Sarasota',
   'SEM':'Seminole',
   'STJ':'St. Johns',
   'STL':'St Lucie',
   'SUM':'Sumter',
   'SUW':'Suwannee',
   'TAY':'Taylor',
   'UNI':'Union',
   'VOL':'Volusia',
   'WAK':'Wakulla',
   'WAL':'Walton',
   'WAS':'Washington'
   }
countyinfodf = pd.DataFrame({
        "Abbrev" : ['ALA' ,'BAK' ,'BAY' ,'BRA' ,'BRE' ,'BRO' ,'CAL' ,'CHA' ,'CIT' ,'CLA' ,'CLL' ,'CLM' ,'DAD' ,'DES' ,'DIX' ,'DUV' ,'ESC' ,'FLA' ,'FRA' ,'GAD' ,'GIL' ,'GLA' ,'GUL' ,'HAM' ,'HAR' ,'HEN' ,'HER' ,'HIG' ,'HIL' ,'HOL' ,'IND' ,'JAC' ,'JEF' ,'LAF' ,'LAK' ,'LEE' ,'LEO' ,'LEV' ,'LIB' ,'MAD' ,'MAN' ,'MRN' ,'MRT' ,'MON' ,'NAS' ,'OKA' ,'OKE' ,'ORA' ,'OSC' ,'PAL' ,'PAS' ,'PIN' ,'POL' ,'PUT' ,'SAN' ,'SAR' ,'SEM' ,'STJ' ,'STL' ,'SUM' ,'SUW' ,'TAY' ,'UNI' ,'VOL' ,'WAK' ,'WAL' ,'WAS'],
        "County" : ['Alachua' ,'Baker' ,'Bay' ,'Bradford' ,'Brevard' ,'Broward' ,'Calhoun' ,'Charlotte' ,'Citrus' ,'Clay' ,'Collier' ,'Columbia' ,'Miami-Dade' ,'Desoto' ,'Dixie' ,'Duval' ,'Escambia' ,'Flagler' ,'Franklin' ,'Gadsden' ,'Gilchrist' ,'Glades' ,'Gulf' ,'Hamilton' ,'Hardee' ,'Hendry' ,'Hernando' ,'Highlands' ,'Hillsborough' ,'Holmes' ,'Indian River' ,'Jackson' ,'Jefferson' ,'Lafayette' ,'Lake' ,'Lee' ,'Leon' ,'Levy' ,'Liberty' ,'Madison' ,'Manatee' ,'Marion' ,'Martin' ,'Monroe' ,'Nassau' ,'Okaloosa' ,'Okeechobee' ,'Orange' ,'Osceola' ,'Palm Beach' ,'Pasco' ,'Pinellas' ,'Polk' ,'Putnam' ,'Santarosa' ,'Sarasota' ,'Seminole' ,'St. Johns' ,'St Lucie' ,'Sumter' ,'Suwannee' ,'Taylor' ,'Union' ,'Volusia' ,'Wakulla' ,'Walton' ,'Washington'],
        "Sachs Region" : ['North Central' ,'North East' ,'North West' ,'North East' ,'Central East' ,'South East' ,'North West' ,'South West' ,'North Central' ,'North East' ,'South West' ,'North Central' ,'South East' ,'Central West' ,'North Central' ,'North East' ,'North West' ,'North East' ,'North West' ,'North West' ,'North Central' ,'South West' ,'North West' ,'North Central' ,'Central West' ,'South West' ,'Central West' ,'Central West' ,'Central West' ,'North West' ,'Central East' ,'North West' ,'North West' ,'North Central' ,'Central East' ,'South West' ,'North West' ,'North Central' ,'North West' ,'North Central' ,'Central West' ,'North Central' ,'Central East' ,'South East' ,'North East' ,'North West' ,'Central East' ,'Central East' ,'Central East' ,'South East' ,'Central West' ,'Central West' ,'Central West' ,'North East' ,'North West' ,'Central West' ,'Central East' ,'North East' ,'Central East' ,'Central West' ,'North Central' ,'North Central' ,'North East' ,'Central East' ,'North West' ,'North West' ,'North West']})

lookup_race = {
    '1':'Other',                # VF code for 'American Indian or Alaskan Native'. SMG chooses to code these respondents as 'Other'
    '2':'Other',                # VF code for 'Asian or Pacific Islander'. SMG chooses to code these respondents as 'Other'
    '3':'Black',                # VF code for 'Black, not Hispanic'
    '4':'Hispanic',             # VF code for 'Hispanic'
    '5':'White, Not Hispanic',  # VF code for 'White, not Hispanic'
    '6':'Other',                # VF code for 'Other'
    '7':'Black',                # VF code for 'Multi-racial'. SMG chooses to code these respondents as 'Black'
    '9':'Other'                 # VF code for 'Unknown'. SMG chooses to code these respondents as 'Other'
    } #there is no '8' race code

def global_variables():
    global date_voterfile
    global path_voterfile
    global county_single
    global county_path
    date_voterfile = input(str("Please input the DATE of the voterfile (default = " + date_voterfile + ") : "))
    path_voterfile = str('/Users/smginterns/Documents/Voter File/' + date_voterfile+'_VoterDetail/')
    county_single = input(str("If you wish to test a single county, which one? \n\t"
                               + "(expected: three capital letters) \n\t" 
                               + "(default = " + county_single + ") \n\t"
                               +"\t\t\t\t\t INPUT > : "))
    county_path = str(
        "/Users/smginterns/Documents/Voter File/"
        + date_voterfile+"_VoterDetail/"
        + county_single+"_"+date_voterfile+".txt")

def whereami():
    print("Current working directory: ", os.getcwd())

def GOTOvoterfile():
    os.chdir("/Users/smginterns/Documents/Voter File/20190910_VoterDetail/")
    
def GOTOpythoncode():
    os.chdir("/Users/smginterns/Desktop/Python code")

def SHOWwhatsinside():
    print(os.listdir(path='.'))
    
def SHOWvoterfiles():
    return os.listdir(
        path='/Users/smginterns/Documents/Voter File/'
        + date_voterfile
        + '_VoterDetail/.')

def create_test_vf():   #setting up a test DataFrame for allvoterfiles
    global allvoterfiles
    allvoterfiles = pd.DataFrame({"col_1" : [1,1,1,1,2,2,2,2], 
                                  "col_2" : [2,3,1,4,5,6,7,2],
                                  "col_3" : [1,2,3,4,5,6,7,8]})

def extract_single_county_emails():
    """This will extract all entries in Glades county that have emails and export them as a .csv file."""
    time_start = datetime.datetime.now()
    print('Extracting emails from '+county_single+'_'+date_voterfile+' ...')
    df = pd.read_csv(county_path, 
                     sep='\t', 
                     header=None, 
                     names=header_voterfile, 
                     dtype=str, 
                     index_col='Voter_ID')
    email = df[df['Email_Address'].str.len()>2] #EMAIL SENSOR
    email.to_csv(outputdir+county_single+'_'+str(datetime.datetime.now())+'.csv') #EXPORT TO CSV

    time_end = datetime.datetime.now()
    time_execute = time_end - time_start
    print('Done! ' + 'Time end: ' + str(datetime.datetime.now()))
    print('Time elapsed: ' + str(time_execute))


def extract_emails():
    time_start = datetime.datetime.now()
    global allvoterfiles
    global allvoterfiles_emails
    allvoterfiles_emails = allvoterfiles[allvoterfiles['Email_Address'].str.len()>2] #EMAIL SENSOR
    time_end = datetime.datetime.now()
    time_execute = time_end - time_start
    print('Done! ' + 'Time end: ' + str(datetime.datetime.now()))
    print('Time elapsed: ' + str(time_execute))

def random_sample_emails():
    time_start = datetime.datetime.now()
    global allvoterfiles_emails, sample_size, slice_size, sampledf
    sampledf = allvoterfiles_emails.sample(n=sample_size)
    time_end = datetime.datetime.now()
    time_execute = time_end - time_start
    print('Done! ' + 'Time end: ' + str(datetime.datetime.now()))
    print('Time elapsed: ' + str(time_execute))






def prune_columns(x):
    '''Selects needed columns, drops the rest, and re-orders the remaining columns in an ideal fashion. '''
    x = x[['a','d']] # Select the ones you want -- https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas
    #build list of columns in the order you want


    

def import_all_voter_files():             #  https://stackoverflow.com/a/36416258
    """This will grab all voterfiles in the directory and hold them in RAM as a spreadsheet-like object called a DataFrame. WARNING: MEMORY-INTENSIVE!"""
    global allvoterfiles     ### DELETE THIS GLOBAL ONCE SAMPLE EXTRACTION / CSV EXPORT COMES ONLINE
    global time_execute_allvoterfiles
    print('Reading all voter files from disk: ' + date_voterfile + '\n'
          + 'Time start: ' + str(datetime.datetime.now()))
    time_start_allvoterfiles = datetime.datetime.now()

    path = path_voterfile                     # use your path
    all_files = glob.glob(os.path.join(path, "*.txt"))     # advisable to use os.path.join as this makes concatenation OS independent
    
    df_from_each_file = (pd.read_csv(f,
                                     sep='\t', 
                                     header=None, 
                                     names=header_voterfile, 
                                     dtype=str, 
                                     index_col='Voter_ID') for f in all_files)
    allvoterfiles = pd.concat(df_from_each_file, ignore_index=True) ### consider replacing with sample extraction & csv export functions?
    # doesn't create a list, nor does it append to one

    time_end_allvoterfiles = datetime.datetime.now()
    time_execute_allvoterfiles = time_end_allvoterfiles - time_start_allvoterfiles
    print('Done! ' + 'Time end: ' + str(datetime.datetime.now()))
    print('Time elapsed: ' + str(time_execute_allvoterfiles))

def readme():
    print('Function list:')   
    print('\n-  import_all_voter_files()' + '\n\t' + import_all_voter_files.__doc__)
#    print('\n-  menu()' + '\n\t' + menu.__doc__)

time_01 = datetime.datetime.now()
print('\nWelcome to the SMG Florida Voter-file handler!'
      + '\n' + 'The time is: ' + str(datetime.datetime.now())
      + '\n' + 'For help, type: readme()')

#%% MAIN
#def menu():
#    """Meant to be the main algorithm to extract a sample for our (semi)monthly Omnibus survey."""
#    #check if variable: allvoterfiles contains enough for a sample. Rows > 1M?
#    #if check is False, then execute the function: read_allvoterfiles()
#    #Then extract from allvoterfiles variable a SAMPLE sliced into SLICESIZE chunks
#    #output each sample-slice into .csv files
#    global sample_size
#    global slice_size
#    if len(allvoterfiles) > sample_size:
#        print("\n"
#              +" Sample size = " + str(sample_size) + "\n"
#              +" Slice size  = " + str(slice_size) + "\n"
#              +" Date of VF  = " + str(date_voterfile) + "\n")
#        do_sample = input("   CONTINUE? Y/N : ")
#        if do_sample == 'y':
#            print("Extracting sample, please wait...")
#            time.sleep(1.5)
#            print("Working...")
#            time.sleep(1.5)
#            print("DONE!")
#            time.sleep(0.666)
#        #extract sample
#    else:
#        print("ERROR! Data is smaller than sample! \n\n"
#                      +"Sample = " + str(sample_size)
#                      +", Data size = " + str(len(allvoterfiles)) + "\n\n"
#                      +"Re-extract sample?           type: r \n"
#                      +"Re-size sample to fit data?  type: s \n"
#                      +"Quit sample-extraction loop? type: q")
#        error = input("   TYPE : ")
#        if error == 'r':
#            print("Re-extracting sample! (please wait approx 4min) please retry when finished.")
#        elif error == 's':
#            sample_size = len(allvoterfiles)
#            time.sleep(0.25)
#            print("Re-sizing sample! Sample is now " + str(sample_size) + " please retry.")
#        else:
#            time.sleep(0.25)
#            print("Quitting sample extraction loop.")
#            #exit sample extraction loop



#I want to make the above user-friendly. Use below as a text-interactive menu
                #http://pythonfiddle.com/simple-text-menu-for-python/
                ##!/usr/bin/python
                ## Version 1
                ### Show menu ##
                #print (30 * '-')
                #print ("   M A I N - M E N U")
                #print (30 * '-')
                #print ("1. Backup")
                #print ("2. User management")
                #print ("3. Reboot the server")
                #print (30 * '-')
                # 
                ### Get input ###
                #choice = raw_input('Enter your choice [1-3] : ')
                # 
                #### Convert string to int type ##
                #choice = int(choice)
                # 
                #### Take action as per selected menu-option ###
                #if choice == 1:
                #        print ("Starting backup...")
                #elif choice == 2:
                #        print ("Starting user management...")
                #elif choice == 3:
                #        print ("Rebooting the server...")
                #else:    ## default ##
                #        print ("Invalid number. Try again...")








#%% TO-DO LIST
"""
ABOVE is the MINIMUM VIABLE PRODUCT for voter file email extraction    

TO DO:
    2) Build random-sample extractor
    3) Currently, the email-sensor only eliminates blank and '*' emails. Can we check for and eliminate improperly formatted emails?
        3a) searchfor : #EMAIL SENSOR
    4) Find a way to turn the code into a standalone program, that works in a VERY user friendly way, such that even an intern can extract a voter file sample.
        4a) Detecting the presence of the voter files, and building a path to them?
        4b) Customized sample/slice sizing?  
        4c) GUI?
    
    DONE (success)    
        1) Try bulk importing without regard to memory usage. Try to overload the computer.
            1a) Loop to iterate through voter files and concatenate them.
            1b) Even consider concatenating whole-files, and not just rows with emails, just to stress-test. Performance in this regard sets the stage for 538-type voter-history analysis.    
    

"""


#%% DOCUMENTATION:
"""
-------------------------------------------------------------------------------
The Data Dictionary for the Florida voter file as of 2019-11-06 is below:

    
    *** File Naming Convention ***
        File Type            Individual File Name       Zip File Name
        Voter Registration   CountyCode_YYYYMMDD.txt    Voter_Registration_YYYYMMDD.zip
        Voting History       CountyCode_H_YYYYMMDD.txt  Voter _History_YYYYMMDD.zip


    *** Voter Registration Extract File ***
        * Field Name *                      * Max Length *   * Valid Codes / Format *    * Protected Data (For voters who have requested public records exemption.) *
        1 County Code                          3               See Code Definition Table
        2 Voter ID                            10
        3 Name Last                           30                                           Y
        4 Name Suffix                          5                                           Y
        5 Name First                          30                                           Y
        6 Name Middle                         30                                           Y
        7 Requested public records exemption   1               N or Y (if Y, protected data not included)
        8 Residence Address Line 1            50                                           Y
        9 Residence Address Line 2            40                                           Y
        10 Residence City (USPS)               40                                           Y
        11 Residence State                      2               State Abbreviation          Y
        12 Residence Zipcode                   10                                           Y
        13 Mailing Address Line 1              40                                           Y
        14 Mailing Address Line 2              40                                           Y
        15 Mailing Address Line 3              40                                           Y
        16 Mailing City                        40                                           Y
        17 Mailing State                        2               State Abbreviation          Y
        18 Mailing Zipcode                     12                                           Y
        19 Mailing Country                     40                                           Y
        20 Gender                               1               “F” “M” or “U”
        21 Race                                 1               See Code Definition Table
        22 Birth Date                          10               MM/DD/YYYY                  Y
        23 Registration Date                   10               MM/DD/YYYY
        24 Party Affiliation                    3               See Code Definition Table
        25 Precinct                             6                                           Y
        26 Precinct Group                       3                                           Y
        27 Precinct Split                       6                                           Y
        28 Precinct Suffix                      3                                           Y
        29 Voter Status                         3               “ACT” – Active or “INA” – Inactive
        30 Congressional District               3                                           Y
        31 House District                       3                                           Y
        32 Senate District                      3                                           Y
        33 County Commission District           3                                           Y
        34 School Board District                2                                           Y
        35 Daytime Area Code                    3                                           Y
        36 Daytime Phone Number                 7                                           Y
        37 Daytime Phone Extension              4                                           Y
        38 Email address                      100                                           Y


    *** Race Codes ***
        * Race Code *   * Race Description *
        1              American Indian or Alaskan Native
        2              Asian or Pacific Islander
        3              Black, not Hispanic
        4              Hispanic
        5              White, not Hispanic
        6              Other
        7              Multi-racial
        9              Unknown
        NOTE: there is no '8' race code


    *** Political Parties Registered in Florida (as of October 2018) ***
        * Party Codes *     * Party Description *
        CPF                 Constitution Party of Florida
        DEM                 Florida Democratic Party
        ECO                 Ecology Party of Florida
        GRE                 Green Party of Florida
        IND                 Independent Party of Florida
        LPF                 Libertarian Party of Florida
        NPA                 No Party Affiliation
        PSL                 Party for Socialism and Liberation - Florida
        REF                 Reform Party of Florida
        REP                 Republican Party of Florida 

    *** County Codes to County Names ***
        * County Code *     * County *
        ALA                 Alachua
        BAK                 Baker
        BAY                 Bay
        BRA                 Bradford
        BRE                 Brevard
        BRO                 Broward
        CAL                 Calhoun
        CHA                 Charlotte
        CIT                 Citrus
        CLA                 Clay
        CLL                 Collier
        CLM                 Columbia
        DAD                 Miami-Dade
        DES                 Desoto
        DIX                 Dixie
        DUV                 Duval
        ESC                 Escambia
        FLA                 Flagler
        FRA                 Franklin
        GAD                 Gadsden
        GIL                 Gilchrist
        GLA                 Glades
        GUL                 Gulf
        HAM                 Hamilton
        HAR                 Hardee
        HEN                 Hendry
        HER                 Hernando
        HIG                 Highlands
        HIL                 Hillsborough
        HOL                 Holmes
        IND                 Indian River
        JAC                 Jackson
        JEF                 Jefferson
        LAF                 Lafayette
        LAK                 Lake
        LEE                 Lee
        LEO                 Leon
        LEV                 Levy
        LIB                 Liberty
        MAD                 Madison
        MAN                 Manatee
        MRN                 Marion
        MRT                 Martin
        MON                 Monroe
        NAS                 Nassau
        OKA                 Okaloosa
        OKE                 Okeechobee
        ORA                 Orange
        OSC                 Osceola
        PAL                 Palm Beach
        PAS                 Pasco
        PIN                 Pinellas
        POL                 Polk
        PUT                 Putnam
        SAN                 Santarosa
        SAR                 Sarasota
        SEM                 Seminole
        STJ                 St. Johns
        STL                 St Lucie
        SUM                 Sumter
        SUW                 Suwannee
        TAY                 Taylor
        UNI                 Union
        VOL                 Volusia
        WAK                 Wakulla
        WAL                 Walton
        WAS                 Washington
-------------------------------------------------------------------------------


"""

""" This program is intended to extract a random-sample of emails from the Florida voter file for use in email surveys. """
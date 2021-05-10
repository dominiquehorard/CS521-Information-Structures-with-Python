# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:44:00 2021

@author: Dom Horard
"""
#Import sys to exit program if the user does not want to continue
import sys

#Importing the Entry class from the Entry file
from Entry import Entry

user_date = 0
user_time = 0

"""
DATE & TIME VALIDATOR FUNCTION
"""
def is_validate_datetime(date,time):
    
    '''
    Parameters
    ----------
    str : user entered string

    Returns
    -------
    Boolean tuple of true or false values if invalid date/time
    None if valid or an error message string if invalid

    '''
    #Import sys to exit if needed
    import sys
    
    #Create lists that split the input based on the / and : characters    
    date_list = user_date.split('/')
    time_list = user_time.split(':')

    #Check if the date/time can't be seperated because of invalid character 
    #input
    if len(date_list) == 1 or len(time_list) == 1:
        print()
        print('Please enter a date seperated by \'/\',' +
              ' and time seperated by \':\'...Goodbye')
        sys.exit()
        
    #Keep track of the length of the month string the user entered
    month_length,day_length,year_length = 0,0,0
        
    #For loop to increment the value of the month, day, and year length counter
    for digit in date_list[0]:
            month_length += 1
    for digit in date_list[1]:
            day_length += 1
    for digit in date_list[2]:
            year_length += 1
        
    #Variables to keep track of the length of the HH,MM,SS string for time 
    #input
    hour_length, min_length = 0, 0
        
    #For loops to increment the value of the time variable counters, 
    #all values between the seperated by : will be 2 in length
    for digit in time_list[0]:
           hour_length += 1
    for digit in time_list[1]:
           min_length += 1

            
    #List to check if the user entered a month that is in this list and
    #has an invalid day date entered        
    mon_list_1 = ['01','03','05','07','08','10','12']
    mon_list_2 = ['04','06','09','11']
    leap_month = ['02']
        
    #Defining leap year as false by default, a check will be made later to turn 
    #it to true if it is a valid leap year date for february
    leap_year = False
        
    #Check if year is in leap year list later
    leap_year_list = []
    
    #for loop looks for values between 1000(inclusive) and 10000(exclusive)
    #and if the value's remainder is 0 when divided by for, not 0 when divided
    #by 100, or is when divided by 400 the value in that range is added to the 
    #end of the list as an int
    for year in range(1000, 10000):
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                leap_year_list.append(year)
        
    #Used later to check if the date was valid, default to true unless an 
    #entered date is invalid
    is_valid_date = True
        
    #Same as is_valid_date, but for time
    is_valid_time = True
    
    #Variable for valid date/time that will be used later to return true if
    #both values are valid
    valid_date_time = True
        
    '''
    ==========================================================================
            ****CHECK FOR VALID DATE****
    ==========================================================================
    '''
                
    #Check if the length of the first element in the date list, the month, 
    #is not equal 2, if it is grearter than 13, or equal to 0
    if month_length != 2 or int(date_list[0]) >= 13 \
        or int(date_list[0]) == 0:
                    
            is_valid_date = False
            print()
            print('Invalid: Months must be entered with leading zeros' +\
                  'from 01 to 12')
    #Check if the day length is 2 for valid dates        
    elif day_length != 2:
                   
            is_valid_date = False
            print()
            print('Invalid: Enter a valid day date with a leading 0')
            
    #Check if the day length is 2 for valid dates        
    elif year_length != 4:
                   
            is_valid_date = False
            print()
            print('Invalid: Enter a valid year date from 1000 to 9999')
                    
    #Else if check that the month is in the 31-day-month list, the day element
    #is not in the range of 1 to 31
    elif date_list[0] in mon_list_1 and int(date_list[1]) not\
        in range(1,32):
                        
            is_valid_date = False
            print()
            print('Invalid: This month needs between 1 and 31 days')
        
                        
    #Else if check that the month is in the 30-day-month list, the day element
    #is not in the range of 1 to 30
    elif date_list[0] in mon_list_2 and int(date_list[1]) not\
        in range(1,31):
                        
            is_valid_date = False
            print()
            print('Invalid: This month needs between 1 and 30 days')    
        
    #Check for valid year starting at the Julian Calendar
    elif int(date_list[2]) < 1000:
            
            is_valid_date = False
            print()
            print('Invalid: Year is not valid, please enter years' + \
                  'between 1000 and 9999 inclusive')
                    
    #Check if the date is a valid leap year date for February
    elif date_list[0] in leap_month and\
        int(date_list[1]) in range(1,30) and \
        int(date_list[2]) in leap_year_list:
            
            #If it is, turn leap_year true
            leap_year = True
                     
    #Check if it's a valid date for the month of February, using the 
    #leap_year = false to make sure there is no leap year exception
    elif date_list[0] in leap_month and int(date_list[1]) not in \
                range(1,29) and leap_year == False:
                    
                is_valid_date = False
                print()
                print('Invalid: This is not a valid date for February')
                
    elif is_valid_date == False and leap_year == False:
                print()
                print('Invalid: This is not a valid Leap ')
            
    """
    Valid February date otherwise
    """
    
    '''
    At this point the date is valid
    '''                         
    '''
    ==========================================================================
            ****CHECK FOR VALID TIME****
    ==========================================================================
    '''
    #if/elif loops to check that all inputs for HH,MM,SS are 2 in length
    if hour_length != 2:
                    
             is_valid_time = False
             print()
             print('Invalid: Hour length must have leading 0 and be'\
                   + ' two digits long')
                 
    elif min_length != 2:
                    
             is_valid_time = False
             print()
             print('Invalid: Minutes length must have leading 0 and be'\
                   + ' two digits long and valid')
                 
    #elif loops test that the values for the HH:MM:SS are appropriate for an 
    #actual time            
    elif int(time_list[0]) > 24 or int(time_list[0]) == 0:
             is_valid_time = False
             print()
             print('Invalid: Hour length must have leading 0 and be between'\
                   + ' 01 and 24 inclusive')
    elif int(time_list[1]) >= 60:
            is_valid_time = False
            print()
            print('Invalid: Minute length must have leading 0 and between'\
                   + ' 01 and 60 exclusive')

    '''
    At this point the time is valid
    '''
            
    '''
    ==========================================================================
            ****FINAL CHECK FOR VALID DATE & TIME****
    ==========================================================================
    '''
    #If either of the validity variables come back false... the 
    if is_valid_date == False and is_valid_time == True or \
       is_valid_date == True and is_valid_time == False:
           
           valid_date_time = False
           # print(valid_date_time, 'The date and time entered is invalid')
           
    #Returning a tuple of True or False values    
    return valid_date_time,is_valid_date,is_valid_time

"""
ADD ENTRY FUNCTION
"""
def entry_add(str):
    '''
    Parameters
    ----------
    a file that was created / entered by the user

    Returns
    -------
    None. Just creates the file for the user, adds the 
    date and entry, then closes it at the end
    '''
    #New line character incase the file already has text
    new_line = '\n'
    
    #Just a seperator for formatting later
    line_seps = ('=' * 40) + '\n'
    
    #Opening the user's file for appending
    new_entry = open(str,'a')
    
    #Call the date/time validating function
    valid_date_time = is_validate_datetime(user_date, user_time)
    
    #Write the date and time to the file if it's valid
    if valid_date_time == (True,True,True):
        
        #Create a list with the date and time
        date_time = [user_date,user_time]
        
        new_entry.write(new_line)
        
        new_entry.write(line_seps)
        
        new_entry.write(' '.join(date_time) + '\n')
        
        new_entry.write(line_seps)
        
        new_entry.write(new_line)
    
    #Else present error and exit the program closing the file    
    else:
        
        print()
        print('Date entered is invalid. Goodbye')
        new_entry.close()
        sys.exit()

    # #Prompt the user for an entry
    # entry = input('What do you want to write about? Press the Enter key' + \
    #               ' when you\'re finished: ')
    
    #Write that entry to the file
    new_entry.write(entry)
    
    print()
    print('Your entry has been added! Goodbye!')
    
    #Close the file
    new_entry.close()

    user_entry = Entry(entry)
    
    return user_entry
    
#Ask the user if they have a file
have_file = input('Do you have a file that you\'d like to add to? ')

'''
TEST FOR THE USER'S INPUT
'''
#Test that the answer is yes for having file
if have_file.lower() == 'yes':

    #Prompt them for the name of the file
    user_file = input('What is the name of the file you want to add to?' + \
                          ' Including the extension: ')
        
    #Try block to see if the file can be opened
    try:
            
         #Open the file input
         i_file = open((user_file),'r')
        
    #Print an error and ask if they'd like to create that file
    except FileNotFoundError:
            
            #Error message
            print()
            print('That does not exist')
            
            #Asking the user if they'd like to create the file
            create_prompt = input('Would you like to create that file? ')
            
            #If statement to see if they'd like to create the file
            if create_prompt.lower() == 'yes':
                
                #New file variable with the value of the file the user wanted
                #to create, break out of the loop
                new_file = open(user_file,'w')
                
                #Notify user that file has been created
                print()
                print('File created')
                
                #Close the file, it will be opened in the function for writing
                new_file.close()
                
                '''
                INSERT THE FUNCTION TO CREATE THE ENTRY HERE
                '''
                #Prompt the user to enter a date and time in try block for 
                #errors
                try:
                    
                    user_date, user_time = input('Enter a date time ' + \
                            '(seperated by a space as MM/DD/YYYY HH:MM): ')\
                            .split()
                            
                #Catch errors in the user's input, print error, and exit
                except ValueError:
                    
                    print()
                    print('Date not entered in correct format. Goodbye!')
                    sys.exit()
                
                #Prompt the user for an entry
                entry = input('What do you want to write about?'\
                              ' Press the Enter key' + \
                  ' when you\'re finished: ')
                
                #Use function to add entry to the file
                entry_add(new_file)
                
            #Elif statement for no answer to create file prompt
            elif create_prompt.lower() == 'no':
                
                #Print that they will be redirected to enter the file name
                print()
                print('Please find the file you\'d like to' + \
                      ' add to and try again. Goodbye.')
                sys.exit()
            
            #Notify user that only yes or no are acceptable answers and exit
            else:
                
                print()
                print('Only yes or no answers are accepted. Goodbye')
                sys.exit()
    
    #Else statement to add entry to the i_file if it exists
    else:
        '''
        INSERT THE FUNCTION TO CREATE THE ENTRY HERE
        '''
        #Prompt the user to enter a date and time in try block for 
        #errors
        try:
                    
            user_date, user_time = input('Enter a date time ' + \
            '(seperated by a space as MM/DD/YYYY HH:MM): ').split()
                            
        #Catch errors in the user's input, print error, and exit
        except ValueError:
                    
            print()
            print('Date not entered in correct format. Goodbye!')
            sys.exit()
        
        else:
            #Prompt the user for an entry
            entry = input('What do you want to write about?' + \
                          ' Press the Enter key' + \
                              ' when you\'re finished: ')
                
            #Create an Entry object with the text from the entry variable
            user_entry = Entry(entry)
            
            #Runs the entry add function
            entry_add(user_file)
    

#Check if the user answered no
elif have_file.lower() == 'no':
 
    #Prompt them to enter a file name for creation
    create_file = input('Please enter the name of a file you\'d like to' + \
                        ' create: ')
    
    #Testing to see if this file already exists and exit if it does
    try:
        
        #Open the file input
        i_file = open((create_file),'r')
    
    #If the file isn't found we want to catch that error and proceed to create
    #the file
    except FileNotFoundError:
        
        #New file variable with the value of the file the user wanted
        #to create, break out of the loop
        new_file = open(create_file,'w')
                    
        #Notify user that file has been created
        print()
        print('File created')
        
        #Close the file, it will be opened in the function for writing
        new_file.close()
        
        # #Prompt the user to enter a date and time
        # user_date, user_time = input('Enter a date time ' + \
        #     '(seperated by a space as MM/DD/YYYY HH:MM): ')\
        #     .split()
        
        '''
        INSERT THE FUNCTION TO CREATE THE ENTRY HERE
        '''
        #Prompt the user to enter a date and time in try block for 
        #errors
        try:
                    
            user_date, user_time = input('Enter a date time ' + \
            '(seperated by a space as MM/DD/YYYY HH:MM): ').split()
                            
        #Catch errors in the user's input, print error, and exit
        except ValueError:
                    
            print()
            print('Date not entered in correct format. Goodbye!')
            sys.exit()
        
        else:
            
            #Prompt the user for an entry
            entry = input('What do you want to write about?' + \
                          ' Press the Enter key' + \
                              ' when you\'re finished: ')
                
            #Create an Entry object with the text from the entry variable
            user_entry = Entry(entry)
            
            #Use function to add entry to the file
            entry_add(create_file)
    
    #If the file does exist, notify the user, close the file, and exit
    else:
        print()
        print('{} already exists. Please choose a file that does not exist.'\
              .format(create_file) + ' Goodbye.')
        i_file.close()
        sys.exit()
        
#Print error and exit if input wasn't yes or no
else:
    print()
    print('Only yes or no answers are accepted. Goodbye')
    sys.exit()

"""
CREATE A SEPARATE FILE UNIT TESTING THE ENTRY CLASS
"""
print(user_entry.get_all_words())
print(user_entry)
print(user_entry.is_paragraph_length())
print(user_entry._Entry__get_word(3))




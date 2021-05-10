# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 08:44:23 2021

@author: Dom Horard
CS 521 O2
04/05/2021
Term Project Proposal

A Journal program that allows users to enter a date, title,
and entry, then sends that to a file.

The program will ask the user first if there is an existing file that they 
would like to send their entry to. If there is, the program will take that 
file, ask for the date & time, and the entry, then append that to the end of 
the file.

If there is no existing file that the user has, the program will have the user
create a name for the file that will be created for the output.

The entries will be formatted for readability.
Dates will be formatted as MM/DD/YYYY, and time formatted as HH:MM

Will need to check that they entered a valied date and time.

The date & time will be underlined/otherwise seperated from the entry.

Time permitting, maybe some sort of search function can be implemented to
retrieve entries from a certain month or day.

In that case, user will first need to be prompted if they want to search for an
entry or create a new entry.


===============================================================================


Can use a dictionary to look up entries for a certain day / month

If the user tries to search for an entry on a date when no entry was created,
print an error.

Maybe have the dictoinary search for the date return the title for the entry, 
and ask the user if they want to return the entry itself if that's 
the date they want to see.

dictionary of dictionaries. {entry_date:{entry_title:entry}}

need to think about having multiple entries under the same date, would need the
entry time as the distinguishing values.

Should let the user know that they need to press enter when they are done with 
the paragrapgh, then prompt them if they want to type more, or quit the program


"""


# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:04:47 2018

@author: pchuzie / Randy Freaking Ramos
"""
import time
import datetime

def countdown():
    days = 0
    year= int(input('Enter a year: '))
    month= int(input('Enter a month (number): '))
    day= int(input('Enter a day: '))
    event = input('Event name: ')
    
    #This compares what the date entered to the current time, and once they 
    #are the same the loop will be exited
    while days != datetime.datetime.now():
        time_delta = (datetime.datetime(year,month,day) - datetime.datetime.now())
        print(str(time_delta)[:-7], event,'!')
        
        #This can be used to print with 'hrs','mins', and 'secs' next to numbers
        """
        sec = time_delta.seconds % 60
        mins = time_delta.seconds // 60
        
        hrs = mins // 60
        mins = mins % 60
        print(time_delta.days,'days',hrs,'hrs', mins,'mins', sec,'secs','\n')
        print('Until Graduation!!')
        print()
        """
        
        time.sleep(1)
        print("\033c")
        

    print('Happy Graduation!!')

countdown()

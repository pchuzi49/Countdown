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
        print("{} until {}!".format(str(time_delta)[:-7], event.strip()))
                
        time.sleep(1)
        print("\033c")
        



countdown()

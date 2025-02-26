# Parking Tickets

import math
import os
import random
import re
import sys

#
# Complete the 'ParkingTickets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER numEvents
#  2. STRING_ARRAY registrations
#  3. INTEGER_ARRAY times
#

def ParkingTickets(numEvents, registrations, times):
    # Write your code here
    
    reg_time = {}
    tickets = 0
    ticketed_cars = set()
    
    for i in range(numEvents):
        reg = registrations[i]
        time = times[i]

        if reg in reg_time:
            reg_time[reg].append(time)
        else:
            reg_time[reg] = [time]
    
    for reg, time_list in  reg_time.items():
        for i in range(1, len(time_list)):
            if reg in ticketed_cars:
                break
            else:
             if (i % 2) == 0:
                exit_entry = time_list[i] - time_list[i - 1]
                if exit_entry < 60:
                   tickets = tickets + 1
                   ticketed_cars.add(reg)
                   break
             else:
                entry_exity = time_list[i] - time_list[i - 1]
                if entry_exity > 60:
                   tickets = tickets + 1
                   ticketed_cars.add(reg)
                   break
    return tickets
               
                
n = 5
reg = ["A", "A", "B", "A", "B"]
times = [100, 200, 250, 300, 450] # Tuple to list
print(ParkingTickets(n,reg,times))
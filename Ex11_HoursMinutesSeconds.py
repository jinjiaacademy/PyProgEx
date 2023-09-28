# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:46:52 2023

@author: Jinjia
"""

"""
Write a getHoursMinutesSeconds() function that has a totalSeconds
parameter. The argument for this parameter will be the number of 
seconds to be translated into the number of hours, minutes, and
seconds. If the amount for the hours, minutes, or seconds is zero,
don't show it.

Additional challenge: break up 24 hour periods into days with a 
"d" suffix.

Prerequisite concepts: join(), append(), lists, string concatenation, 
while loops
"""


def getHoursMinutesSeconds(totalSeconds):
    # transfer totalSeconds into hours, minutes, and seconds.
    minute = 60
    hour = minute * 60
    day = hour * 24
    
    days = totalSeconds // day
    daysLeft = totalSeconds % day
    hours = daysLeft // hour
    hoursLeft = daysLeft % hour
    minutes = hoursLeft // minute
    seconds = hoursLeft % minute
    
    time = [days, hours, minutes, seconds]
    units = ["d", "h", "m", "s"]
    
    timeShow = []
    if totalSeconds == 0:
        return '0s'
    for i in range(len(time)):
        if time[i] != 0:
            timeShow.append(str(time[i]) + units[i])
    return " ".join(timeShow)
    
assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
#assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
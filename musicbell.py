#!/usr/bin/env python
#
# Version 2/13/2015
import random
import os
import time
import sys

base_path = '/usr/local/musicbell'
ending_song = os.path.join(base_path, 'class_ending.aif')
ending_song_length = 2 #How many mins long is the song
starting_song = os.path.join(base_path, 'class_starting.aif')
starting_song_length = 2 #How many mins long is the song
TERMINAL_NOTIFIER="/Applications/Utilities/terminal-notifier.app/Contents/MacOS/terminal-notifier"

def class_over():
    os.system('%s -title ":Alerts:" -message "Class is about to END..."' % (TERMINAL_NOTIFIER))
    os.system('Afplay %s' % (ENDING_SONG))
    os.system('ntpdate -u pool.ntp.org')

def class_starting():
    os.system('osascript -e "set Volume 10"')
    os.system('%s -title ":Alerts: -message" "Class is about to BEGIN..."' % (TERMINAL_NOTIFIER))
    os.system('Afplay %s' % (ENDING_SONG))
    os.system('ntpdate -u pool.ntp.org')
    time.sleep(60)

#Tuple for when there is no class. (Month,Day) format. These will need to be updated
#yearly. Long breaks set in different spot.
no_class (
    (9,14),(9,23)(10,12),(10,13)(11,25),(11,26),(11,27),(1,18)(2,15)
)

#Tuple for when you want class starting music to play. (Hour,Min) format.
class_start_times = (
    (8,15),(8,45),(9,30),(10,15),(11,0),(11,45)(12,30),(13,15),(14,0),(14,45),
    (15,30)
)

#Tuple for when you want class ending music to play.
class_end_times = (
    (8,40),(9,25),(10,10),(10,55),(11,40),(12,25),(13,10),(13,55),(14,40),
    (15,25)
)

FIRSTDAY = 8 #Sept
LASTDAY = 22 #June
WINTER_BRK_START = 21 #Dec
WINTER_BRK_END = 5 #Jan
SPRING_BRK_START = 21 #March
SPRING_BRK_END = 1 #April

DAY = time.strftime('%a')
TODAY = int(time.strftime('%d'))
MONTH = int(time.strftime('%m'))

# No School in Summer or on Weekends
if MONTH in (7,8) or DAY in ('Sat','Sun'):
    sys.exit(0)

# Winter Break
if (MONTH == 12 and TODAY >= WINTER_BRK_START) or (MONTH == 1 and
    TODAY <= WINTER_BRK_END):
    sys.exit(0)

# Spring Break
if (MONTH == 3 and TODAY >= SPRING_BRK_START) or (MONTH == 4 and
    TODAY <= SPRING_BRK_END):
    sys.exit(0)

# School in session from early Sept to Middle of June.
if (MONTH == 9 and TODAY < FIRSTDAY) or (MONTH == 6 and TODAY > LASTDAY):
    sys.exit(0)

# If the above all pass then proceed to main loop.
while True:

    HOUR = int(time.strftime("%H"))
    MIN = int(time.strftime("%M"))

    #Will play the song starting starting_song_length mins BEFORE class start time
    for start_time in class_start_times:
        if (HOUR == start_time[0][0] and
        (MIN == (start_time[0][1] - starting_song_length)%60)):
            class_starting()

    #Will play the song starting ending_song_length mins BEFORE class ends.
    for end_time in class_end_times:
        if (HOUR == end_time[0][0] and
        (MIN == (end_time[0][1] - ending_song_length)%60)):
            class_ending()

    #Check is school day is over.
    if HOUR >= 5:
        sys.exit(0)
    else:
        time.sleep(1) #Wait 1 sec before trying again

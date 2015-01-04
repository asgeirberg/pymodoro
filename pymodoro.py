#!/usr/bin/python

import sys
import time
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Set a Pomodoro timer.")

    parser.add_argument('-b', action="store_true", help='sets the number of minutes to 5, the default break time', default=False)
    parser.add_argument('-m', '--minutes', action="store", dest="minutes", type=int, help='sets the number of minutes to countdown. Default is 25', default=25)
    parser.add_argument('-q', action="store_true", help='supresses output', default=False)
    parser.add_argument('-p', action="store_true", help='prints a message every second', default=False)

    return parser.parse_args()

def print_minutes(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    print "\r",

    if print_seconds:
        if h > 0:
            print " %d:%02d:%02d" % (h, m, s),
        else:
            print " %02d:%02d" % (m, s),
    else:
        if seconds % 60 == 0:
            if h > 0:
                print " %d:%02d:%02d\r" % (h, m, s),
            else:
                print " %02d:%02d\r" % (m, s),

    sys.stdout.flush()

def countdown(count, quiet):
    while (count >= 0):
        if not quiet:  
            print_minutes(count)
        count -= 1
        time.sleep(1)

    if not quiet:
        print ('\a')

break_flag = parse_arguments().b

if not break_flag:
    seconds = parse_arguments().minutes * 60
else:
    seconds = 5 * 60

quiet = parse_arguments().q
print_seconds = parse_arguments().p

countdown(seconds, quiet)

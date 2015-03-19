#! /usr/bin/env python3

import os
import sys
venvpath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../venv"))
if not sys.prefix == venvpath:
    print ("Warning: overworkalert is possibly not running in correct virtual environment.")
    print (sys.prefix)
    print (venvpath)

import datetime
import subprocess
import smtplib
import traceback
from email.mime.text import MIMEText
from time import sleep

import util
import idledetectors

from defaults import *  # read default settings from defaults.py
from settings import *  # read user settings from settings.py

def popup(alerter):
    print ("Showing alert.")
    alerter()

def email():
    print ("Sending email.")
    msg = "You've been working too hard.  Please get up and walk around."
    msg = MIMEText(msg)

    msg['Subject'] = 'Overworking warning'
    msg['From'] = FROM_EMAIL
    msg['To'] = NOTIFY_EMAIL

    s = smtplib.SMTP(SMTP_HOST)
    s.sendmail(FROM_EMAIL, NOTIFY_EMAIL, msg.as_string())
    s.quit()


def runMonitor(idleDetector, alerter, howLongIsGone, interval, emailTime, popupTime, popupInterval):
    
    # we poll every `interval` seconds to see if the user is
    # idle (away from keyboard) or active (working, programming, sitting).

    # sittingPollCount is the number of consecutive polls which
    # report sitting.
    sittingPollCount = 0
    goneCount = 0

    didEmail = False
    popups = 0

    a = datetime.datetime.now()
    while True:
        sleep_seconds = (datetime.datetime.now() - a).total_seconds()
        a = datetime.datetime.now()
        if sleep_seconds > interval + 30:
            # computer must have been put to sleep.  assume user
            # was not working regardless of idleDetector
            print ("adding sleep time to goneCount")
            goneCount += int(sleep_seconds / interval);
        else:
            idle = idleDetector(interval)
            if idle:
                goneCount += 1
            else:
                goneCount = 0

        if goneCount * interval > howLongIsGone:
            sittingPollCount = 0
            didEmail = False
            popups = 0
        else:
            sittingPollCount += 1

        print ("goneCount " + str(goneCount))
        print ("sittingCount " + str(sittingPollCount))

        # if "user is still at desk" (if not at desk, but not yet "gone",
        # we'll just be waiting until they are not idle)
        if not idle:
            if sittingPollCount * interval > emailTime:
                if not didEmail:
                    try:
                        email()
                    except Exception as e:
                        popup(alerter)
                        print ("error sending email.  showed alert instead.")
                        print (traceback.format_exc())
                    didEmail = True
            if sittingPollCount * interval > popupTime:
                if sittingPollCount * interval > popupTime + (popups * popupInterval):
                    popup(alerter)
                    popups += 1

        sleep(interval)  # sleep for `interval` seconds

            

def run():
    runMonitor(IDLE_DETECTOR, ALERTER, HOW_LONG_IS_GONE, INTERVAL,
            EMAIL_WARNING, POPUP_WARNING, POPUP_INTERVAL)

if __name__ == '__main__':
    run()

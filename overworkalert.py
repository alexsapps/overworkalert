#! /usr/bin/env python3

import subprocess
import smtplib
from email.mime.text import MIMEText
from time import sleep

from defaults import *  # read default settings from defaults.py
from settings import *  # read user settings from settings.py


def getCommandOutput(args):
    return subprocess.check_output(args).decode("utf-8")

def email():
    msg = "You've been working too hard.  Please get up and walk around."
    msg = MIMEText(msg)

    msg['Subject'] = 'Overworking warning'
    msg['From'] = FROM_EMAIL
    msg['To'] = NOTIFY_EMAIL

    s = smtplib.SMTP(SMTP_HOST)
    s.sendmail(FROM_EMAIL, NOTIFY_EMAIL, msg.as_string())
    s.quit()

def popup():
    getCommandOutput(POPUP_CMD)

def isIdle_xprintidle(interval):
    output = getCommandOutput(["xprintidle"])
    idle = int(output)
    return idle / 1000 > interval

def isIdle_gnomescreensaver(interval):
    output = getCommandOutput(["gnome-screensaver-command","-q"])
    return "is active" in output

def runMonitor(idleDetector, howLongIsGone, interval, emailTime, popupTime, popupInterval):
    
    # we poll every `interval` seconds to see if the user is
    # idle (away from keyboard) or active (working, programming, sitting).

    # sittingPollCount is the number of consecutive polls which
    # report sitting.
    sittingPollCount = 0
    goneCount = 0

    didEmail = False
    popups = 0

    while True:
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

        # print ("goneCount " + str(goneCount))
        # print ("sittingCount " + str(sittingPollCount))

        # if "user is still at desk" (if not at desk, but not yet "gone",
        # we'll just be waiting until they are not idle)
        if not idle:
            if sittingPollCount * interval > emailTime:
                if not didEmail:
                    email()
                    didEmail = True
            if sittingPollCount * interval > popupTime:
                if sittingPollCount * interval > popupTime + (popups * popupInterval):
                    popup()
                    popups += 1

        sleep(interval)  # sleep for `interval` seconds
        
def run():
    runMonitor(IDLE_DETECTOR, HOW_LONG_IS_GONE, INTERVAL,
            EMAIL_WARNING, POPUP_WARNING, POPUP_INTERVAL)

if __name__ == '__main__':
    run()

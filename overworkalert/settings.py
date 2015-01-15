import idledetectors
import alerters

# override default settings here

NOTIFY_EMAIL = 'you@example.org'
FROM_EMAIL = NOTIFY_EMAIL
SMTP_HOST = 'smtp.example.org'

# uncomment below lines to override default lettings

# the algorithm that detects if you're idle
# IDLE_DETECTOR = idledetectors.isIdle_gnomescreensaver
# IDLE_DETECTOR = idledetectors.isIdle_osx_screenLocked

# aleter / popup
#  function that shows a real time notification on your screen
# ALERTER = alerters.alert_gnomePopup
# ALERTER = alerters.alert_osxPopup

# how many seconds of continual sitting before the desk job worker
# gets a non-distracting email reminding them to stand up
# EMAIL_WARNING = 60 * 50  # 50 minutes

# how many seconds of continual sitting before the desk job worker
# gets an interrupting pop-up display reminding them to stand up
# POPUP_WARNING = 60 * 60  # 60 minutes

# how many seconds between repeated popups
# POPUP_INTERVAL = 60 * 2  # 2 minutes

# number of seconds of continuous inactivity until you're considered
# to have left the computer and be walking around, in seconds
# HOW_LONG_IS_GONE = 60 * 2  # 2 minutes

# how long between polls of idleness.  frequent polls = more accurate
# for some detectors.  measured in seconds.
# INTERVAL = 15  # 15 seconds

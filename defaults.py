from overworkalert import *

IDLE_DETECTOR = isIdle_gnomescreensaver
EMAIL_WARNING = 60 * 50  # 50 minutes
POPUP_WARNING = 60 * 60  # 60 minutes
POPUP_INTERVAL = 60 * 2  # 2 minutes
HOW_LONG_IS_GONE = 60 * 2  # 2 minutes
INTERVAL = 15  # 15 seconds
NOTIFY_EMAIL = 'you@example.org'
FROM_EMAIL = NOTIFY_EMAIL
SMTP_HOST = 'smtp.example.org'
POPUP_CMD = ['notify-send','Overworking Warning','Get up and walk around.']

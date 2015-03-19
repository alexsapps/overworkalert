import util

################################
#       LINUX
################################

# find the idle detection function you like and spceify
# it in settings.py.

# important:  in this context, idle means idleness of your
# computer, not your body.  if your keyboard is idle,
# that means your body is stretching, walking around and
# taking a mental break.

# use the xprintidle command on Linux to determine when you
# are idle.  if you don't touch the keyboard or mouse for
# a number of seconds greater than the "interval" setting,
# you won't be considered overworking.
def isIdle_xprintidle(interval):
    output = util.getCommandOutput(["xprintidle"])
    idle = int(output)
    return idle / 1000 > interval


# determine if you are idle with gnomescreensaver (default for
# Ubuntu) by locking your screen before you leave.  when
# overworkalert sees your screen locked for HOW_LONG_IS_GONE
# seconds, your time will be reset and you won't be considered
# to be overworking.
def isIdle_gnomescreensaver(interval):
    output = util.getCommandOutput(["gnome-screensaver-command","-q"])
    return "is active" in output


################################
#       OS X
################################

# determine if you are idle using last keyboard/mouse input time
# using this trick from a stackoverflow answer:
# http://stackoverflow.com/questions/8653144/
def isIdle_osx_HIDIdleTime(interval):
    cmd = ("echo $((`ioreg -c IOHIDSystem | sed -e '/HIDIdleTime/"
           " !{ d' -e 't' -e '}' -e 's/.* = //g' -e 'q'` / 1000000000))"
           )
    output = util.getBashOutput(cmd)
    idle = int(output)
    return idle > interval

def isIdle_osx_screensaver(interval):
    cmd = ("osascript -e 'tell application \"System Events\"' "
           "-e 'get running of screen saver preferences' -e 'end tell'"
           )
    output = util.getBashOutput(cmd)
    return "true" in str(output)

# http://stackoverflow.com/questions/11505255/osx-check-if-the-screen-is-locked
def isIdle_osx_screenLocked(interval):
    import Quartz
    d=Quartz.CGSessionCopyCurrentDictionary()
    return d and d.get("CGSSessionScreenIsLocked", 0)


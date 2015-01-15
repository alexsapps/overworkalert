import util

def alert_gnomePopup():
    cmd = ['notify-send','Overworking Warning','Time to get up and walk around!']
    utils.getCommandOutput(cmd)

def alert_osxPopup():
    cmd = "osascript -e 'tell app \"System Events\" to display dialog \"Time to get up and walk around!\"'"
    util.getBashOutput(cmd)   

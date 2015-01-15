import subprocess

def getCommandOutput(args):
    return subprocess.check_output(args).decode("utf-8")

def getBashOutput(bash_command):
    # http://stackoverflow.com/questions/4256107
    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0]
    return output

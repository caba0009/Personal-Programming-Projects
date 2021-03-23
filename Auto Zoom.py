# @author Tanner Cabaniss
# @email <tanner.l.cabaniss-1@ou.edu>
# @version 1.0

from datetime import datetime
import sys, time
import webbrowser

def getCurrentDay(): # Determine the current day of the week
    today = datetime.today()
    currentDay = today.strftime("%A")
    return currentDay

def getCurrentTime(): # Determine the current time
    now = datetime.now()
    currentTime = now.strftime("%H%M")
    currentTime = int(currentTime)
    return currentTime


def selectDay(day): # Assign classSet to appropriate day of the week
    if (day == "Monday" or day == "Wednesday"):
        classSet = 1
    elif (day == "Tuesday" or day == "Thursday"):
        classSet = 2
    else:
        classSet = 0
    return classSet

def selectTime(time): # Assign timeSet to appropriate time of the day
    if (time >= 1245 and time <= 1430):
        timeSet = 1
    elif (time >= 1445 and time <= 1630):
        timeSet = 2
    elif (time >= 1515 and time <= 1700):
        timeSet = 3
    elif (time >= 1715 and time <= 1900):
        timeSet = 4
    elif (time >= 1915 and time <= 2115):
        timeSet = 5
    else:
        timeSet = 0
    return timeSet

def selectZoom(time,day): # Select appropriate link for given time and day
    if (day == 1 and time == 3):
        webbrowser.open("http://www.google.com")
    elif (day == 1 and time == 4):
        webbrowser.open("https://oklahoma.zoom.us/j/96436565728?pwd=QWg5cFVMQ3BaeDRUVGFHOG9NOXM1dz09")
    elif (day == 1 and time == 5):
        webbrowser.open("https://oklahoma.zoom.us/j/91486554635?pwd=VTU4ZURiMk9HbGt0QWFpYWg2QmdhUT09#success")
    elif (day == 2 and time == 1):
        webbrowser.open("https://oklahoma.zoom.us/j/94740417467?pwd=TlB5Zmk1clk1c2gyUVpoQjh5dVpDUT09")
    elif (day ==2 and time == 2):
        webbrowser.open("https://oklahoma.zoom.us/j/97119662535?pwd=T1ltOVlPZnlGNGlzSnVISkpMV28xUT09")
    else:
        sys.exit()

def main():
    selectZoom(selectTime(getCurrentTime()),selectDay(getCurrentDay()))
    sys.exit() # Automatically closes program once link has been opened

main()
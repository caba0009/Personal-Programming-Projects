import os.path, time
import os, sys
import tkinter as tk
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from time import strftime
from pathlib import Path, PureWindowsPath
from matplotlib import pyplot as plt
import numpy as np


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    print(dirName)
    global allFiles
    allFiles = list()
    for entry in listOfFile:
        fullPath = PureWindowsPath(dirName, entry)
        if os.path.isdir(fullPath):
            try:
                allFiles += getListOfFiles(fullPath)
            except:
                print ('file error')
        else:
            try:
                allFiles.append(fullPath)
            except:
                print('file error')
    return allFiles

def creation_date(path_to_file):
    global newList
    newList = list()
    for path in allFiles:
        newList.append(time.strftime('%H', (time.localtime(os.path.getctime(path)))))
    return newList

def createList():
    root = Tk()
    root.withdraw()
    filePath = filedialog.askdirectory(initialdir = "/",title = "Select file")
    getListOfFiles(str(filePath))
    creation_date(allFiles)
    return newList

def restart_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    if messagebox.askyesno(subject, content) == True:
        main()
    else:
        pass
    try:
        root.destroy()
    except:
        pass

def exit_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    if messagebox.askyesno(subject, content) == True:
        sys.exit()
    else:
        restart_box('Restart?', 'Would you like to analyze another set of photoes?')
    try:
        root.destroy()
    except:
        pass
def typedata_box(subject, content):
    kind = simpledialog.askstring("Data Type", "Please enter data type...graph, graphsimple, number, numbersimple")
    hour0 = newList.count('00')
    hour1 = newList.count('01')
    hour2 = newList.count('02')
    hour3 = newList.count('03')
    hour4 = newList.count('04')
    hour5 = newList.count('05')
    hour6 = newList.count('06')
    hour7 = newList.count('07')
    hour8 = newList.count('08')
    hour9 = newList.count('09')
    hour10 = newList.count(str(10))
    hour11 = newList.count(str(11))
    hour12 = newList.count(str(12))
    hour13 = newList.count(str(13))
    hour14 = newList.count(str(14))
    hour15 = newList.count(str(15))
    hour16 = newList.count(str(16))
    hour17 = newList.count(str(17))
    hour18 = newList.count(str(18))
    hour19 = newList.count(str(19))
    hour20 = newList.count(str(20))
    hour21 = newList.count(str(21))
    hour22 = newList.count(str(22))
    hour23 = newList.count(str(23))
    morning = newList.count('06') + newList.count('07') + newList.count('08') + newList.count('09')
    mid_day = newList.count('10') + newList.count('11') + newList.count('12') + newList.count('13') + newList.count('14') + newList.count('15')
    afternoon = newList.count('16') + newList.count('17') + newList.count('18') + newList.count('19') + newList.count('20')
    night = newList.count('21') + newList.count('22') + newList.count('23') + newList.count('24') + newList.count('00') + newList.count('01') + newList.count('02') + newList.count('03') + newList.count('04') + newList.count('05')
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    if kind == 'number':
        print('12:00 A.M. - 12:59 A.M. : '+ str(hour0))
        print('1:00 A.M. - 1:59 A.M.   : '+ str(hour1))
        print('2:00 A.M. - 2:59 A.M.   : '+ str(hour2))
        print('3:00 A.M. - 3:59 A.M.   : '+ str(hour3))
        print('4:00 A.M. - 4:59 A.M.   : '+ str(hour4))
        print('5:00 A.M. - 5:59 A.M.   : '+ str(hour5))
        print('6:00 A.M. - 6:59 A.M.   : '+ str(hour6))
        print('7:00 A.M. - 7:59 A.M.   : '+ str(hour7))
        print('8:00 A.M. - 8:59 A.M.   : '+ str(hour8))
        print('9:00 A.M. - 9:59 A.M.   : '+ str(hour9))   
        print('10:00 A.M. - 10:59 A.M. : '+ str(hour10))
        print('11:00 A.M. - 11:59 A.M. : '+ str(hour11))
        print('12:00 P.M. - 12:59 P.M. : '+ str(hour12))
        print('1:00 P.M.  - 1:59 P.M.  : '+ str(hour13))
        print('2:00 P.M.  - 2:59 P.M.  : '+ str(hour14))
        print('3:00 P.M.  - 3:59 P.M.  : '+ str(hour15))
        print('4:00 P.M.  - 4:59 P.M.  : '+ str(hour16))
        print('5:00 P.M.  - 5:59 P.M.  : '+ str(hour17))
        print('6:00 P.M.  - 6:59 P.M.  : '+ str(hour18))
        print('7:00 P.M.  - 7:59 P.M.  : '+ str(hour19))
        print('8:00 P.M.  - 8:59 P.M.  : '+ str(hour20))
        print('9:00 P.M.  - 9:59 P.M.  : '+ str(hour21))
        print('10:00 P.M. - 10:59 P.M. : '+ str(hour22))
        print('11:00 P.M. - 11:59 P.M. : '+ str(hour23) + '\n')
    elif kind == 'numbersimple':
        print('----------------')
        print('Morning(5am-9am)   : '+ str(morning))
        print('----------------')
        print('Mid-Day(10am-3pm)  : '+ str(mid_day))
        print('----------------')
        print('Afternoon(4pm-8pm) : '+ str(afternoon))
        print('----------------')
        print('Night(9pm-5am)     : '+ str(night))
        print('----------------')
    elif kind == 'graph':
        ylist = [hour0, hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8, hour9, hour10, hour11, hour12, hour13, hour14, hour15, hour16, hour17, hour18, hour19, hour20, hour21, hour22, hour23]
        xlist = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']
        ypos = np.arange(len(xlist))
        plt.xticks(ypos,xlist)
        plt.bar(ypos,ylist)
        plt.xlabel('Time')
        plt.ylabel('Number of Pictures')
        plt.title('Game Camera Analysis')
        plt.show()
    elif kind == 'graphsimple':
        xlist = ['Morning(6am-9am)', 'Mid-Day(10am-3pm)', 'Afternoon(4pm-8pm)', 'Night(9pm-5am)']
        ylist = [morning, mid_day, afternoon, night]
        ypos = np.arange(len(xlist))
        plt.xticks(ypos,xlist)
        plt.bar(ypos,ylist)
        plt.xlabel('Time of Day')
        plt.ylabel('Number of Pictures')
        plt.title('Game Camera Analysis')
        plt.show()
    else:
        print('Not valid type...Restarting Program')
        main()

def main():
    print('BOOTING..')
    createList()
    typedata_box("Data Type", "Please enter data type...graph, graphsimple, number, numbersimple")
    restart_box('Restart?', 'Would you like to analyze another set of photos?')
    exit_box('Exit Application', 'Do you want to quit the application?')

main()
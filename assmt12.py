#Question.1- Print the current day using Datetime module.
import datetime as d
date=d.date.today()
print('DATE IS:',date)
print('YEAR:',date.strftime("%Y"))
print('MONTH:',date.strftime("%B"))
print('DAY OF MONTH:',date.strftime("%D"))
print('WEEKDAY IS:',date.strftime("%A"))


#Question.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
webbrowser.open("https://youtu.be/TeXFNPXFcSs")


#Question.3- Write a program to rename all the files in a directory and convert them into .jpg file format.

import os,sys
address = r'C:\Users\Saurav\Desktop\py11\pyy11'
for file in os.listdir(address):
    oldfile = os.path.join(address,file)
    if not os.path.isfile(oldfile):
        continue
    oldbase = os.path.splitext(file)
    newfile = oldfile.replace('.txt', '.jpg')
    newname = os.rename(oldfile, newfile)

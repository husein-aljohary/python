from msilib.schema import RadioButton
from multiprocessing.sharedctypes import Value
from tkinter import *


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3 
import os


"""



top=Tk()
top.minsize(900,950)

#num1=Label(text="first name")
#num1.pack()
#num1input=Entry()
#num1input.pack()


#but=Button(text="Convert")   
#but.pack() 

engine=pyttsx3.init()
def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('Voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice() 
        elif (speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',50)
            setvoice()    


top.title( "Text to speech")

top.resizable (False, False)
top.configure (bg="#0000FF")
#icon
#image_icon=PhotoImage (file = "speak .png")
#top.iconphoto(False, image_icon) 


Top_frame=Frame(top,bg= "white",width=900, height=100)
Top_frame.place(x=0,y=0)
#Logo=PhotoImage (file="speaker logo.png")
Label(Top_frame,  bg="white").place(x=10,y=5)
Label (Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black") . place (x=100,y=30)

text_area=Text (top, font=" Robote 20",bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=150, width=500, height=250)

Label(top, text="voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580, y=160)
Label(top, text="SPEED", font="arial 15 bold", bg="#305e65",fg="white") .place (x=760, y=160)

gender_combobox=Combobox(top, values=[ 'Male','Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=500,y=200)
gender_combobox.set ('Male')

speed_combobox=Combobox(top, values= [ 'Fast', 'Normal', 'slow '], font="arial 14", state='r', width=10)
speed_combobox. place (x=730, y=200)
speed_combobox . set('Normal')

#imageicon=PhotoImage(file="speak.png")
btn=Button (top, text= "Speak" , compound=LEFT, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550,y=280)




top.mainloop()

"""

top=Tk()
var = IntVar()
#
str=tk.StringVar()
#change the background
top.configure(bg="#F0E68C")
top.minsize(900,950)
engine =pyttsx3.init()
voices = engine.getProperty('voices')
def speack():
    text=text_area.get(1.0,END)
    #change the voice
    if str.get()=='A':
        engine.setProperty('voice', voices[0].id)  
    else:
        engine.setProperty('voice', voices[1].id)


    engine .say(text)
    #speed the voice
    engine .setProperty('rate',150)
    engine .runAndWait()
#Label(top, text="Hello there!", font=("arial italic", 18) ).pack()
title=Label(text="Write text to convert it to voice ",background="#F0E68C",font="italic").place(x=170,y=110)

text_area=Text (top, font=" Robote 20",bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=150, width=500, height=250)

r1 = tk.Radiobutton(top, text='Male', variable=str, value='A',background="#7CB9E8",width=6,height=1).place(x=300,y=420)

#r1.pack()

r2 = tk.Radiobutton(top, text='Female', variable=str, value='B',background="#FF00BF",width=6,height=1).place(x=390,y=420)

#r2.pack()
##################################################################


btn=Button (top, text= "Speak" , compound=LEFT, width=10, font="arial 14 bold",command=speack)
btn.place(x=10,y=450)

top.mainloop()







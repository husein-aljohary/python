from cProfile import label
from curses import window
from tkinter import *

window=Tk()
window.title("*firs program*")
window.geometry("420x500")
window.config(background="red")
photo=PhotoImage(file='C:\\Users\\user\\Desktop\\road.png')

label=Label(window,
text="hellllllo",
font=('fantasy ',40),
fg='green',
bg='black',
relief=RAISED,
bd='10',
image=photo,
compound='bottom')


label.config(background="white")
label.pack()



count = 0

def click():
    global count
    count+=1
    print(count)


button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                compound='bottom')
button.pack()


entry=Entry(window,
            font=(50))

entry.pack()




#entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello "+username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)


entry = Entry(window,
              font=("Arial",20),
              fg="#00FF00",
              bg="black")

#entry.insert(0,'Spongebob')
#entry.config(show="*")
#entry.config(state=DISABLED)

entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)










window.mainloop()
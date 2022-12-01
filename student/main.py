from tkinter import *
from tkinter import ttk
from tkinter import font
from db import Database
from tkinter import messagebox

db=Database("Student.db")

root=Tk()
root.title("Student System")
root.geometry('1000x615+40+80')
root.resizable(False,False)
root.configure(bg='#D3C9C6')

id=StringVar()
name=StringVar()
email=StringVar()
gender=StringVar()
gpa=StringVar()

logo=PhotoImage(file='logo.png')
lp_logo=Label(root,image=logo,bg='#D3C9C6')
lp_logo.place(x=50,y=420)


######enteries
entries_frame=Frame(root,bg='#D3C9C6')
entries_frame.place(x=1, y=1, width=350, height=440)
title=Label(entries_frame, text='Student Information', font=('calibri',15,'bold'), bg='#D3C9C6')
title.place(x=10, y=1)

lblid=Label(entries_frame,text='ID',font=('calibri',15), bg='#D3C9C6')
lblid.place(x=8, y=50)
txtid=Entry(entries_frame, width=22,textvariable=id , font=('calibri',15))
txtid.place(x=80, y=50)

lblname=Label(entries_frame,text='Name', font=('calibri',15), bg='#D3C9C6')
lblname.place(x=8, y=90)
txtname=Entry(entries_frame, width=22,textvariable=name , font=('calibri',15))
txtname.place(x=80, y=90)

lblemail=Label(entries_frame,text='Email', font=('calibri',15), bg='#D3C9C6')
lblemail.place(x=8, y=130)
txtemail=Entry(entries_frame, width=22,textvariable=email , font=('calibri',15))
txtemail.place(x=80, y=130)

lblgender=Label(entries_frame,text='Gender', font=('calibri',15), bg='#D3C9C6')
lblgender.place(x=8, y=170)
combogender=ttk.Combobox(entries_frame,textvariable=gender , state='readonly', width=20, font=('calibri',15))
combogender['value']=('Male','Female')
combogender.place(x=80, y=170)

lblgpa=Label(entries_frame,text='Gpa', font=('calibri',15), bg='#D3C9C6')
lblgpa.place(x=8, y=210)
txtgpa=Entry(entries_frame, width=22,textvariable=gpa , font=('calibri',15))
txtgpa.place(x=80, y=210)


def hide():
    root.geometry('360x615')

def show():
    root.geometry('1000x615+40+80')

btnhide=Button(entries_frame, text='hide',command=hide,cursor='hand2', bg='#A0857D', fg='white')
btnhide.place(x=250,y=10)
btnshow=Button(entries_frame, text='show',command=show,cursor='hand2', bg='#A0857D', fg='white')
btnshow.place(x=300,y=10)

def getdata(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row =data['values']
    #id.set(row[0])
    name.set(row[1])
    email.set(row[2])
    gender.set(row[3])
    gpa.set(row[4])
    

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def clear():
    id.set("")
    name.set("")
    email.set("")
    gender.set("")
    gpa.set("")

def delete():
    db.remove(row[0])
    clear()
    displayall()

def add_student():
    if txtname.get() == "" or txtid.get()=="" or txtemail.get()=="" or txtgpa.get()=="" or combogender.get()=="" :
        messagebox.showerror("Error","please fill all entries")
        return
    db.insert(
        txtid.get(),
        txtname.get(),
        txtemail.get(),
        combogender.get(),
        txtgpa.get()
        
    )
    messagebox.showinfo("seccess adding")
    clear()
    displayall()

def update():
    if txtname.get() == "" or txtid.get()=="" or txtemail.get()=="" or txtgpa.get()=="" or combogender.get()=="" :
        messagebox.showerror("Error","please fill all entries")
        return
    
    db.update(row[0],
        #txtid.get(),
        txtname.get(),
        txtemail.get(),
        combogender.get(),
        txtgpa.get()
    )
    messagebox.showinfo('Success','the data is update')
    clear()
    displayall()

###Buttons
buttons_frame=Frame(entries_frame,bg='#D3C9C6',bd=1)
buttons_frame.place(x=10, y=320, width=330, height=100)
btnadd=Button(buttons_frame,
                text='Add Student',
                width=11,
                height=1,
                font=('calibri',14),
                fg='white',
                bg='#A0857D',
                bd=0,cursor='hand2',
                command=add_student
            ).place(x=2,y=5)

btnedit=Button(buttons_frame,
                text='Edit Student',
                width=11,
                height=1,
                font=('calibri',14),
                fg='white',
                bg='#A0857D',
                bd=0,cursor='hand2',
                command=update
            ).place(x=2,y=50)

btndelete=Button(buttons_frame,
                text='Delete Student',
                width=12,
                height=1,
                font=('calibri',14),
                fg='white',
                bg='#A0857D',
                bd=0,cursor='hand2',
                command=delete
            ).place(x=128,y=5)

btnclear=Button(buttons_frame,
                text='Clear',
                width=12,
                height=1,
                font=('calibri',14),
                fg='white',
                bg='#A0857D',
                bd=0,cursor='hand2',
                command=clear
            ).place(x=128,y=50)

#######table

tree_frame=Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=670,height=610)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('calibri',13))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="100")
tv.heading("2",text="Name")
tv.column("2",width="170")
tv.heading("3",text="Email")
tv.column("3",width="220")
tv.heading("4",text="Gender")
tv.column("4",width="90")
tv.heading("5",text="Gpa")
tv.column("5",width="50")
tv['show']= 'headings'
tv.bind("<ButtonRelease-1>",getdata)
tv.place(x=1,y=1,height=610)


displayall()



root.mainloop()
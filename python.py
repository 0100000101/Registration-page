from tkinter import *
from tkinter import ttk
root=Tk()
root.title('WINDOW')
root.geometry('400x300')
root.resizable(False,False)
root.config()
a=Frame(root)
b=Frame(root)
b1=Frame(root)
profileFrame = Frame(root,bg="#D0D0D0")
q=13
q1=45
q2=0
q3=5

def gotoLoginPage():
    a.forget()
    b.pack(expand=True,fill=BOTH)
    b.config(bg='#EEF350')

def registerPage():
    a.forget()
    b1.pack(expand=True,fill=BOTH)
    b1.config(bg='#9550EC')

def backtoMainFromLogin():
    b.forget()
    a.pack(expand=True,fill=BOTH)

def backtoMainFromLogin1():
    b1.forget()
    a.pack(expand=True,fill=BOTH)

def backtoMainFromLogin2():
    profileFrame.forget()
    b.pack(expand=True,fill=BOTH)

def show1():
    if calc2['show']=='*':
        calc2.configure(show='')
    else:
        calc2.configure(show='*')
        buttonadd.configure(text='SHOW')

def goToProfilePage():
    login = calc.get()
    password = calc.get()
    if login == "admin":
        if password == "admin":
            b.forget()
            profileFrame.pack(expand=True,fill=BOTH)

def add():
    new_diller = v.get()
    names_listbx.insert(END,new_diller)

def delete():
    f=names_listbx.curselection()
    names_listbx.delete(f)
rightFrameonProfile = Frame(a,bg='#6AD2F7')
rightFrameonProfile.place(relx=0.2,rely=0,relwidth=0.8,relheight=1)
leftFrameonProfile = Frame(a,bg='#6AD2F7')
leftFrameonProfile.place(relx=0,rely=0,relwidth=0.2,relheight=1)
a.pack(expand=True,fill=BOTH)
lable=Label(a,text='WELCOME',font=("Comic Sans MS", 10),bg='#6AD2F7')
lable.pack(padx=168,pady=15)
button=Button(a,text='Login page',font='verdana 8 bold',command=lambda :gotoLoginPage())
button.config(height=2,background='#0097FF',)
button.pack()
button2=Button(a,text='Register page',font='verdana 8 bold',command=lambda :registerPage())
button2.config(height=2,background='#0097FF',)
button2.pack()
text1=Label(b,text='Welcome to my login page.',font=("Comic Sans MS", 12),fg='#B900FF',bg='#EEF350')
text1.pack()
lable2=Label(b,text='Login :',bg='#EEF350')
lable2.place(x=80,y=40)
lable3=Label(b,text='PASS  :',bg='#EEF350')
lable3.place(x=80,y=62)
calc = Entry(b,font=('bold',8))
calc.place(y=43,x=130)
calc2 = Entry(b,font=('bold',8),show='*')
calc2.place(y=63,x=130)
buttonadd = Button(b,text='SHOW',font='Helvetica 7 bold',command=show1)
buttonadd.config(width=3,height=1)
buttonadd.place(x=260,y=63)
x = Radiobutton(b,text="Admin",value="Admin",bg='#EEF350')
x.place(x=118,y=95)
x1 = Radiobutton(b,text="User",value="User",bg='#EEF350')
x1.place(x=200,y=95)
buttonadd2 = Button(b,text='Login',font='Helvetica 10 bold',command=goToProfilePage)
buttonadd2.config(width=5,height=1)
buttonadd2.place(x=165,y=130)
knopka = Button(b,text='Back',fg='red',command=lambda :backtoMainFromLogin())
knopka.place(x=6,y=6)
knopka1 = Button(b1,text='Back',fg='red',command=lambda :backtoMainFromLogin1())
knopka1.place(x=6,y=6)
text3=Label(profileFrame,text='Please enter your information:',font=("Comic Sans MS", 12),bg="#D0D0D0")
text3.pack()
text4=Label(profileFrame,text='Name:',bg="#D0D0D0")
text4.place(x=150,y=30)
calc11=Entry(profileFrame,font=('bold',8),bd=2)
calc11.place(y=33,x=205)
Gender=['Gender','Male','Female','other']
z=StringVar(value=Gender[0])
combobox=ttk.Combobox(profileFrame,textvariable=z,values=Gender)
combobox.place(x=155,y=60)
text5=Label(profileFrame,text='Eye color:',bg="#D0D0D0")
text5.place(x=150,y=90)
calc12=Entry(profileFrame,font=('bold',8),bd=2)
calc12.place(y=93,x=205)
text6=Label(profileFrame,text='Height:',bg="#D0D0D0")
text6.place(x=150,y=115)
calc13=Entry(profileFrame,font=('bold',8),bd=2)
calc13.place(y=117,x=205)
text7=Label(profileFrame,text='inches',bg="#D0D0D0")
text7.place(x=332,y=115)
text8=Label(profileFrame,text='Weight:',bg="#D0D0D0")
text8.place(x=150,y=140)
calc14=Entry(profileFrame,font=('bold',8),bd=2)
calc14.place(y=140,x=205)
text9=Label(profileFrame,text='lbs',bg="#D0D0D0")
text9.place(x=332,y=140)
knopka3 = Button(profileFrame,text='Back',fg='red',command=lambda :backtoMainFromLogin2())
knopka3.place(x=6,y=6)
names = [' Jhon       Smith              425-6577',' Allen       Mathews        478-4578']
names_var= Variable(value=names)
names_listbx = Listbox(b1,listvariable=names_var,selectmode=MULTIPLE,width=30,height=5,bd=2,bg='#E3E3E3')
names_listbx.pack()
add_bt=Button(b1,text="Add",font=("",12),command=add)
add_bt.place(x=300,y=10)
v=Entry(b1)
v.pack(padx=3,pady=6)
delete_bt=Button(b1,text="Delete",font=("",12),command=delete)
delete_bt.place(x=300,y=50)

root.mainloop()

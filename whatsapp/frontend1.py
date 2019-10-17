from tkinter import *
import webbrowser
def retrieve(): #for send button 
    global input
    input =t1.get("1.0",'end-1c')
    import bckend
    print(input)

def Go_to_github():  #for help button
    webbrowser.open('https://github.com/GHakshay')



window=Tk()

l1=Label(window,text="Whatsapp Automation",font='Helvetica 10 bold')
l1.grid(row=0,column=8)

l2=Label(window,text="Made by A-Team")
l2.grid(row=11,column=2)

b1=Button(window,text ="send",font='Helvetica 10 bold',height=3,width=13,command=retrieve)
b1.grid(row=2,column=8)

b2=Button(window,text =" help ",font='Helvetica 10 bold',height=3,width=13,command=Go_to_github)
b2.grid(row=2,column=15)


"""
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=1,column=0,columnspan=12,rowspan=10)
window.grid_columnconfigure(0, weight=4)
"""

t1=Text(window,height=20,width=40)
t1.grid(row=1,column=4,columnspan=10)
#"1" means from line 1 it ll take input
window.mainloop()

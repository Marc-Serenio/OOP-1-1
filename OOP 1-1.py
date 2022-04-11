from tkinter import *
window = Tk()

window.geometry("600x500+30+80")
window.title ("Welcome to Python Programming")

#add Button widget

btn = Button(window,text="What's your Name", fg="Gold", bg="Black")
btn.place(x=80, y=110)
#Add label widget

lbl = Label(window, text= "STUDENT PERSONAL INFORMATION", fg="Gold", bg="Black")
lbl.place(x=200, y=60)
lbl2 = Label(window, text="GENDER", fg="Gold", bg="Black")
lbl2.place(x=80, y=150)


#Add text field widget

txtfld = Entry(window, bd=3, font=("Courier New", 13))
txtfld.place(x=190, y=110)


#add radio button

v1 = StringVar()
v2 = StringVar()
v1.set(1)
r1 = Radiobutton(window, text="Male", value=v1)
r1.place(x=80, y=200)

r2 = Radiobutton(window, text="Female", value=v2)
r2.place(x=200, y=200)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()


chkbox = Checkbutton(window, text="Basketball", variable=v3)
chkbox2 = Checkbutton(window, text="Volleyball", variable=v4)
chkbox3 = Checkbutton(window, text="Badminton", variable=v5)
chkbox4 = Checkbutton(window, text="Chess", variable=v6)


chkbox.place(x=80, y=300)
chkbox2.place(x=250, y=300)
chkbox3.place(x=350, y=300)
chkbox4.place(x=450, y=300)


lbl3 = Label(window, text="SPORTS", fg="Gold", bg="Black")
lbl3.place(x=80, y=250)

lbl4 = Label(window, text="SUBJECTS", fg="Gold", bg="Black")
lbl4.place(x=80, y=350)

var = StringVar()
var.set("arithmethic")
data1 = "CALCULUS"
data2 = "PROGRAMMING"
data3 = "PHYSICS"

lstbox = Listbox(height= 5, selectmode="multiple")
lstbox.insert(END, data1, data2, data3)
lstbox.place(x=70, y=390)


window.mainloop()
from tkinter import *
window = Tk()

window.geometry("700x400+30+80")
window.title("Midterm In OOP")

lbl = Label(window,text = "Enter your fullname", fg="red")
lbl.place(x=50, y=125)
txtfld = Entry(window, bd=3, font=("Courier",16))
txtfld.place(x=270, y=125)

def click():
    value=txtfld.get()
    txtfld2.insert(END,str(value))

btn = Button(window, text="Click to display your Fullname", fg="red", command = click)
btn.place(x=50, y=180)

txtfld2 = Entry(window, bd=3, font= ("Courier New", 16))
txtfld2.place(x=270, y=180)

window.mainloop()
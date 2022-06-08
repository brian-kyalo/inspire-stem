#create your first gui application 

from tkinter import *

window = Tk()
window.title("Welcome to my Application")
window.configure(bg="white")
window.geometry("400x400") #fix the window size
f_name = Label(window, text="First Name", font=("Arial Bold", 20))
s_name = Label(window, text="second Name", font=("Arial Bold", 20))
f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window ")
    top.configure(bg='red')
    msg= Label(top,text= "Welcome to Pop Up ",font=("")).place()



btn = Button(window, text = "Click Me", bg= "black",fg='red' command= open_popup().pack())

btn.grid(column = 120 , row = 180)
f_name_box = Entry(window ,width=20)
s_name_box = Entry(window ,width=20)

f_name_box.grid(column = 100 , row = 100)
s_name_box.grid(column = 100 , row = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window ")
    top.configure(bg='red')
    msg= Label(top,text= "Welcome to Pop Up ",font=("")).place()
window.mainloop()



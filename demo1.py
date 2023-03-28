from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My First GUI")

btn1 = Button(window, text = "Click Me", fg = "Red" , bg="Yellow")
btn1.place(x=10, y=10)
txtfld = Entry(window, border = 10)
txtfld.place(x=100,y=100)

lbl = Label(window, text = "My First Demo")
lbl.place(x=50,y=50)

window.mainloop()
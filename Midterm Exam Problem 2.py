from tkinter import *
class MyWindow:
    def __init__(self,win):

        self.lbl0 = Label(win,text="My Full Name")
        self.lbl0.place(x=200,y=20)
        self.lbl1 = Label(win,text="Enter Given Name:")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "Enter Middle Name: ")
        self.lbl2.place(x=100,y=80)
        self.lbl3 = Label(win, text="Enter Last Name: ")
        self.lbl3.place(x=100,y=110)
        self.lbl4 = Label(win, text="My Full Name is: ")
        self.lbl4.place(x=100,y=150)
        self.txt1 = Entry(win,bd=2)
        self.txt1.place(x=300,y=50)
        self.txt2 = Entry(win,bd=2)
        self.txt2.place(x=300,y=80)
        self.txt3 = Entry(win,bd=2)
        self.txt3.place(x=300,y=110)
        self.txt4 = Entry(win,bd=2,width=30)
        self.txt4.place(x=300,y=150)
        self.btnfull = Button(win,text="Show Full Name", command = self.full)
        self.btnfull.place(x=200,y=175)


    def full(self):
        self.txt4.delete(0, 'end')
        given = str(self.txt1.get())
        middle = str(self.txt2.get())
        last = str(self.txt3.get())
        full = given+" "+middle+" "+last
        self.txt4.insert(END, str(full))


window = Tk()
mywin = MyWindow(window)
window.geometry("500x300+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()

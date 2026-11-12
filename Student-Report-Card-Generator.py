from tkinter import *
from tkinter.messagebox import askokcancel
win = Tk()

#==================================================================

def get_marks():
    student = name_entry.get().strip()
    maths = M.get()
    sst = SS.get()
    science = SC.get()
    eng = EN.get()
    hindi = H.get()

    total = maths+sst+science+eng+hindi
    per = total / 500 * 100
    div = ""
    if per <= 33:
        div = "Backbencher"
    elif per <=60:
        div = "Below Average"
    elif per <= 75:
        div = "Average"
    elif per <=90:
        div = "Above Average"
    else:
        div = "Topper"

    messagebox(student,total,per,div)
def messagebox(*data):
    print_1 = f"""
    NAME : {data[0]},
    TOTAL : {data[1]},
    PERCENTAGE : {data[2]}%,
    TYPE : {data[3]}
    """
    askokcancel(title="PERFECT CLASSES",
    message=print_1)

#==================================================================

win.config(bg="#fc7303")
win.title("Student-Report-Card-Generator")  

width = 600
height = 700
s_w = win.winfo_screenwidth()
s_h = win.winfo_screenheight()
c_x = int(s_w/2 - width/2)
c_y = int(s_h/2 - height/2)
win.geometry(f"{width}x{height}+{c_x}+{c_y}")
win.resizable(False,False)  

#==================================================================
l = Label(win,text="PERFECT CLASSES",font=("Elephant",35,"bold"),bg="#fc7303")
l.place(x=10,y=10,height=60,width=580) 

#==================================================================
name = Label(win,text="Student Name",font=("Elephant",23,"bold"))
name.place(x=10,y=90,height=60,width=290) 

NAME = StringVar()
name_entry = Entry(win,font=("Elephant",23,"bold"),textvariable=NAME)
name_entry.place(x=303,y=90,height=60,width=290)

#==================================================================
Marks = Label(win,text="MARKS",font=("Elephant",30,"bold"),bg="#fc7303")
Marks.place(x=10,y=170,height=60,width=580)  

#==================================================================
M = DoubleVar()
SS = DoubleVar()
SC = DoubleVar()
EN = DoubleVar()
H = DoubleVar()  

#==================================================================
subject = ["Maths","Social Science","Science","English","Hindi"]  

Maths = Label(win,text=subject[0],font=("Elephant",23,"bold"))
Maths.place(x=10,y=240,height=60,width=290)
Maths_entry = Entry(win,font=("Elephant",23,"bold"),textvariable=M)
Maths_entry.place(x=303,y=240,height=60,width=290) 

Sst = Label(win,text=subject[1],font=("Elephant",23,"bold"),)
Sst.place(x=10,y=310,height=60,width=290)
Sst_entry = Entry(win,font=("Elephant",23,"bold"),textvariable=SS)
Sst_entry.place(x=303,y=310,height=60,width=290)  

Science = Label(win,text=subject[2],font=("Elephant",23,"bold"),)
Science.place(x=10,y=380,height=60,width=290)
Science_entry = Entry(win,font=("Elephant",23,"bold"),textvariable=SC)
Science_entry.place(x=303,y=380,height=60,width=290)  

English = Label(win,text=subject[3],font=("Elephant",23,"bold"),)
English.place(x=10,y=450,height=60,width=290)
English_entry = Entry(win,font=("Elephant",23,"bold"),textvariable=EN)
English_entry.place(x=303,y=450,height=60,width=290)  

Hindi = Label(win,text=subject[4],font=("Elephant",23,"bold"),)
Hindi.place(x=10,y=520,height=60,width=290)
Hindi_entry = Entry(win,font=("Elephant",23,"bold"),textvariable=H)
Hindi_entry.place(x=303,y=520,height=60,width=290)  

#==================================================================
b = Button(win,text="DONE",font=("Elephant",23,"bold"),bg="#538eed",command=get_marks)
b.place(x=10,y=590,height=60,width=580)
 
#==================================================================

win.mainloop()
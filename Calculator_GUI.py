from tkinter import *


win=Tk()

win.geometry("240x300")
win.resizable(0,0)
data=StringVar()
val=""
Res=0
A=0
def One_Button():
  global val
  val=val+"1"
  data.set(val)
  
  
def two_Button():
  global val
  val=val+"2"
  data.set(val)
  
def three_Button():
  global val
  val=val+"3"
  data.set(val)

def four_Button():
  global val
  val=val+"4"
  data.set(val)

def five_Button():
  global val
  val=val+"5"
  data.set(val)

def six_Button():
  global val
  val=val+"6"
  data.set(val)

def seven_Button():
  global val
  val=val+"7"
  data.set(val)

def eight_Button():
  global val
  val=val+"8"
  data.set(val)

def nine_Button():
  global val
  val=val+"9"
  data.set(val)

def zero_Button():
  global val
  val=val+"0"
  data.set(val)

def plus_Button():
  global val,A,operator
  A=int(val)
  operator="+"
  val=val+"+"
  data.set(val)

def minus_Button():
  global val,A,operator
  A=int(val)
  operator="-"
  val=val+"-"
  data.set(val)

def divide_Button():
  global val,A,operator
  A=int(val)
  operator="/"
  val=val+"/"
  data.set(val)

def multiply_Button():
  global val,A,operator
  A=int(val)
  operator="*"
  val=val+"*"
  data.set(val)


def result():
  global val,A,operator,Res
  if(operator=="+"):
    B=int(val.split("+")[1])
    Res=A+B
    data.set(Res)
   
  if(operator=="-"):
    B=int(val.split("-")[1])
    Res=A-B
    data.set(Res)
  
  if(operator=="*"):
    B=int(val.split("*")[1])
    Res=A*B
    data.set(Res)
  
  if(operator=="/"):
    B=int(val.split("/")[1])
    if(B==0):
      data.set("ERROR")
    else:
      Res=A/B
      data.set(Res)
   
  
def clear():
  global val,A,operator
  val=""
  A=0
  operator=""
  data.set(val)
L=Label(win,textvariable=data,font=("Verdana",50),background="#FB9C0A",fg="black")
L.pack(expand=False,fill="both")

Frame1=Frame(win)
Frame1.pack()
Frame2=Frame(win)
Frame2.pack()
Frame3=Frame(win)
Frame3.pack()
Frame4=Frame(win)
Frame4.pack()


B1=Button(Frame1, text="1",width=2,height=2,command=One_Button)
B1.pack(side=LEFT)
B2=Button(Frame1, text="2",width=2,height=2,command=two_Button)
B2.pack(side=LEFT)
B3=Button(Frame1, text="3",width=2,height=2,command=three_Button)
B3.pack(side=LEFT)
B4=Button(Frame1, text="+",width=2,height=2,command=plus_Button)
B4.pack(side=LEFT)
B5=Button(Frame2, text="4",width=2,height=2,command=four_Button)
B5.pack(side=LEFT)
B6=Button(Frame2, text="5",width=2,height=2,command=five_Button)
B6.pack(side=LEFT)
B7=Button(Frame2, text="6",width=2,height=2,command=six_Button)
B7.pack(side=LEFT)
B8=Button(Frame2, text="-",width=2,height=2,command=minus_Button)
B8.pack(side=LEFT)
B9=Button(Frame3, text="7",width=2,height=2,command=seven_Button)
B9.pack(side=LEFT)
B10=Button(Frame3, text="8",width=2,height=2,command=eight_Button)
B10.pack(side=LEFT)
B11=Button(Frame3, text="9",width=2,height=2,command=nine_Button)
B11.pack(side=LEFT)
B12=Button(Frame3, text="*",width=2,height=2,command=multiply_Button)
B12.pack(side=LEFT)
B13=Button(Frame4, text="0",width=2,height=2,command=zero_Button)
B13.pack(side=LEFT)
B14=Button(Frame4, text="=",width=2,height=2,command=result)
B14.pack(side=LEFT)
B15=Button(Frame4, text="c",width=2,height=2,command=clear)
B15.pack(side=LEFT)
B16=Button(Frame4, text="/",width=2,height=2,command=divide_Button)
B16.pack(side=LEFT)


win.mainloop()

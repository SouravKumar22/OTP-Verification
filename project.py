import os
import math
import random
from re import sub
import smtplib 
from tkinter import *
from tokenize import String
OTP=""
m=Tk()
m.title("OTP Verification.")
e = StringVar()
o = StringVar()
l=[]
def submit():    
    email=e.get()
    digits="0123456789"
    OTP=" "
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    OTP=int(OTP)
    a = str(OTP) + " is your OTP"
    msg= a
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("smrtsourav13@gmail.com", 'gtqngyfajuligrff')
    s.sendmail('smrtsourav13@gmail.com',email,msg)
    print("OTP",OTP)
    l.append(OTP)
def verify():
    otp=o.get()
    otp=int(otp)
    print("OTP",OTP)
    print("otp",otp)
    if otp in l:
        g=Label(m,text="Verified..").place(relx=0.6,rely=0.09,anchor="center")
        l.clear()
    else:
        zx=Label(m,text="Not Verified..").place(relx=0.6,rely=0.09,anchor="center")


d=Label(m,text="Email").place(relx=0.5,rely=0.03,anchor="center")
r=Entry(m,textvariable=e,font=("calibri",12,"normal")).place(relx=0.6,rely=0.03,anchor="center")
b = Button(m,text='Send OTP',command=submit).place(relx=0.7,rely=0.03,anchor="center")
p = Button(m,text='Verify OTP',command=verify).place(relx=0.7,rely=0.07,anchor="center")
j=Label(m,text="OTP").place(relx=0.5,rely=0.07,anchor="center")
t=Entry(m,textvariable=o,font=("calibri",12,"normal")).place(relx=0.6,rely=0.07,anchor="center")
m.mainloop()
#tpoqiacshkqcsefr
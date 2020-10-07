from tkinter import * 
import datetime
from  PIL import Image,ImageTk  #import PIL library to our code


# image=Image.open("age.png")
# image.thumbnail((300,300),Image.ANTIALIAS)
#ANTIALIAS  helps to deals some problems while using images
photo=ImageTk.PhotoImage(file=r'age.png')   #converts the image to the tinker image
label_image=Label(image=photo)   #stores the image in the label
label_image.grid(row=0,column=1)

def age_ratio():
    # n=today()
    d=datetime.date.today()
    d2=datetime.date(int(year_text.get()),int(month_text.get()),int(day_text.get()))
    delta=d-d2
    age=delta.days/365
    # print(d)
    # d3=datetime.timedelta(d-d2)
    # dt=datetime.datetime.year(int(year_text.get()),int(month_text.get()),int(day_text.get()))
    print("Hi "+name_text.get().upper() +" your age is....."+str(age))



window=Tk()
window.title("Age Calculator")
"""
only taks remaining lgic and image import
"""

l1=Label(window,text="Name")
l1.grid(row=6,column=2)

l2=Label(window,text="Year")
l2.grid(row=7,column=2)
l3=Label(window,text="Month")
l3.grid(row=8,column=2)
l4=Label(window,text="Day")
l4.grid(row=9,column=2)

name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=6,column=4)

year_text=StringVar()
e2=Entry(window,textvariable=year_text)
e2.grid(row=7,column=4)

month_text=StringVar()
e3=Entry(window,textvariable=month_text)
e3.grid(row=8,column=4)

day_text=StringVar()
e4=Entry(window,textvariable=day_text)
e4.grid(row=9,column=4)


b1=Button(window,text="Calculate Age",width=12,command=age_ratio,bg="Pink")
b1.grid(row=10, column=3)

window.mainloop()
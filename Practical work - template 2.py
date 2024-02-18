from tkinter import*

root = Tk ()
root.title ('domashka')
root.geometry ('500x300')
root.configure(cursor='pencil')

lb= Label(root,text='Сколько штук?', font='Arial 11')
lb.pack ()

var=IntVar()
var.set(1)
rad0 = Radiobutton (root,text='0-10', variable=var, value=0)
rad1 = Radiobutton (root,text='11-20', variable=var, value=1)
rad2 = Radiobutton (root,text='21-30', variable=var, value=2)
rad3 = Radiobutton (root,text='31-40', variable=var, value=3)
rad0.pack()
rad1.pack()
rad2.pack()
rad3.pack()

lb= Label(root,text='Какого цвета?', font='Arial 11')
lb.pack ()

v1= IntVar()
v2= IntVar()
v3= IntVar()
v4= IntVar()
ch1  = Checkbutton(root,text="Red", bg='red', variable=v1, onvalue=1, offvalue=0)
ch2  = Checkbutton(root,text="Blue", bg='blue', variable=v2, onvalue=2, offvalue=0)
ch3  = Checkbutton(root,text="Green", bg='green', variable=v3, onvalue=3, offvalue=0)
ch4  = Checkbutton(root,text="Yellow", bg='yellow', variable=v4, onvalue=4, offvalue=0)
ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()

root.mainloop()
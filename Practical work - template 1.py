from tkinter import*
root=Tk()
root.title('Vhod')
root.geometry('400x250')
root.configure(bg='#ccc', cursor='pencil')

lbl = Label (root,text='Ваш адрес:', bg='gainsboro', bd= '4', font='Arial 10', fg='#252525')
lbl.pack ()

tex = Text (root, bg='#ddd', width='20', height='0.5', bd=3, font= 'Arial 8')
tex.pack()

lbl = Label (root,text='Коментарий:', bg='#ccc', bd= '0', font='Arial 10', fg='#252525')
lbl.pack ()

tex = Text (root, bg='#eee', width='30', height='7', bd=2, font= 'Arial 8')
tex.pack()

btn= Button (root, bd=3, bg='#0282cc', text='Отправить', font= 'Arial 11', width='15')
btn.pack()

root.mainloop()

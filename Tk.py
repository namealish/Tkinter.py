from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import  Menu
from tkinter import ttk
from tkinter import filedialog
import pandas as pd



def clicked():
    res = "Hi{}".format(txt.get())
    lbl.configure(text=res)

room =Tk()
room ['bg'] = '#fafafa'
room.title('Far cry')
menu = Menu(room)
new_item = Menu(menu)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Открыть')
new_item.add_separator()
new_item.add_command(label='Сохранить')
menu.add_cascade(label='Файл', menu=new_item)
room.configure(menu=menu)
lbl = Label(room, text="Klient")
lbl.grid(column=0, row=1)
txt = Entry(room, width=10)
txt.grid(column=4, row=1)
combo = Combobox(room)
combo['values'] = (1,2,3,4,5,)
combo.current()
combo.grid(column=2, row=1)
btn = Button(room, text="Нажать", bg='blue', fg='orange', command=clicked)
btn.grid(column=3, row=1)
room.wm_attributes('-alpha', 1)
room.geometry('300x250')
ttk.Label(room, text="Add Excel File :").grid(row=0, column=0, padx=20, pady=20)
open_file = ttk.Button(room, text="Open files")
open_file.grid(row=0, column=1, columnspan=2, padx=20, pady=20)
box_red_path = ttk.Label(room, text="")
box_red_path.grid(row=1, column=1, columnspan=4, padx=20, pady=20)


def upload_excel():
    filename = filedialog.askopenfilename(title="Select a File", filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))

    path = filename

    box_red_path.configure(text=path)


open_file.config(command=upload_excel)


room.mainloop()
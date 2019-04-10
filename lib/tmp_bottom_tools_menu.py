import tkinter as tk
from tkinter import ttk

class tools_bar_tm():
    
    def __init__(self,pl,ax=0,ay=0):

        self.__place=pl
        self.__ax_start=ax
        self.__ay_start=ay 
        self.cl_list=(("Черный",'black'), ("Белый",'white'),
                     ('Красный','red'),("Оранжевый",'orange'),
                     ("Желтый",'yellow'), ("Зеленый",'green'), 
                     ("Фиолетовый",'purple'))
        self.colors=[ "Черный", "Белый",'Красный',"Оранжевый","Желтый", "Зеленый", "Фиолетовый"]
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.map('prim-second.TCombobox', fieldbackground=[('readonly','white')])
        self.style.map('prim-second.TCombobox', foreground=[('readonly','black')])
    
    def set_style(self,color):
        #self.style.map('prim-second.TCombobox', fieldbackground=[('readonly','green')])
        print(color)
        self.style.map('prim-second.TCombobox', foreground=[('readonly',color)])

    def on_select(self,*kward):
        self.set_style(self.cl_list[self.cb.current()][1])

    def create(self,):
        
        self.cb = ttk.Combobox(self.__place, values=self.colors,style='prim-second.TCombobox')
        self.cb.set(self.colors[0])
        self.cb['state'] = 'readonly'
        self.cb.grid(row=self.__ax_start, column=self.__ay_start)
        self.cb.bind('<<ComboboxSelected>>', self.on_select)

 
 
root=tk.Tk()
root.title(u'toolbar_exemp')
root.geometry('430x380+50+100')

root.resizable(True, True)

createtb=tools_bar_tm(root)
createtb.create()
print ('ok')
root.mainloop()
print ('main exit')
'''
def skillUsed():
    if chkUsedVar.get() == 1:
        style.map('custom.TCombobox', fieldbackground=[('readonly','green')])
        style.map('custom.TCombobox', foreground=[('readonly','red')])
    else:
        style.map('custom.TCombobox', fieldbackground=[('readonly','white')])
        style.map('custom.TCombobox', foreground=[('readonly','black')])

root = tk.Tk()

style = ttk.Style()
style.theme_use('alt')

cboxVar1 = tk.StringVar()
cboxVar1.set("spam")

cboxVar2 = tk.StringVar()
cboxVar2.set("silly")

chkUsedVar = tk.IntVar()
chk = tk.Checkbutton(root, text='Used', variable=chkUsedVar, command=skillUsed)
chk.grid(row=0, column=2)

combo01 = ttk.Combobox(root, values=['spam', 'eric', 'moose'], textvariable=cboxVar1)
combo01['state'] = 'readonly'
combo01.grid(row=0, column=0)

combo02 = ttk.Combobox(root, values=['parrot', 'silly', 'walk'], textvariable=cboxVar2, style='custom.TCombobox')
combo02['state'] = 'readonly'
combo02.grid(row=0, column=1)

root.mainloop()
'''
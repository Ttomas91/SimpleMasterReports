from tkinter import Tk , Frame
import os
import sys

main_pach=os.getcwd()
lib_pach=main_pach+'/lib/'

class add_path():
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        sys.path.remove(self.path)

with add_path(lib_pach):
    tools_menu = __import__("tools_menu")

print ()
root=Tk()
root.title(u'toolbar_exemp')
root.geometry('430x380+50+100')

root.resizable(True, True)
menu=Frame(root,bd=1)
createtb=tools_menu.tools_bar(menu,main_pach)
createtb.init()
createtb.creates()
createtb.builds()
menu.grid(row=0,column=0)
print ('ok')
root.mainloop()
print ('main exit')

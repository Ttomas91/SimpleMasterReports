from tkinter import Tk 
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

createtb=tools_menu.tools_bar(root,main_pach)
createtb.init()
createtb.creates()
createtb.builds()
print ('ok')
root.mainloop()
print ('main exit')

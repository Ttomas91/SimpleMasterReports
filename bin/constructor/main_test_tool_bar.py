from tkinter import Tk , Frame, Label
import os
import sys
import random
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
root.geometry('400x200+50+100')

root.resizable(True, True)
menu=Frame(root,bd=1)
createtb=tools_menu.tools_bar(menu,main_pach)
createtb.init()
createtb.creates()
createtb.builds()
menu.grid(row=0,column=0,sticky =  "w")

def f1(*arg):
    dict=createtb.gets()
    print (dict)
lists=['text_in','text_s','fone_c','text_c']
def f2(*arg):
    dict=createtb.gets()
    for x in dict:
        for b in dict[x]:
            if x in lists:
                dict[x][b] = random.randrange(0,7,1)
            else:
                dict[x][b] = random.randrange(0,2,1)
    createtb.sets(dict)

tmp_place=Frame(root,bd=1)
bit=Label(tmp_place, text='ok',width=10,height=3)
                    
bit.grid(row=0,column=0,sticky =  "w")
                    
bit.bind('<Button-1>', f2)
bit.bind('<Button-3>', f1)
tmp_place.grid(row=1,column=0,sticky =  "w")

print ('ok')
root.mainloop()
print ('main exit')

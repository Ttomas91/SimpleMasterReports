from tkinter import Label
from PIL import ImageTk

class tools_bar():
    
    
    def __init__(self,pl,main_path):

        self.place=pl
        self.icon_patch=main_path+'/icons/'
        mask_to=[[0 for y in range(11)]for x in range(2)]

        self.but_border_up=self.factory_objects(
            0,1,1,1,
            ImageTk.PhotoImage(file=self.icon_patch+'up_border_null'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'up_border_solid'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'up_border_solid'+'.png'),
            self.f_bord_up,)
        
        self.but_border_all=self.factory_objects(
            0,2,1,1,
            ImageTk.PhotoImage(file=self.icon_patch+'all_border_null'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'all_border_solid'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'all_border_solid'+'.png'),
            self.f_bord_all,)

        self.but_border_left=self.factory_objects(
            1,0,1,1,
            ImageTk.PhotoImage(file=self.icon_patch+'left_border_null'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'left_border_solid'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'left_border_solid'+'.png'),
            self.f_bord_left,)

        self.but_border_down=self.factory_objects(
            1,1,1,1,
            ImageTk.PhotoImage(file=self.icon_patch+'down_border_null'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'down_border_solid'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'down_border_solid'+'.png'),
            self.f_bord_down,)

        self.but_border_right=self.factory_objects(
            1,2,1,1,
            ImageTk.PhotoImage(file=self.icon_patch+'right_border_null'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'right_border_solid'+'.png'),
            ImageTk.PhotoImage(file=self.icon_patch+'right_border_solid'+'.png'),
            self.f_bord_right,)

        
        
        mask_to[0][3]=[ImageTk.PhotoImage(file=self.icon_patch+'top_text_ax1_select'+'.png'),ImageTk.PhotoImage(file=self.icon_patch+'top_text_ax1'+'.png'),self.f_text_v_up]
        mask_to[0][4]=[ImageTk.PhotoImage(file=self.icon_patch+'centre_text_ax1_select'+'.png'),ImageTk.PhotoImage(file=self.icon_patch+'centre_text_ax1'+'.png'),self.f_text_v_centr]
        mask_to[0][5]=[ImageTk.PhotoImage(file=self.icon_patch+'bottom_text_ax1_select'+'.png'),ImageTk.PhotoImage(file=self.icon_patch+'bottom_text_ax1'+'.png'),self.f_text_v_down]
        mask_to[0][7]=[1,ImageTk.PhotoImage(file=self.icon_patch+'up'+'.png'),self.f_join_up]
        
        mask_to[1][3]=[ImageTk.PhotoImage(file=self.icon_patch+'left_text_ax0_select'+'.png'),ImageTk.PhotoImage(file=self.icon_patch+'left_text_ax0'+'.png'),self.f_text_h_left]
        mask_to[1][4]=[ImageTk.PhotoImage(file=self.icon_patch+'centre_text_ax0_select'+'.png'),ImageTk.PhotoImage(file=self.icon_patch+'centre_text_ax0'+'.png'),self.f_text_h_centr]
        mask_to[1][5]=[ImageTk.PhotoImage(file=self.icon_patch+'right_text_ax0_select'+'.png'),ImageTk.PhotoImage(file=self.icon_patch+'right_text_ax0'+'.png'),self.f_text_h_right]
        mask_to[1][6]=[1,ImageTk.PhotoImage(file=self.icon_patch+'left'+'.png'),self.f_join_left]
        mask_to[1][7]=[1,ImageTk.PhotoImage(file=self.icon_patch+'down'+'.png'),self.f_join_down]
        mask_to[1][8]=[1,ImageTk.PhotoImage(file=self.icon_patch+'right'+'.png'),self.f_join_right]

        
        self.mask_tool=mask_to

    def factory_objects(self,ax,ay,len_ax,len_ay,i_0,i_1,i_2,func,*a_key):
        ob={}
        ob['ax']=ax
        ob['ay']=ay
        ob['len_ax']=len_ax
        ob['len_ay']=len_ay
        ob['icon_0']=i_0
        ob['icon_1']=i_1
        ob['icon_2']=i_2
        ob['func']=func
        for x in range(len(a_key)):
            ob['a_key_'+str(x)]=a_key[x]
        
        return ob

    def f_bord_up(self,*key):
        if self.mask_tool[0][1][-2]==0:
            self.mask_tool[0][1][-2]=1
            self.mask_tool[0][1][-1].configure(image=self.mask_tool[0][1][0])

            if self.mask_tool[0][1][-2]==1 and self.mask_tool[1][0][-2]==1 and self.mask_tool[1][1][-2]==1 and self.mask_tool[1][2][-2]==1 :
                self.mask_tool[0][2][-2]=1
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][0])
            else:
                self.mask_tool[0][2][-2]=0
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])

        else:
            self.mask_tool[0][1][-2]=0
            self.mask_tool[0][1][-1].configure(image=self.mask_tool[0][1][1])
            self.mask_tool[0][2][-2]=0
            self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])
        
    def f_bord_left(self,*key):
        if self.mask_tool[1][0][-2]==0:
            self.mask_tool[1][0][-2]=1
            self.mask_tool[1][0][-1].configure(image=self.mask_tool[1][0][0])

            if self.mask_tool[0][1][-2]==1 and self.mask_tool[1][0][-2]==1 and self.mask_tool[1][1][-2]==1 and self.mask_tool[1][2][-2]==1 :
                self.mask_tool[0][2][-2]=1
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][0])
            else:
                self.mask_tool[0][2][-2]=0
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])

        else :
            self.mask_tool[1][0][-2]=0
            self.mask_tool[1][0][-1].configure(image=self.mask_tool[1][0][1])
            self.mask_tool[0][2][-2]=0
            self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])
        
    def f_bord_right(self,*key):
        if self.mask_tool[1][2][-2]==0:
            self.mask_tool[1][2][-2]=1
            self.mask_tool[1][2][-1].configure(image=self.mask_tool[1][2][0])

            if self.mask_tool[0][1][-2]==1 and self.mask_tool[1][0][-2]==1 and self.mask_tool[1][1][-2]==1 and self.mask_tool[1][2][-2]==1 :
                self.mask_tool[0][2][-2]=1
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][0])
            else:
                self.mask_tool[0][2][-2]=0
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])

        else :
            self.mask_tool[1][2][-2]=0
            self.mask_tool[1][2][-1].configure(image=self.mask_tool[1][2][1])
            self.mask_tool[0][2][-2]=0
            self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])

    def f_bord_down(self,*key):
        if self.mask_tool[1][1][-2]==0:
            self.mask_tool[1][1][-2]=1
            self.mask_tool[1][1][-1].configure(image=self.mask_tool[1][1][0])

            if self.mask_tool[0][1][-2]==1 and self.mask_tool[1][0][-2]==1 and self.mask_tool[1][1][-2]==1 and self.mask_tool[1][2][-2]==1 :
                self.mask_tool[0][2][-2]=1
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][0])
            else:
                self.mask_tool[0][2][-2]=0
                self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])

        else :
            self.mask_tool[1][1][-2]=0
            self.mask_tool[1][1][-1].configure(image=self.mask_tool[1][1][1])
            self.mask_tool[0][2][-2]=0
            self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])
        
    def f_bord_all(self,*key):
        if self.mask_tool[0][2][-2]==0:
            self.mask_tool[0][2][-2]=1
            self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][0])

            if self.mask_tool[0][1][-2]==0:
                self.f_bord_up()
            if self.mask_tool[1][0][-2]==0:
                self.f_bord_left()
            if self.mask_tool[1][2][-2]==0:
                self.f_bord_right()
            if self.mask_tool[1][1][-2]==0:
                self.f_bord_down()

        else :
            if self.mask_tool[0][1][-2]==1:
                self.f_bord_up()
            if self.mask_tool[1][0][-2]==1:
                self.f_bord_left()
            if self.mask_tool[1][2][-2]==1:
                self.f_bord_right()
            if self.mask_tool[1][1][-2]==1:
                self.f_bord_down()

            self.mask_tool[0][2][-2]=0
            self.mask_tool[0][2][-1].configure(image=self.mask_tool[0][2][1])
        


    def f_text_v_up(self,*key):
        if self.mask_tool[0][3][-2]==0:
            self.mask_tool[0][3][-2]=1
            self.mask_tool[0][3][-1].configure(image=self.mask_tool[0][3][0])
            self.mask_tool[0][4][-2]=0
            self.mask_tool[0][4][-1].configure(image=self.mask_tool[0][4][1])
            self.mask_tool[0][5][-2]=0
            self.mask_tool[0][5][-1].configure(image=self.mask_tool[0][5][1])
        else:
            self.mask_tool[0][3][-2]=0
            self.mask_tool[0][3][-1].configure(image=self.mask_tool[0][3][1])
        
    def f_text_v_centr(self,*key):
        if self.mask_tool[0][4][-2]==0:
            self.mask_tool[0][4][-2]=1
            self.mask_tool[0][4][-1].configure(image=self.mask_tool[0][4][0])
            self.mask_tool[0][3][-2]=0
            self.mask_tool[0][3][-1].configure(image=self.mask_tool[0][3][1])
            self.mask_tool[0][5][-2]=0
            self.mask_tool[0][5][-1].configure(image=self.mask_tool[0][5][1])
        else:
            self.mask_tool[0][4][-2]=0
            self.mask_tool[0][4][-1].configure(image=self.mask_tool[0][4][1])

    def f_text_v_down(self,*key):
        if self.mask_tool[0][5][-2]==0:
            self.mask_tool[0][5][-2]=1
            self.mask_tool[0][5][-1].configure(image=self.mask_tool[0][5][0])
            self.mask_tool[0][3][-2]=0
            self.mask_tool[0][3][-1].configure(image=self.mask_tool[0][3][1])
            self.mask_tool[0][4][-2]=0
            self.mask_tool[0][4][-1].configure(image=self.mask_tool[0][4][1])
        else:
            self.mask_tool[0][5][-2]=0
            self.mask_tool[0][5][-1].configure(image=self.mask_tool[0][5][1])

        
    def f_join_up(self,*key):
        print('test ',key,5)
        
    def f_text_h_left(self,*key):
        if self.mask_tool[1][3][-2]==0:
            self.mask_tool[1][3][-2]=1
            self.mask_tool[1][3][-1].configure(image=self.mask_tool[1][3][0])
            self.mask_tool[1][4][-2]=0
            self.mask_tool[1][4][-1].configure(image=self.mask_tool[1][4][1])
            self.mask_tool[1][5][-2]=0
            self.mask_tool[1][5][-1].configure(image=self.mask_tool[1][5][1])
        else:
            self.mask_tool[1][3][-2]=0
            self.mask_tool[1][3][-1].configure(image=self.mask_tool[1][3][1])
        
    def f_text_h_centr(self,*key):
        if self.mask_tool[1][4][-2]==0:
            self.mask_tool[1][4][-2]=1
            self.mask_tool[1][4][-1].configure(image=self.mask_tool[1][4][0])
            self.mask_tool[1][3][-2]=0
            self.mask_tool[1][3][-1].configure(image=self.mask_tool[1][3][1])
            self.mask_tool[1][5][-2]=0
            self.mask_tool[1][5][-1].configure(image=self.mask_tool[1][5][1])
        else:
            self.mask_tool[1][4][-2]=0
            self.mask_tool[1][4][-1].configure(image=self.mask_tool[1][4][1])

    def f_text_h_right(self,*key):
        if self.mask_tool[1][5][-2]==0:
            self.mask_tool[1][5][-2]=1
            self.mask_tool[1][5][-1].configure(image=self.mask_tool[1][5][0])
            self.mask_tool[1][3][-2]=0
            self.mask_tool[1][3][-1].configure(image=self.mask_tool[1][3][1])
            self.mask_tool[1][4][-2]=0
            self.mask_tool[1][4][-1].configure(image=self.mask_tool[1][4][1])
        else:
            self.mask_tool[1][5][-2]=0
            self.mask_tool[1][5][-1].configure(image=self.mask_tool[1][5][1])

    def f_join_left(self,*key):
        print('test ',key,12)
    def f_join_right(self,*key):
        print('test ',key,13)


    def f_join_down(self,*key):
        print('test ',key,15)

    def create(self, ):
        for n in range(len(self.mask_tool)):
            for m in range(len(self.mask_tool[n])):
                if isinstance( self.mask_tool[n][m], list)==True:
                    tmp=self.mask_tool[n][m]
                    bit=Label(self.place, image=tmp[1])
                    
                    bit.grid(row=n,column=m)
                    
                    bit.bind('<Button-1>', tmp[2])
                    bit.bind('<Button-2>', tmp[2])

                    self.mask_tool[n][m].append(0)

                    self.mask_tool[n][m].append(bit)



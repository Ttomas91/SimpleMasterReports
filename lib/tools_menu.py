from tkinter import Label,Frame
from tkinter import ttk
from PIL import ImageTk

class tools_bar():
    
    def __init__(self,pl,main_pach,ax=0,ay=0):

        self.__place=pl
        self.__f_place=Frame(self.__place,bd=1)
        self.__s_place=Frame(self.__place,bd=1)
        self.__icon_patch=main_pach+'/icons/'
        self.__ax_start=ax
        self.__ay_start=ay 

    class button_sub_menu():

        li_obj=[]

        def __init__(self,pl,pos_ax,pos_ay,ic_pach):
            self.s_plase=pl
            self.s_ax=pos_ax
            self.s_ay=pos_ay
            self.ico_pach=ic_pach

        def factory_objects(self,name,ax,ay,len_ax,len_ay,i_0,i_1,i_2,func,*a_key,**k_key,):

            ob={}
            ob['name']=name
            ob['ax']=self.s_ax+ax
            ob['ay']=self.s_ay+ay
            ob['len_ax']=len_ax
            ob['len_ay']=len_ay
            ob['icon_0']=ImageTk.PhotoImage(file=self.ico_pach+i_0+'.png')
            ob['icon_1']=ImageTk.PhotoImage(file=self.ico_pach+i_1+'.png')
            ob['icon_2']=ImageTk.PhotoImage(file=self.ico_pach+i_2+'.png')
            ob['func_b1']=func

            for x in range(len(a_key)):
                ob['a_key_'+str(x)]=a_key[x]

            for x in k_key:
                ob[x]=k_key[x]

            return ob
        
        def build(self,):

            for x in self.li_obj:
                
                bit=Label(self.s_plase, image=x['icon_0'])
                    
                bit.grid(row=x['ax'],column=x['ay'],rowspan=x['len_ax'],columnspan=x['len_ay'],)
                    
                bit.bind('<Button-1>', x['func_b1'])

                x['status']=0

                x['object']=bit

    class borders(button_sub_menu):

        def create(self,):
            up=self.factory_objects(
                name='up',
                ax=0,
                ay=1,
                len_ax=1,
                len_ay=1,
                i_0='up_border_null',
                i_1='up_border_solid',
                i_2='up_border_solid',
                func=self.f_bord_up )
        
            all=self.factory_objects(
                name='all',
                ax=0,
                ay=2,
                len_ax=1,
                len_ay=1,
                i_0='all_border_null',
                i_1='all_border_solid',
                i_2='all_border_solid',
                func=self.f_bord_all,)

            left=self.factory_objects(
                name='left',
                ax=1,
                ay=0,
                len_ax=1,
                len_ay=1,
                i_0='left_border_null',
                i_1='left_border_solid',
                i_2='left_border_solid',
                func=self.f_bord_left)

            down=self.factory_objects(
                name='down',
                ax=1,
                ay=1,
                len_ax=1,
                len_ay=1,
                i_0='down_border_null',
                i_1='down_border_solid',
                i_2='down_border_solid',
                func=self.f_bord_down)

            right=self.factory_objects(
                name='right',
                ax=1,
                ay=2,
                len_ax=1,
                len_ay=1,
                i_0='right_border_null',
                i_1='right_border_solid',
                i_2='right_border_solid',
                func=self.f_bord_right)
            
            self.li_obj=[up,left,down,right,all,]
        
        def __chec_all(self,):
            df=True
            for v in self.li_obj:
                if v['name']!='all':
                    if v['status']!=1:
                        df=False
            if df==True:
                self.__all_stat('all',tf=1)
        
        def __all_stat(self,name,tf):

            for b in self.li_obj:
                if b['name']==name:

                    b['status']=tf

                    if b['status']==0:

                        b['object'].configure(image=b['icon_0'])

                    elif b['status']==1:

                        b['object'].configure(image=b['icon_1'])

        def __solo_status(self,ob_name):

            for x in self.li_obj:
                if x['name']==ob_name:

                    if ob_name=='all':
                        if x['status']==0:
                            x['status']=1
                            x['object'].configure(image=x['icon_1'])                         

                        elif x['status']==1:
                            x['status']=0
                            x['object'].configure(image=x['icon_0'])
                        for n in self.li_obj:
                            if n['name']!='all':
                                self.__all_stat(n['name'],x['status'])

                    else:
                        if x['status']==0:
                            x['status']=1
                            x['object'].configure(image=x['icon_1'])
                            self.__chec_all()

                        elif x['status']==1:
                            x['status']=0
                            x['object'].configure(image=x['icon_0'])
                            self.__all_stat('all',0)

        def f_bord_up(self,*key):
            self.__solo_status('up')
        
        def f_bord_left(self,*key):
            self.__solo_status('left')
        
        def f_bord_right(self,*key):
            self.__solo_status('right')

        def f_bord_down(self,*key):
            self.__solo_status('down')
        
        def f_bord_all(self,*key):
            self.__solo_status('all')
        
    class join(button_sub_menu):

        def create(self,):    
            up=self.factory_objects(
                name='up',
                ax=0,
                ay=1,
                len_ax=1,
                len_ay=1,
                i_0='up',
                i_1='up',
                i_2='up',
                func=self.f_join_up,
                )

            left=self.factory_objects(
                name='left',
                ax=1,
                ay=0,
                len_ax=1,
                len_ay=1,
                i_0='left',
                i_1='left',
                i_2='left',
                func=self.f_join_left,)

            down=self.factory_objects(
                name='down',
                ax=1,
                ay=1,
                len_ax=1,
                len_ay=1,
                i_0='down',
                i_1='down',
                i_2='down',
                func=self.f_join_down,)

            right=self.factory_objects(
                name='right',
                ax=1,
                ay=2,
                len_ax=1,
                len_ay=1,
                i_0='right',
                i_1='right',
                i_2='right',
                func=self.f_join_right,)
            
            self.li_obj=[up,left,down,right,]

        def f_join_left(self,*key):
            print('test Button left')
            
        def f_join_right(self,*key):
            print('test Button right')

        def f_join_up(self,*key):
            print('test Button up')

        def f_join_down(self,*key):
            print('test Button down')
        
    class text_v(button_sub_menu):
        
        def create(self,):    

            top=self.factory_objects(
                name='top',
                ax=0,
                ay=0,
                len_ax=1,
                len_ay=1,
                i_0='top_text_ax1',
                i_1='top_text_ax1_select',
                i_2='top_text_ax1_select',
                func=self.f_text_v_top,
                )

            centr=self.factory_objects(
                name='centr',
                ax=0,
                ay=1,
                len_ax=1,
                len_ay=1,
                i_0='centre_text_ax1',
                i_1='centre_text_ax1_select',
                i_2='centre_text_ax1_select',
                func=self.f_text_v_centr,)

            bottom=self.factory_objects(
                name='bottom',
                ax=0,
                ay=2,
                len_ax=1,
                len_ay=1,
                i_0='bottom_text_ax1',
                i_1='bottom_text_ax1_select',
                i_2='bottom_text_ax1_select',
                func=self.f_text_v_bottom,)
            
            self.li_obj=[top,centr,bottom]

        def __set_status(self,name,st):                
            for b in self.li_obj:
                if b['name']!=name:
                    b['status']=st
                    if st==0:
                        b['object'].configure(image=b['icon_0'])
                    elif st==1:
                        b['object'].configure(image=b['icon_1'])


        def __event(self,name):
            for x in self.li_obj:
                if x['name']==name:
                    if x['status']==0:
                        x['status']=1
                        x['object'].configure(image=x['icon_1'])
                        self.__set_status(name,0)
                    elif x['status']==1:
                        x['status']=0
                        x['object'].configure(image=x['icon_0'])


        def f_text_v_top(self,*key):
            self.__event('top')
            
        def f_text_v_centr(self,*key):
            self.__event('centr')

        def f_text_v_bottom(self,*key):
            self.__event('bottom')
         
    class text_h(text_v):
        
        def create(self,):  

            left=self.factory_objects(
                name='left',
                ax=0,
                ay=0,
                len_ax=1,
                len_ay=1,
                i_0='left_text_ax0',
                i_1='left_text_ax0_select',
                i_2='left_text_ax0_select',
                func=self.f_text_h_left,
                )

            centr=self.factory_objects(
                name='centr',
                ax=0,
                ay=1,
                len_ax=1,
                len_ay=1,
                i_0='centre_text_ax0',
                i_1='centre_text_ax0_select',
                i_2='centre_text_ax0_select',
                func=self.f_text_h_centr,)

            right=self.factory_objects(
                name='right',
                ax=0,
                ay=2,
                len_ax=1,
                len_ay=1,
                i_0='right_text_ax0',
                i_1='right_text_ax0_select',
                i_2='right_text_ax0_select',
                func=self.f_text_h_right,)
            
            self.li_obj=[left,centr,right]

        def __set_status(self,name,st):                
            for b in self.li_obj:
                if b['name']!=name:
                    b['status']=st
                    if st==0:
                        b['object'].configure(image=b['icon_0'])
                    elif st==1:
                        b['object'].configure(image=b['icon_1'])


        def __event(self,name):
            for x in self.li_obj:
                if x['name']==name:
                    if x['status']==0:
                        x['status']=1
                        x['object'].configure(image=x['icon_1'])
                        self.__set_status(name,0)
                    elif x['status']==1:
                        x['status']=0
                        x['object'].configure(image=x['icon_0'])
        
        def f_text_h_left(self,*key):
                self.__event('left')
            
        def f_text_h_centr(self,*key):
                self.__event('centr')

        def f_text_h_right(self,*key):
                self.__event('right')
    
    class cb_sub_menu():

        li_obj=[]

        def __init__(self,pl,pos_ax,pos_ay):
            self.s_plase=pl
            self.s_ax=pos_ax
            self.s_ay=pos_ay
            self.cl_list=(("Черный",'black'), ("Белый",'white'),
                        ('Красный','red'),("Оранжевый",'orange'),
                        ("Желтый",'yellow'), ("Зеленый",'green'), 
                        ("Фиолетовый",'purple'))
            self.colors=[ "Черный", "Белый",'Красный',"Оранжевый","Желтый", "Зеленый", "Фиолетовый"]
            self.style = ttk.Style()
            self.style.theme_use('alt')
            self.style.map('prim-second.TCombobox', fieldbackground=[('readonly','white')])
            self.style.map('prim-second.TCombobox', foreground=[('readonly','black')])
            self.style.map('main.TCombobox', fieldbackground=[('readonly','white')])
            self.style.map('main.TCombobox', foreground=[('readonly','black')])

        def factory_objects(self,name,lists,stat,witch,ax,ay,len_ax,len_ay,func,styles,*a_key,**k_key,):

            ob={}
            ob['name']=name
            ob['list']=lists
            ob['status']=stat
            ob['witch']=witch
            ob['ax']=self.s_ax+ax
            ob['ay']=self.s_ay+ay
            ob['len_ax']=len_ax
            ob['len_ay']=len_ay
            ob['func_b1']=func
            ob['styl']=styles

            for x in range(len(a_key)):
                ob['a_key_'+str(x)]=a_key[x]

            for x in k_key:
                ob[x]=k_key[x]

            return ob
        
        def build(self,):

            for x in self.li_obj:
                
                bit=ttk.Combobox(self.s_plase, values=x['list'],style=x['styl'],width=x['witch'])
                bit.set(x['list'][x['status']])    
                bit.grid(row=x['ax'],column=x['ay'],rowspan=x['len_ax'],columnspan=x['len_ay'],)
                    
                bit['state'] = 'readonly'
                bit.bind('<<ComboboxSelected>>', x['func_b1'])

                x['object']=bit
        
        def create(self,):  


            self.text_c=self.factory_objects(
                name='text_c',
                lists=self.colors,#[ 'text' for x in self.cl_list],
                stat=0,
                witch=10,
                ax=0,
                ay=0,
                len_ax=1,
                len_ay=2,
                func=self.f_text_colors,
                styles='prim-second.TCombobox'
                )

            self.fone_c=self.factory_objects(
                name='fone_c',
                lists=self.colors,#[ 'fone' for x in self.cl_list],
                stat=1,
                witch=10,
                ax=0,
                ay=2,
                len_ax=1,
                len_ay=2,
                func=self.f_fone_colors,
                styles='prim-second.TCombobox')

            self.fronts=self.factory_objects(
                name='fronts',
                lists=['arial', 'timenewroman',],
                stat=0,
                witch=15,
                ax=0,
                ay=4,
                len_ax=1,
                len_ay=3,
                func=self.f_fronts,
                styles='main.TCombobox')

            self.text_s=self.factory_objects(
                name='text_s',
                lists=[x for x in range(8,25,2)],
                stat=3,
                witch=5,
                ax=0,
                ay=7,
                len_ax=1,
                len_ay=2,
                func=self.f_text_s,
                styles='main.TCombobox')
            
            self.li_obj=[self.text_c,self.fone_c,self.fronts,self.text_s]
    
        def __set_style(self,type,color):
            if type=='txt':
                self.style.map('prim-second.TCombobox', foreground=[('readonly',color)])
            elif type=='ground':
                self.style.map('prim-second.TCombobox', fieldbackground=[('readonly',color)])
            
            
        
        def f_text_colors(self,*kvar):
            self.__set_style('txt',self.cl_list[self.text_c['object'].current()][1])
            pass
        def f_fone_colors(self,*kvar):
            self.__set_style('ground',self.cl_list[self.fone_c['object'].current()][1])
            pass
        def f_fronts(self,*kvar):
            print(self.fronts['object'].get())
            pass
        def f_text_s(self,*kvar):
            print(self.text_s['object'].get())
            pass

    def init(self,):
        self._bord=self.borders(pl=self.__f_place,
                          ic_pach = self.__icon_patch,
                          pos_ax = self.__ax_start+0,
                          pos_ay = self.__ay_start+0,)
        self._t_ax1=self.text_v(pl=self.__f_place,
                          ic_pach = self.__icon_patch,
                          pos_ax = self.__ax_start+0,
                          pos_ay = self.__ay_start+3,)
        self._t_ax0=self.text_h(pl=self.__f_place,
                          ic_pach = self.__icon_patch,
                          pos_ax = self.__ax_start+1,
                          pos_ay = self.__ay_start+3,)
        self._joy=self.join(pl=self.__f_place,
                          ic_pach = self.__icon_patch,
                          pos_ax = self.__ax_start+0,
                          pos_ay = self.__ay_start+6,)
        self._combox=self.cb_sub_menu(pl=self.__s_place,
                          pos_ax = self.__ax_start+0,
                          pos_ay = self.__ay_start+0,)                          
        self.list_sub_menu=[self._bord,self._t_ax1,self._t_ax0,self._joy,self._combox]

    def creates(self,):
        for count in self.list_sub_menu:
            count.create()

    def builds(self,):
        for count in self.list_sub_menu:
            count.build()
            self.__f_place.grid(row=0,column=0,sticky =  "w")
            self.__s_place.grid(row=1,column=0,sticky =  "w")

    



from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('水果大賣場')
        style = ttk.Style(self)
#=======================strat topframe======================
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')
        btn1 = ttk.Button(topFrame,text='哈密瓜')
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text='葡萄')
        btn2.pack(side='left',expand=True,fill='x',padx=10)
        btn3 = ttk.Button(topFrame,text='櫻桃')
        btn3.pack(side='left',expand=True,fill='x',padx=10)
#======================end topframe======================

#======================strat bottomframe=====================
        bottomFrame1 = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottomFrame1.pack(padx=10,pady=10,side='left')
        btnF1_1 = ttk.Button(bottomFrame1,text='芭樂', padding=(30,40))
        btnF1_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF1_2 = ttk.Button(bottomFrame1,text='葡萄柚', padding=10)
        btnF1_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF1_3 = ttk.Button(bottomFrame1,text='柳橙', padding=10)
        btnF1_3.pack(side='top',expand=True,fill='x',padx=10)
#======================end bottomframe======================

#======================strat bottomframe======================
        bottomFrame2 = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottomFrame2.pack(padx=10,pady=10,side='left')
        btnF2_1 = ttk.Button(bottomFrame2,text='草莓', padding=(30,25))
        btnF2_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF2_2 = ttk.Button(bottomFrame2,text='香蕉', padding=10)
        btnF2_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF2_3 = ttk.Button(bottomFrame2,text='蘋果', padding=25)
        btnF2_3.pack(side='top',expand=True,fill='x',padx=10)
#======================end bottomframe======================

#======================strat bottomframe======================
        bottomFrame3 = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottomFrame3.pack(padx=10,pady=10,side='left')
        btnF3_1 = ttk.Button(bottomFrame3,text='荔枝', padding=(30,20))
        btnF3_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF3_2 = ttk.Button(bottomFrame3,text='西瓜', padding=20)
        btnF3_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF3_3 = ttk.Button(bottomFrame3,text='芒果', padding=20)
        btnF3_3.pack(side='top',expand=True,fill='x',padx=10)
#======================end bottomframe======================

def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()
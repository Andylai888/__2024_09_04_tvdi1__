from getinfo import GetInfo
import tkinter as tk
from tkinter import font

a = GetInfo()
b = a.getInfoFromWeb()
monthPrice = a.DataTransform(b)
value = 0

class PriceShow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Invoice Price")
        self.geometry("600x650")
        global value 
        fontstyle3 = font.Font(family="微軟正黑體", size=11, weight ="bold")

        self.midFrame = tk.Frame(self, width = 500, height = 300, bd = 4, relief= tk.GROOVE)
        self.midFrame.pack()
        self.drawMidinner(monthPrice[value][1])
        titleFrame = tk.Frame(self, width=500, bd=4, relief=tk.GROOVE)
        for index, i in enumerate(monthPrice):
            titleButton = tk.Button(titleFrame, text=i[0], bd=3, relief=tk.RAISED, padx=14, pady =10, font=fontstyle3)
            titleButton.bind("<Button-1>", self.userClick)
            titleButton.pack(side=tk.LEFT, ipadx = 9, padx=5, pady =10)
        titleFrame.pack()
        self.buttomFrame = tk.Frame(self, width = 500, bd = 4, relief= tk.GROOVE)
        self.buttomEntry()
        self.buttomFrame.pack()

    def userClick(self, event):
        '''
        when the month button clicked, return the text and use it to change global "value"
        use the current "value" to draw the midInner frame
        :param event: it is bind to button-1 click
        :return: renew the midInner frame
        '''
        bottonTxt = event.widget["text"] 
        global value
        if bottonTxt == monthPrice[0][0]:
            value = 0
        elif bottonTxt == monthPrice[1][0]:
            value = 1
        elif bottonTxt == monthPrice[2][0]:
            value = 2
        pricelist = monthPrice[value][1]
        self.midinnerFrame.destroy()
        self.drawMidinner(pricelist)


    def drawMidinner(self, priceList):
        '''
        use the price list to draw the major frame
        :param priceList: the lottery number list
        :return: the major inner frame with price numbers
        '''
        global value
        self.midinnerFrame = tk.Frame(self.midFrame, width=550)
        fontstyle1 = font.Font(family="Arial", size=18, weight="bold")
        fontstyle2 = font.Font(family="微軟正黑體", size=12, weight="bold")

        tk.Label(self.midinnerFrame, text=f"{monthPrice[value][0]}    開獎日期:{monthPrice[value][2]}", font=fontstyle2).grid(column=0, row=0, columnspan=2, ipadx=93)

        labels = [
            ("獎別", "中獎號碼"),
            ("特別獎", priceList[0] if len(priceList) > 0 else "", "同期統一發票收執聯8位數號碼與特獎號碼相同者獎金1,000萬元"),
            ("特獎", priceList[1] if len(priceList) > 1 else "", "同期統一發票收執聯8位數號碼與特獎號碼相同者獎金200萬元"),
            ("頭獎", priceList[2:5] if len(priceList) > 4 else "", "同期統一發票收執聯8位數號碼與特獎號碼相同者獎金20萬元"),
            ("二獎", "同期統一發票收執聯末7位數號碼與頭獎中獎號碼末7位相同者各得獎金4萬元"),
            ("三獎", "同期統一發票收執聯末6位數號碼與頭獎中獎號碼末6位相同者各得獎金1萬元"),
            ("四獎", "同期統一發票收執聯末5位數號碼與頭獎中獎號碼末5位相同者各得獎金4千元"),
            ("五獎", "同期統一發票收執聯末4位數號碼與頭獎中獎號碼末4位相同者各得獎金1千元"),
            ("六獎", "同期統一發票收執聯末3位數號碼與頭獎中獎號碼末3位相同者各得獎金2百元"),
            ("增開六獎", priceList[5] if len(priceList) > 5 else "", "同期統一發票收執聯末3位數號碼與增開六獎號碼相同者各得獎金2百元")
        ]

        row = 1
        for label_text, *prizes in labels:
            tk.Label(self.midinnerFrame, text=label_text, padx=20, font=fontstyle2).grid(column=0, row=row, rowspan=len(prizes) + 1)
            for prize in prizes:
                tk.Label(self.midinnerFrame, text=prize, font=fontstyle1 if isinstance(prize, str) else fontstyle2).grid(column=1, row=row)
                row += 1
        
        self.midinnerFrame.pack()
        

    def buttomEntry(self):
        fontstyle4 = font.Font(family="微軟正黑體", size=12, weight="bold")
        tk.Label(self.buttomFrame, text="對獎專區\n輸入末三碼", font=fontstyle4).grid(column=0, row=0, rowspan=2, padx=45)
        
        self.numberKeyin = tk.StringVar()
        tk.Entry(self.buttomFrame, textvariable=self.numberKeyin).grid(column=1, row=0, ipadx=50, padx=10)
        
        tk.Button(self.buttomFrame, text="對獎", bd=2, relief=tk.RAISED, font=fontstyle4, command=self.on_click).grid(column=2, row=0, padx=30, pady=10, ipadx=17, rowspan=2)
        
        self.label2 = tk.Label(self.buttomFrame, text="", font=fontstyle4)
        self.label2.grid(column=1, row=1)
        

    def buttomEntry(self):
        '''
        draw the buttom frame for price check
        :return: buttom frame
        '''
        fontstyle4 = font.Font(family="微軟正黑體", size=12, weight="bold")
        label1 = tk.Label(self.buttomFrame, text="對獎專區\n輸入末三碼", font = fontstyle4)
        label1.grid(column=0, row=0, rowspan = 2, padx = 45)
        self.numberKeyin = tk.StringVar()
        self.keyinNumber = tk.Entry(self.buttomFrame, textvariable=self.numberKeyin)
        self.keyinNumber.grid(column=1, row=0, ipadx=50, padx = 10)
        matchNumber = tk.Button(self.buttomFrame, text = "對獎" , bd = 2, relief= tk.RAISED, font = fontstyle4, command = self.on_click)
        matchNumber.grid(column=2, row=0, padx = 30, pady = 10, ipadx = 17, rowspan =2)
        words = ""
        self.label2 = tk.Label(self.buttomFrame, text=words, font = fontstyle4)
        self.label2.grid(column=1, row=1)

    def on_click(self):
        '''
        this method provides a simple  code to check the input string,
        and then matches the string with the lottery number
        '''
        entryNumber = self.numberKeyin.get()
        global value
        pricelist = monthPrice[value][1]
        self.label2.configure(text="")
        if len(entryNumber) != 3:
            words = "輸入字數不符，請重新輸入!!"
            self.label2.configure(text=words, fg = "red")
        elif entryNumber.isdigit() is not True:
            words = "含有數字以外的字元，請重新輸入!!"
            self.label2.configure(text=words, fg = "red")
        elif entryNumber in [pricelist[2][-3:],pricelist[3][-3:],pricelist[4][-3:],pricelist[5][-3:]]:
            words = f"{entryNumber:s} 恭喜中獎了!!"
            self.label2.configure(text=words, fg = "green")

        else:
            words = f"{entryNumber:s} 未中獎，再接再厲!!"
            self.label2.configure(text=words, fg = "brown")
        self.keyinNumber.delete(0, "end")

if __name__ == "__main__":
    window = PriceShow()
    window.mainloop()
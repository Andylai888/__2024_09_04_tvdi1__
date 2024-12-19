import tkinter as tk
from tkinter import font
import tkinter as tk
from tkinter import font, messagebox
from getinfo import GetInfo
import tkinter as tk
from tkinter import font



class PriceShow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Invoice Price")
        self.geometry("600x650")
        
        # 確保 monthPrice 有數據，否則顯示錯誤提示
        if not monthPrice or not all(len(m) >= 2 for m in monthPrice):
            print("Error: monthPrice 資料格式不正確或為空")
            tk.Label(self, text="無法載入資料，請檢查數據來源", font=("微軟正黑體", 16), fg="red").pack()
            return
        
        global value
        value = 0  # 初始選中第一個月份

        # UI 結構初始化
        self.midFrame = tk.Frame(self, width=500, height=300, bd=4, relief=tk.GROOVE)
        self.midFrame.pack()
        self.draw_midinner()

        titleFrame = tk.Frame(self, width=500, bd=4, relief=tk.GROOVE)
        for index, item in enumerate(monthPrice):
            titleButton = tk.Button(
                titleFrame,
                text=item[0],
                bd=3,
                relief=tk.RAISED,
                padx=14,
                pady=10,
                font=("微軟正黑體", 11, "bold"),
                command=lambda idx=index: self.change_month(idx)
            )
            titleButton.pack(side=tk.LEFT, ipadx=9, padx=5, pady=10)
        titleFrame.pack()

        self.buttomFrame = tk.Frame(self, width=500, bd=4, relief=tk.GROOVE)
        self.buttom_entry()
        self.buttomFrame.pack()

    def change_month(self, idx):
        """
        切換月份，重新繪製中間內容
        """
        global value
        value = idx
        self.update_midinner()

    def draw_midinner(self):
        """
        初始化繪製中間區域框架
        """
        self.midinnerFrame = tk.Frame(self.midFrame, width=550)
        self.midinnerFrame.pack()
        self.update_midinner()

    def update_midinner(self):
        """
        根據當前 value 和 monthPrice 內容更新中間框架
        """
        global value
        self.midinnerFrame.destroy()  # 清除舊的框架
        self.midinnerFrame = tk.Frame(self.midFrame, width=550)
        self.midinnerFrame.pack()

        # 驗證當前數據是否有效
        if not (0 <= value < len(monthPrice)):
            tk.Label(self.midinnerFrame, text="無效的月份資料", font=("微軟正黑體", 16), fg="red").pack()
            return
        
        price_list = monthPrice[value][1] if len(monthPrice[value]) > 1 else []
        
        # 畫出標題
        tk.Label(
            self.midinnerFrame,
            text=f"{monthPrice[value][0]} 開獎日期: {monthPrice[value][2] if len(monthPrice[value]) > 2 else 'N/A'}",
            font=("微軟正黑體", 12, "bold"),
        ).grid(column=0, row=0, columnspan=2, ipadx=93)

        # 如果 price_list 資料不足，提供替代顯示
        if len(price_list) < 6:
            tk.Label(
                self.midinnerFrame,
                text="資料不完整，請稍後重試",
                font=("微軟正黑體", 14),
                fg="red"
            ).pack()
            return

        # 正常繪製中獎號碼列表
        awards = [
            ("特別獎", price_list[0], "同期統一發票收執聯8位數號碼與特別獎號碼相同者獎金1,000萬元"),
            ("特獎", price_list[1], "同期統一發票收執聯8位數號碼與特獎號碼相同者獎金200萬元"),
            ("頭獎", "\n".join(price_list[2:5]), "同期統一發票收執聯8位數號碼與頭獎號碼相同者獎金20萬元"),
            ("增開六獎", price_list[5], "同期統一發票收執聯末3位數號碼與增開六獎號碼相同者各得獎金200元")
        ]

        fontstyle1 = font.Font(family="Arial", size=18, weight="bold")
        fontstyle2 = font.Font(family="微軟正黑體", size=12, weight="bold")

        for idx, (name, number, desc) in enumerate(awards):
            tk.Label(self.midinnerFrame, text=name, font=fontstyle2).grid(column=0, row=1 + idx * 2, rowspan=2)
            tk.Label(self.midinnerFrame, text=number, font=fontstyle1, fg="red").grid(column=1, row=1 + idx * 2)
            tk.Label(self.midinnerFrame, text=desc, wraplength=400).grid(column=1, row=2 + idx * 2)

    def buttom_entry(self):
        """
        底部輸入框和按鈕
        """
        fontstyle4 = font.Font(family="微軟正黑體", size=12, weight="bold")
        tk.Label(self.buttomFrame, text="對獎專區\n輸入末三碼", font=fontstyle4).grid(column=0, row=0, rowspan=2, padx=45)
        self.numberKeyin = tk.StringVar()
        self.keyinNumber = tk.Entry(self.buttomFrame, textvariable=self.numberKeyin)
        self.keyinNumber.grid(column=1, row=0, ipadx=50, padx=10)
        tk.Button(
            self.buttomFrame,
            text="對獎",
            font=fontstyle4,
            command=self.on_click,
        ).grid(column=2, row=0, padx=30, pady=10, ipadx=17, rowspan=2)
        self.label2 = tk.Label(self.buttomFrame, text="", font=fontstyle4)
        self.label2.grid(column=1, row=1)

    def on_click(self):
        """
        處理輸入對獎邏輯
        """
        entry_number = self.numberKeyin.get()
        global value
        price_list = monthPrice[value][1] if len(monthPrice[value]) > 1 else []
        self.label2.configure(text="")
        if len(entry_number) != 3:
            self.label2.configure(text="輸入字數不符，請重新輸入!!", fg="red")
        elif not entry_number.isdigit():
            self.label2.configure(text="含有數字以外的字元，請重新輸入!!", fg="red")
        elif any(entry_number == price[-3:] for price in price_list):
            self.label2.configure(text=f"{entry_number} 恭喜中獎了!!", fg="green")
        else:
            self.label2.configure(text=f"{entry_number} 未中獎，再接再厲!!", fg="brown")
        self.keyinNumber.delete(0, "end")


if __name__ == "__main__":
    window = PriceShow()
    window.mainloop()

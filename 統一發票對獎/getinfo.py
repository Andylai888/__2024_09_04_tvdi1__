from tkinter.simpledialog import Dialog
from tkinter import ttk
from tkinter import Misc
import tkinter as tk


class Messagebox(Dialog):
    def __init__(self, parent: Misc, title: str, name: str, bmi: float, status: str, advice: str, status_color: str):
        self.parent = parent
        self.name = name
        self.bmi = bmi
        self.status = status
        self.advice = advice

        # 設置樣式
        style = ttk.Style(parent)
        style.configure('status.TLabel', foreground=status_color, font=('Arial', 12, 'bold'))
        super().__init__(parent=parent, title=title)

    def body(self, master):
        contain_frame = ttk.Frame(master, padding=(10, 10))
        
        # 顯示姓名
        ttk.Label(contain_frame, text="姓名:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(contain_frame, text=self.name).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # 顯示 BMI 值
        ttk.Label(contain_frame, text="BMI值:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(contain_frame, text=f"{self.bmi:.2f}").grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # 顯示狀態
        ttk.Label(contain_frame, text="狀態:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(contain_frame, text=self.status, style='status.TLabel').grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # 顯示建議
        ttk.Label(contain_frame, text="建議:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(contain_frame, text=self.advice, wraplength=300).grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        contain_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def apply(self):
        # 清空輸入框
        self.parent.name_value.set('')
        self.parent.hight_value.set('')
        self.parent.weight_value.set('')

    def buttonbox(self):
        box = ttk.Frame(self)

        # 確定按鈕
        ttk.Button(box, text="確定", command=self.ok, style="TButton").pack(padx=5, pady=10, side=tk.RIGHT)
        box.pack(padx=10, pady=10)

    def ok(self):
        print("OK button was clicked!")
        super().ok()

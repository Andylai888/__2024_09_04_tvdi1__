import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox


class Window(ThemedTk):
    def __init__(self, theme: str | None, **kwargs):
        super().__init__(**kwargs)
        self.title("BMI計算器")
        self.resizable(False, False)

        
        style = ttk.Style()
        style.configure('input.TFrame', background='#ffffff')
        style.configure('press.TButton', font=('arial', 17))

        
        titleFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        titleFrame.pack(padx=200, pady=(0, 0))

        
        input_frame = ttk.Frame(self, style='Input.TFrame')

        
        label_name = ttk.Label(input_frame, text="姓名:")
        label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.name_value = tk.StringVar()
        entry_name = ttk.Entry(input_frame, textvariable=self.name_value)
        entry_name.grid(row=0, column=1, padx=10, pady=10)

        
        label_height = ttk.Label(input_frame, text="身高 (cm):")
        label_height.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.height_value = tk.StringVar()
        entry_height = ttk.Entry(input_frame, textvariable=self.height_value)
        entry_height.grid(row=1, column=1, padx=10, pady=10)

       
        label_weight = ttk.Label(input_frame, text="體重 (kg):")
        label_weight.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.weight_value = tk.StringVar()
        entry_weight = ttk.Entry(input_frame, textvariable=self.weight_value)
        entry_weight.grid(row=2, column=1, padx=10, pady=10)

        input_frame.pack(pady=50, padx=100)

        
        button_frame = ttk.Frame(self)
        button_calculate = ttk.Button(button_frame, text="計算", command=self.show_bmi_result, style='press.TButton')
        button_calculate.pack(side=tk.RIGHT, expand=True, fill=tk.X)

        button_close = ttk.Button(button_frame, text="關閉", command=self.destroy, style='press.TButton')
        button_close.pack(side=tk.LEFT, expand=True, fill=tk.X)

        button_frame.pack(padx=20, fill=tk.X, pady=(0, 20))

    def show_bmi_result(self):
        try:
            name: str = self.name_value.get()
            height: int = int(self.height_value.get())
            weight: int = int(self.weight_value.get())
        except ValueError:
            messagebox.showwarning("Warning", "格式錯誤，請確認欄位輸入內容！")
        else:
            self.show_result(name=name, height=height, weight=weight)

    def show_result(self, name: str, height: int, weight: int):
        bmi = weight / (height / 100) ** 2
        if bmi < 18.5:
            status = "體重過輕"
            ideal_weight = 18.5 * (height / 100) ** 2
            weight_change = ideal_weight - weight
            advice = f"您需要至少增加 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        elif 18.5 <= bmi <= 24.9:
            status = "正常"
            advice = "您的體重正常，請保持！"
        else:
            status = "體重過重"
            ideal_weight = 24.9 * (height / 100) ** 2
            weight_change = weight - ideal_weight
            advice = f"您需要至少減少 {abs(weight_change):.2f} 公斤才能達到正常體重。"

        messagebox.showinfo(
            title="BMI 計算結果",
            message=f"姓名: {name}\nBMI: {bmi:.2f}\n狀態: {status}\n建議: {advice}",
        )


def main():
    window = Window(theme='arc')
    window.mainloop()


if __name__ == '__main__':
    main()

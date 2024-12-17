from dash import Dash,html,dcc,callback,Input, Output,dash_table,_dash_renderer
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
_dash_renderer._set_react_version("18.2.0")
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from tools import CustomMessagebox

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__,external_stylesheets=dmc.styles.ALL)

radio_data = [['pop','人口'],['lifeExp','平均壽命'],['gdpPercap','人均GDP']]
selected_data = [{'value':value,'label':value} for value in df.country.unique()]
elements = [
    {"position": 6, "mass": 12.011, "symbol": "C", "name": "Carbon"},
    {"position": 7, "mass": 14.007, "symbol": "N", "name": "Nitrogen"},
    {"position": 39, "mass": 88.906, "symbol": "Y", "name": "Yttrium"},
    {"position": 56, "mass": 137.33, "symbol": "Ba", "name": "Barium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
]

rows = [
    dmc.TableTr(
        [
            dmc.TableTd(element["position"]),
            dmc.TableTd(element["name"]),
            dmc.TableTd(element["symbol"]),
            dmc.TableTd(element["mass"]),
        ]
    )
    for element in elements
]

head = dmc.TableThead(
    dmc.TableTr(
        [
            dmc.TableTh("Element Position"),
            dmc.TableTh("Element Name"),
            dmc.TableTh("Symbol"),
            dmc.TableTh("Atomic Mass"),
        ]
    )
)

body = dmc.TableTbody(rows)
caption = dmc.TableCaption("Some elements from periodic table")

app.layout = dmc.MantineProvider(
    [
    
        dmc.Container(        
            dmc.Title(f"世界各國人口,壽命,GDP統計數字", order=2),
            fluid=True,
            ta='center',
            my=30  
        )
    ,
        dmc.Flex(
            [
                dmc.Stack(
                    [
                        #dcc.RadioItems(['pop','lifeExp','gdpPercap'],value='pop',inline=True,id='radio_item')
                        dmc.RadioGroup(
                            children=dmc.Group([dmc.Radio(l, value=k) for k, l in radio_data], my=10),
                            id="radio_item",
                            value="pop",
                            label="請選擇查詢的種類",
                            size="md",
                            mb=10,
                        )
        
                    , 
                        #dcc.Dropdown(df.country.unique(),value='Taiwan',id='dropdown-selection')
                        dmc.Select(
                            label="請選擇國家",
                            placeholder="請選擇1個",
                            id="dropdown-selection",
                            value="Taiwan",
                            data=selected_data,
                            w=200,
                            mb=10,
                        )
                    ],
                    
                )
            ,
                
                #dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
                dmc.ScrollArea(
                    dmc.Table(
                        [head, body, caption],
                        w='100%'
                    ),
                    h=300,
                    w='50%'
                )

                
                

            ],
            direction={"base": "column", "sm": "row"},
            gap={"base": "sm", "sm": "lg"},
            justify={"base": "center"},
            

        )
    ,
    #dcc.Graph(id='graph-content')
        dmc.Container(
           dcc.Graph(id='graph-content') 
        )
    ]
)

#圖表顯示的事件
@callback(    
    Output('graph-content','figure'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
    
)
def update_graph(country_value,radio_value):
    dff = df[df.country == country_value]
    print(radio_value)
    if radio_value == "pop":
        title = f'{country_value}:人口成長圖表'
    elif radio_value == "lifeExp":
        title = f'{country_value}:預期壽命'
    elif radio_value == 'gdpPercap':
        title = f'{country_value}:人均GDP'

    return px.line(dff,x='year',y=radio_value,title=title)

#表格顯示的事件
# @callback(    
#     Output('datatable','data'),
#     Output('datatable','columns'),    
#     Input('dropdown-selection','value'),
#     Input('radio_item','value') 
# )
# def update_table(country_value,radio_value):
#     dff = df[df.country == country_value]
#     columns = [
#         {'id':'country','name':'country'},
#         {'id':'year','name':'year'}        
#     ]
#     if radio_value == 'pop':
#         columns.append({'id':'pop','name':'pop'})
#     elif radio_value == 'lifeExp':
#         columns.append({'id':'lifeExp','name':'lifeExp'})
#     elif radio_value == 'gdpPercap':
#         columns.append({'id':'gdpPercap','name':'gdpPercap'})

#     return dff.to_dict('records'),columns
    
class Window(ThemedTk):
    def __init__(self,theme:str|None,**kwargs):
        super().__init__(**kwargs)
        self.title("BMI計算器")
       
        self.resizable(False,False)
        style = ttk.Style()
        style.configure('input.TFrame',background='#ffffff')
        style.configure('press.TButton',font=('arial',17))
       
        titleFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        titleFrame.pack(padx=100,pady=(0,5))
        
        input_frame = ttk.Frame(self,style='Input.TFrame')
        
        label_name = ttk.Label(input_frame, text="姓名(name):")
        label_name.grid(row=0, column=0, padx=10, pady=10,sticky=tk.E)

        self.name_value = tk.StringVar()
        self.name_value.set('')
        entry_name = ttk.Entry(input_frame,textvariable=self.name_value)
        entry_name.grid(row=0, column=1, padx=20, pady=20)

       
        label_height = ttk.Label(input_frame, text="身高 (cm):")
        label_height.grid(row=1, column=0, padx=10, pady=10,sticky=tk.E)

        self.hight_value = tk.StringVar()
        self.hight_value.set('')
        entry_height = ttk.Entry(input_frame,textvariable=self.hight_value)
        entry_height.grid(row=1, column=1, padx=20, pady=20)

        label_weight = ttk.Label(input_frame, text="體重 (kg):")
        label_weight.grid(row=2, column=0, padx=10, pady=10,sticky=tk.E)

        self.weight_value = tk.StringVar()
        self.weight_value.set('')
        entry_weight = ttk.Entry(input_frame,textvariable=self.weight_value)
        entry_weight.grid(row=2, column=1, padx=20, pady=20)    

        input_frame.pack(pady=50,padx=100)
        
        button_frame = ttk.Frame(self)
        button_calculate = ttk.Button(button_frame, text="計算", command=self.show_bmi_result,style='press.TButton')
        button_calculate.pack(side=tk.RIGHT,expand=True,fill=tk.X)

        button_close = ttk.Button(button_frame, text="關閉",command=self.destroy,style='press.TButton')
        button_close.pack(side=tk.LEFT,expand=True,fill=tk.X)
        button_frame.pack(padx=30,fill=tk.X,pady=(0,30))

    
    
    def show_bmi_result(self):
        try:
            name:str = self.name_value.get()
            height:int = int(self.hight_value.get())
            weight:int = int(self.weight_value.get())
        
        
        except ValueError:
            messagebox.showwarning("Warning","格式錯誤,欄位沒有填寫")
        except Exception:
            messagebox.showwarning("Warning","不知明的錯誤")
        else:
            self.show_result(name=name,height=height,weight=weight)


    def show_result(self,name:str,height:int,weight:int):
            bmi = weight / (height / 100) ** 2
            if bmi < 18.5:
                status = "體重過輕是怎樣~想當紙片人嗎!"
                ideal_weight = 18.5 * (height / 100) ** 2
                weight_change = ideal_weight - weight
                status_color = "red"
                advice = f"您需要至少增加 {abs(weight_change):.2f} 公斤才不會被風吹走。"
            elif 18.5 <= bmi <= 24.9:
                status = "唉呦正常喔~給您按個讚!"
                status_color = "blue"
                advice = "您的體重怎麼保持的~教一下吧！"
            else:
                status = "體重過重啦~有那麼好吃嗎?吃的那麼胖!"
                ideal_weight = 24.9 * (height / 100) ** 2
                weight_change = weight - ideal_weight
                status_color = "red"
                advice = f"您需要減肥 {abs(weight_change):.2f} 公斤才能再繼續吃。"

            CustomMessagebox(self,title="BMI",name=name,bmi=bmi,status=status,advice=advice,status_color=status_color)
            
            
            

def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    app.run(debug=True)
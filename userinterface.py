#this is the first git test
import tkinter as tk
import mysql.connector
import datetime
def btn_clicked():

    day=input.get()
    sql = ('''
    SELECT  SUM(value)
    FROM    receipt
    WHERE   created_at > %s
    ''')

    date = datetime.datetime.now()
    date = date+datetime.timedelta(days=-int(day))
    param = (date,)

    cursor.execute(sql, param)
    sum=cursor.fetchall()
    label['text'] = sum
   
def btn2_clicked():
    value=value_input.get()
    marchandise = data_input.get()
    sql = ('''
    SELECT  SUM(value)
    FROM    receipt
    WHERE   created_at > %s
    ''')

def btn3_clicked():
    value = value2_input.get()
    marchandise = data2_input.get()
    date = day.get()
    sql = ('''
    SELECT  SUM(value)
    FROM    receipt
    WHERE   created_at > %s
    ''')


    
cnx = None
day=-1
try:
    cnx = mysql.connector.connect(
        user='uzak',  # ユーザー名
            password='Skakki0209@',  # パスワード
            db='mysql',
            host='192.168.0.12'  # ホスト名(IPアドレス）
        )

    if cnx.is_connected:
        cursor = cnx.cursor(buffered=True)


    # ウィンドウ作成
    root = tk.Tk()

    # ボタンの作成と配置
    root.minsize(width=500, height=500)
    button1 = tk.Button(root, text="決定", command=btn_clicked)
    button1.place(x=300, y=10, width=50, height=30)
   
    root.title('レシート家計簿')
    input = tk.Entry(width=14)
    input.insert(0, "ここに値を入力")
    input.place(x=200, y=14)
    label = tk.Label(root, text='', font=('System', 24))
    label.place(x=300, y=10)



    # ラベル
    txt = tk.Label(text='何日間のデータを知りたいですか？')
    txt.place(x=10, y=10)
    txt2 = tk.Label(text="個別にデータを追加")
    txt2.place(x=10,y=50)
    data_input = tk.Entry(width=14)
    data_input.insert(0, "商品名を入力")
    data_input.place(x=200, y=50)
    value_input = tk.Entry(width=14)
    value_input.insert(0, "値段を入力")
    value_input.place(x=300, y=50)
    button2 = tk.Button(root, text="追加", command=btn2_clicked)
    button2.place(x=400, y=45, width=50, height=30)
    button3= tk.Button(root, text="追加", command=btn3_clicked)
    button3.place(x=300, y=95, width=50, height=30)
    data2_input = tk.Entry(width=12)
    data2_input.insert(0, "商品名を入力")
    data2_input.place(x=220, y=100)
    value2_input = tk.Entry(width=10)
    value2_input.insert(0, "値段を入力")
    value2_input.place(x=150, y=100)
    day_input= tk.Entry(width=12)
    day_input.place(x=70, y=100)
    day_input.insert(0, "x日ごとに購入")
    txt2 = tk.Label(text="定期購入")
    txt2.place(x=10,y=97)
    

    
   
    # メインループ
    root.mainloop()

except:
    print("Error occured")
finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
cursor.close() 


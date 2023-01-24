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
    print(date)
    param = (date,)

    cursor.execute(sql, param)
    sum=cursor.fetchall()
    label['text'] = sum
   
def bottun2_clicked():
    value=value_input.get()
    marchandise = data_input.get()
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
            host='10.101.68.90'  # ホスト名(IPアドレス）
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
    txt = tk.Label(text='何日間の合計を知りたいですか？')
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
    button2.place(x=450, y=50, width=50, height=30)
   
    # メインループ
    root.mainloop()

except:
    print("Error occured")
finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
cursor.close() 

    

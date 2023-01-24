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
    button1 = tk.Button(root, text="決定", command=btn_clicked)
    button1.place(x=10, y=20, width=10, height=10)
    root.minsize(width=500, height=500)
    root.title('レシート家計簿')
    input = tk.Entry(width=20)
    input.insert(0, "ここに値を入力")
    input.place(x=200, y=10)
    label = tk.Label(root, text='', font=('System', 24))
    label.place(x=300, y=10)



    # ラベル
    txt = tk.Label(text='何日間の合計を知りたいですか？')
    txt.place(x=10, y=10)
    txt2 = tk.Label(text="個別にデータを追加")
    txt2.place(x=10,y=100)
    # メインループ
    root.mainloop()

except:
    print("Error occured")
finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
cursor.close() 

    

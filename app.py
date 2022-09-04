from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return render_template('index.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    db = pymysql.connect(host="127.0.0.1",
                         user="root",
                         password="123456",
                         database="db_test")
    cur = db.cursor()
    sql = "select Con from text"

    try:
        cur.execute(sql)
        # db.commit()
        results1 = cur.fetchall()
        # results2 = cur.fetchone()
        # print(results1)
        # print(type(results2))
    except Exception as e:
        db.rollback()  # 如果出错就回滚并且抛出错误收集错误信息。
        print("Error!:{0}".format(e))

    a = results1[-1][0]
    cur.close()
    db.close()

    return render_template('data.html', data=a)


if __name__ == '__main__':
    app.run()

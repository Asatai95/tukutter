import MySQLdb
from flask import Flask, render_template, redirect, request, make_response

application = Flask(__name__)

@application.route('/')
def test_db():

    return render_template('singlepage_template_sample.html')

@application.route('/', methods=['POST'])
def test():

    phone = request.form['phone']
    print(phone)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='single', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'insert into phone(number) values(%s) on duplicate key update number = "' + phone + '" '
    con.execute(sql, [phone])
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/')

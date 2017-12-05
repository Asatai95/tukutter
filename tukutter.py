import MySQLdb
from flask import Flask, request, render_template, redirect

application = Flask(__name__)

@application.route('/top')
def top():

    return render_template('top.html')

@application.route('/login')
def login():

    return render_template('login.html')

@application.route('/login', methods=['POST'])
def login_db():

    log_id = request.form['log_id']
    passwd = request.form['passwd']

    db = MySQLdb.connect( user='root', passwd='asatai95',
        host='localhost', db='tukutter', charset='utf8')

    con = db.cursor()

    sql = "select log_id, passwd from users where log_id and passwd =' " +log_id+ " ' and ' " +passwd+ " ' "
    con.execute(sql)
    passwd = con.fetchall()

    if len(log_id) and len(passwd) is 0:

         return render_template('top.html')

    else:
         return redirect('http://localhost:8080/login')

    print(result)

@application.route('/new')
def new():

    html = render_template('new.html')

    print(html)
    return html

@application.route('/new', methods=['POST'])
def new_db():

    log_id = request.form['log_id']
    passwd = request.form['passwd']
    user_name = request.form['user_name']

    db = MySQLdb.connect( user='root', passwd='asatai95',
        host='localhost', db='tukutter', charset='utf8')

    con = db.cursor()

    sql = 'insert ignore into users(log_id,passwd,user_name) values(%s,%s,%s)'
    con.execute(sql,[log_id,passwd,user_name])

    db.commit()

    db.close()
    con.close()

    print('http://localhost:8080/top')
    return redirect('http://localhost:8080/top')

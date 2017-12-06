import MySQLdb
from flask import Flask, request, render_template, redirect, make_response

application = Flask(__name__)

@application.route('/top')
def top():

    return render_template('top.html')

# @application.route('/login')
# def cookie():
#
#     resp = make_response('cookie set')
#     resp.set_cookie('log_id', 'passwd')
#
#     print('resp')


@application.route('/login')
def login():

    return render_template('login.html')

@application.route('/login', methods=['POST'])
def login_db():

    log_id = request.form['log_id']
    passwd = request.form['passwd']
    print(log_id)
    print(passwd)

    db = MySQLdb.connect( user='root', passwd='asatai95',
        host='localhost', db='tukutter', charset='utf8')
    print('???')

    con = db.cursor()
    print(con)

    sql = "select log_id, passwd from users where log_id = '" + log_id + "' and passwd = '" + passwd + "'"
    con.execute(sql)
    result = con.fetchall()
    print(result)
    print(sql)

    if len(log_id) and len(passwd) is 0:

        print('top.html')

        return render_template('top.html')

    else:
        print('login.html')
        return redirect('http://localhost:8080/login')

    print(result)

@application.route('/logout')
def logout():

    return redirect('https://localhost:8080/login')

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

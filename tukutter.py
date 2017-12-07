import MySQLdb
import time
from flask import Flask, request, render_template, redirect, make_response

application = Flask(__name__)

@application.route('/')
def top():

    return render_template('top.html')

@application.route('/login')
def login():

    return render_template('login.html')

@application.route('/login', methods=['POST'])
def login_db():

    log = request.form['log_id']
    pas = request.form['passwd']


    db = MySQLdb.connect( user='root', passwd='asatai95',
        host='localhost', db='tukutter', charset='utf8')

    con = db.cursor()

    sql = "select log_id, passwd from users where log_id = '" + log + "' and passwd = '" + pas + "'"
    con.execute(sql)

    result = con.fetchall()

    if len(result) is 1:

        print('top.html')

        resp = make_response(render_template('top.html'))
        resp.set_cookie(log, pas)
        print(resp)

        return resp

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

@application.route('/tweet')
def tweet():

    return render_template('tweet.html')

@application.route('/tweet', methods=['POST'])
def tweet_db():

    test = request.form['tweet']
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')

    db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()

    sql = 'insert into tweet(user_id, tweet_comment, created_at) value (1, %s, %s)'
    con.execute(sql, [test, time_stamp])
    db.commit()
    print(sql)


    db.close()
    con.close()

    return render_template('tweet.html')

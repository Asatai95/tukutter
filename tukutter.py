import MySQLdb
import time
from flask import Flask, request, render_template, redirect, make_response

application = Flask(__name__)

@application.route('/')
def top_db():

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select created_at, tweet_comment, user_name from tweet inner join users on tweet.user_id = users.id where log_id != '" + data + "' "
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return render_template('top.html', rows=result)


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
        resp.set_cookie('name' , log)
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

    print('http://localhost:8080/')
    return redirect('http://localhost:8080/')

@application.route('/tweet')
def tweet():

    return render_template('tweet.html')

@application.route('/tweet', methods=['POST'])
def tweet_db():

    test = request.form['tweet']
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')

    if len(test) is 0:

        return render_template('tweet.html', test='文字を入力して下さい')

    db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()

    sql = 'insert into tweet(user_id, tweet_comment, created_at) values(1 ,%s, %s)'
    con.execute(sql, [test, time_stamp])
    db.commit()
    print(sql)


    db.close()
    con.close()

    return render_template('tweet.html')

@application.route('/view')
def search():

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select tweet_comment, created_at, user_name from tweet inner join users on tweet.user_id = users.id"
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return render_template('search.html', rows=result)

@application.route('/search', methods=['POST'])
def search_db():

    search = request.form["search"]

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select tweet_comment, created_at, user_name from tweet inner join users on tweet.user_id = users.id where tweet_comment like '" '%' + search + '%' "' "
    con.execute(sql)
    db.commit()

    result = con.fetchall()
    print(result)

    if result == ():

        return render_template('search.html', test='該当なし')


    return render_template('search.html', rows=result)




# @application.route('/pro')
# def profile():
#
#     return render_template('pro.html')

@application.route('/pro')
def profile_db():

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select created_at, tweet_comment, user_name from tweet inner join users on tweet.user_id = users.id where log_id = '" + data + "'"
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return render_template('pro.html', rows=result)


@application.route('/oki')
def oki():

    return render_template('oki.html')

@application.route('/top', methods=['POST'])
def oki_db():

    oki = request.form['oki']

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "insert into fab(tweet_id,user_id) values(1,1)"
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return render_template('pro.html', rows=result)

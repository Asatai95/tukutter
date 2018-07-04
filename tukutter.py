import MySQLdb
import time
import os
from flask import Flask, request, render_template, redirect, make_response, send_from_directory, url_for, flash
from werkzeug import secure_filename

application = Flask(__name__)

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'gif'])
path = './static/img/*.ALLOWED_EXTENSIONS'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['SECRET_KEY'] = os.urandom(24)

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@application.route('/tukutter')
def top_db():

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select tweet.tw_id, created_at, tweet_comment, user_name, user_img, log_id from tweet inner join users on tweet.user_id = users.log_id where log_id != '" + data + "' "
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if sql is not False:

        sql = "select user_name, user_img from users where log_id = '" + data + "'"
        con.execute(sql)
        db.commit()
        print(sql)

        top = con.fetchall()
        print(top)

    return render_template('top.html', rows=result, tops=top)

@application.route('/')
def login():

    return render_template('login.html')

@application.route('/', methods=['POST'])
def login_db():

    log = request.form['log_id']
    pas = request.form['passwd']

    if log == (''):

        error_log = 'ログインIDを入力してください'

        return render_template('login.html', error_log=error_log)

    elif pas == (''):

        error_pas = 'パスワードを入力してください'

        return render_template('login.html', error_pas=error_pas)

    else:

        db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()

        sql = "select log_id, passwd from users where log_id = '" + log + "' and passwd = '" + pas + "' "
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        if result == ():

            error_login = 'ログインID、またはパスワードが異なります。'

            return render_template('login.html', error_login=error_login)

        else:

            print('top.html')

            resp = make_response(redirect('http://localhost:8080/tukutter'))
            resp.set_cookie('name' , log)
            print(resp)

            return resp

@application.route('/forgot')
def forgot():

    return render_template('forgot.html')

@application.route('/forgot', methods=['POST'])
def forgot_db():

    log_id = request.form['log_id']
    print(log_id)

    db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()

    sql = 'select log_id from users where log_id = "' + log_id + '" '
    test = con.execute(sql)
    db.commit()
    print(sql)
    print(test)

    if test == 0:

        error = '存在しないログインIDです。'

        return render_template('forgot.html', error=error)

    else:

        result = con.fetchall()
        print(result)

        resp = make_response(redirect('http://localhost:8080/remake'))
        resp.set_cookie('name' , log_id)
        print(resp)

    return resp

@application.route('/remake')
def remake():

    return render_template('remake.html')

@application.route('/remake', methods=['POST'])
def remake_db():

    data = request.cookies.get('name', None)
    passwd = request.form['passwd']
    passwd_again = request.form['passwd_again']
    print(passwd)
    print(passwd_again)
    print(data)

    if passwd == (''):

        error = 'パスワードを入力してください。'

        return render_template('remake.html', error=error)

    elif passwd_again == (''):

        error = '確認用のパスワードも入力してください。'

        return render_template('remake.html', error=error)

    elif passwd != passwd_again:

        error = '項目に同じパスワード値を入力してください。'

        return render_template('remake.html', error=error)

    elif len(passwd) <= 8 and len(passwd_again) <= 8:

        error = ('パスワードは8文字以上16文字以内で入力してください。')

        return render_template('remake.html', error=error)

    elif len(passwd) > 16:

        error = 'パスワードは16文字以内で入力してください。'

        return render_template('remake.html', error=error)

    elif passwd == passwd_again:

        print(data)

        db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()

        sql = 'select passwd from users where log_id = "' + data + '" '
        passwd_check = con.execute(sql)
        db.commit()
        print(passwd_check)
        print('test')

        result = con.fetchall()
        task = result[0][0]
        print(result)
        print('test')

        if task == passwd and task == passwd_again:

            error = 'すでに使用されているパスワードです。'

            return render_template('remake.html', error=error)

        else:

            db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
            con = db.cursor()

            sql = 'update users set passwd = "' + passwd + '" where log_id = "' + data + '" '
            commit = con.execute(sql)
            db.commit()
            print(sql)
            print(commit)

            result = con.fetchall()
            print(result)

            resp = make_response(redirect('http://localhost:8080/'))
            resp.set_cookie('','')
            print(resp)

            return resp

@application.route('/logout')
def logout():

    resp = make_response(redirect('http://localhost:8080/'))
    resp.set_cookie('', '')
    print(resp)

    return resp

@application.route('/new')
def new():

    return render_template('new.html')

@application.route('/new', methods=['POST'])
def new_db():

    log_id = request.form['log_id']
    print(log_id)
    passwd = request.form['passwd']
    print(passwd)
    user_name = request.form['user_name']
    print(user_name)
    img_file = request.files["img_file"]
    print(img_file)

    if log_id == ('') and passwd == ('') and user_name == (''):
        return render_template("new.html", error='全ての内容を入力してください。')

    elif log_id == (''):
        return render_template("new.html", error='ログインIDを入力してください。')

    elif passwd == (''):
        return render_template("new.html", error='パスワードを入力してください。')

    elif user_name == (''):
        return render_template("new.html", error='名前を入力してください。')

    elif passwd <= 8:
        return render_template("new.html", error='パスワードは8文字以上16文字以下です。')

    elif passwd >= 16:
        return render_template("new.html", error='パスワードは8文字以上16文字以下です。')

    else:

        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            path = UPLOAD_FOLDER + filename
            print(path)

            db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
            con = db.cursor()

            sql = 'insert into users(log_id,passwd,user_name,user_img) values(%s,%s,%s,%s)'

            try:

                test = con.execute(sql,[log_id,passwd,user_name,path])
                db.commit()
                print(test)

                result = con.fetchall()
                print(result)

            except MySQLdb.IntegrityError:

                error = 'すでに登録されているログインIDです。'

                return render_template('new.html', log_error=error)

            resp = make_response(redirect('http://localhost:8080/tweet'))
            resp.set_cookie("name", log_id)
            print(resp)

            return resp

        else:

            path = './static/img/profile.png'
            print(path)

            db = MySQLdb.connect( user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
            con = db.cursor()
            print('test')

            sql = 'insert into users(log_id,passwd,user_name,user_img) values(%s,%s,%s,%s)'

            try:

                test = con.execute(sql,[log_id,passwd,user_name,path])
                db.commit()
                print(test)

            except MySQLdb.IntegrityError:

                    error = 'すでに登録されているログインIDです。'

                    return render_template('new.html', log_error=error)

            resp = make_response(redirect('http://localhost:8080/tweet'))
            resp.set_cookie("name", log_id)
            print(resp)

            return resp

@application.route('/tweet')
def tweet():

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'select user_img, user_name from users where log_id = "' + data + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return render_template('tweet.html', tweets=result)

@application.route('/tweet', methods=['POST'])
def tweet_db():

    data = request.cookies.get("name", None)
    print(data)
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
    test = request.form['tweet']
    print(time_stamp)
    print(test)

    if len(test) is 0:

        return render_template('tweet.html', test='文字を入力して下さい')

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()

    sql = "insert into tweet(tweet_comment, created_at) values(%s, %s)"
    con.execute(sql, [test, time_stamp])

    print(sql)

    if sql is not False:

        db.commit()

        sql = "update tweet set user_id = '" + data + "' order by tw_id DESC limit 1 "
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        return redirect('http://localhost:8080/pro')

    return render_template('tweet.html')

@application.route('/search')
def search():

    data = request.cookies.get("name", None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select tweet_comment, created_at, user_name, user_img, tw_id from tweet inner join users on tweet.user_id = users.log_id where log_id != '" + data + "'"
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if sql is not False:

        sql = 'select user_name, user_img from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        view = con.fetchall()
        print(view)

    return render_template('search.html', rows=result, views=view)

@application.route('/search', methods=['POST'])
def search_db():

    data = request.cookies.get("name", None)
    print(data)
    search = request.form["search"]
    print(search)

    if search == (''):

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_name, user_img from users where log_id = "' + data + '"'
        con.execute(sql)
        db.commit()
        print(sql)

        search = con.fetchall()
        print(search)

        return render_template('search.html', test='キーワードを入力してください。', views=search)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select tweet_comment, created_at, user_name, user_img, tw_id from tweet inner join users on tweet.user_id = users.log_id where tweet_comment like '" '%' + search + '%' "' "
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if result == () :

        sql = 'select user_name, user_img from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        view = con.fetchall()
        print(view)

        return render_template('search.html', test='該当なし', views=view)

    else:

        sql = 'select user_name, user_img from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        view = con.fetchall()
        print(view)

    return render_template('search.html', rows=result, views=view)

@application.route('/pro')
def pro():

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select user_name, user_intro, user_img from users where log_id = '" + data + "'"
    con.execute(sql)
    db.commit()
    print(sql)
    test = con.fetchall()
    print(test)

    if sql is not False:

        sql = "select user_name, created_at, tweet_comment, user_img, tw_id from tweet inner join users on tweet.user_id = users.log_id where log_id = '" + data + "' "
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

    return render_template('pro.html', rows=result, pros=test)

@application.route('/pro/edit/<pro_id>')
def pro_view(pro_id=None):

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select user_name, user_img from users where log_id = '" + data + "' "
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if sql is not False:

        sql = "select tweet_comment from tweet where tw_id = '" + pro_id + "' "
        con.execute(sql)
        db.commit()
        print(sql)

        test = con.fetchall()
        print(test)

    return render_template('pro_edit.html', tests=result, views=test, pro_id=pro_id)

@application.route('/pro/edit/<pro_id>', methods=['POST'])
def pro_id(pro_id=None):

    data = request.cookies.get('name', None)
    print(data)
    write = request.form['write']
    print(write)
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(time_stamp)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'update tweet set tweet_comment = "' + write + '", created_at = "' + time_stamp + '" where tw_id = "' + pro_id + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/pro')

@application.route('/pro/delete/<pro_id>')
def pro_delete(pro_id=None):

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'delete from tweet where tw_id = "' + pro_id + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/pro')

@application.route('/edit')
def edit():

    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'select user_img, id, user_name, user_intro from users where log_id = "' + data + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return render_template('edit.html', pros=result)

@application.route('/edit', methods=['POST'])
def edit_db():


    data = request.cookies.get('name', None)
    print(data)
    passwd = request.form["passwd"]
    print(passwd)
    passwd_again = request.form["passwd_again"]
    print(passwd_again)
    user_name = request.form["user_name"]
    print(user_name)
    user_intro = request.form["user_intro"]
    print(user_intro)
    img_file = request.files["img_file"]
    print(img_file)


    if passwd == (''):

        error = 'passwordを入力してください！！'

        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_img, id, user_name, user_intro from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        return render_template('edit.html', pros=result, error=error)

    elif len(passwd) <= 8 or len(passwd) >= 16:

        error = 'パスワードを8文字以上16文字以内で入力してください！！'

        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_img, id, user_name, user_intro from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        return render_template('edit.html', pros=result, error=error)

    elif passwd != passwd_again:

        error = 'パスワードは両方とも同様の内容を入力してください！！'

        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_img, id, user_name, user_intro from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        return render_template('edit.html', pros=result, error=error)

    elif user_name == (''):

        error = '名前を入力してください！！'

        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_img, id, user_name, user_intro from users where log_id = "' + data + '" '
        con.execute(sql)
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        return render_template('edit.html', pros=result, error=error)

    else:

        if img_file and allowed_file(img_file.filename):

            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            path = UPLOAD_FOLDER + filename
            print(path)

            db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
            con = db.cursor()
            print('???')

            sql = "update users set user_img = %s, passwd = '" + passwd + "', user_name = '" + user_name + "', user_intro = '" + user_intro + "' where log_id = '" + data + "' "
            con.execute(sql, [path])
            db.commit()
            print(sql)

            result = con.fetchall()
            print(result)

            return redirect('http://localhost:8080/pro')

        else:

            path = './static/img/profile.png'

            data = request.cookies.get('name', None)
            print(data)

            db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
            con = db.cursor()
            print('???')

            sql = "update users set user_img = %s, passwd = '" + passwd + "', user_name = '" + user_name + "', user_intro = '" + user_intro + "' where log_id = '" + data + "' "
            con.execute(sql, [path])
            db.commit()
            print(sql)

            result = con.fetchall()
            print(result)

            return redirect('http://localhost:8080/pro')

@application.route('/oki/<user_id>')
def oki(user_id=None):

    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'insert into fab(tweet_id, log_id, fab_time) values(%s, %s, %s) on duplicate key update tweet_id = "' + user_id + '", log_id = "' + data + '", id=LAST_INSERT_ID(id) '
    con.execute(sql, [user_id, data, time_stamp])
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/oki')


@application.route('/oki')
def oki_db():

    data = request.cookies.get('name', None)
    print(data)

    coun = 1

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select tweet.tw_id, user_name, user_img, tweet_comment, tweet.created_at, users.log_id from tweet inner join users on tweet.user_id = users.log_id inner join fab on fab.tweet_id = tweet.tw_id where fab.log_id = '" + data + "' "
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if result == ():

        co = 3
        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = "select user_name, user_img from users where log_id = '" + data + "' "
        con.execute(sql)
        db.commit()
        print(sql)

        oki = con.fetchall()
        print(oki)

        return render_template('oki.html', com='誰かの投稿をお気に入りしてみよう👍', test=oki, count=co)

    else:

        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = "select user_name, user_img from users where log_id = '" + data + "' "
        con.execute(sql)
        db.commit()
        print(sql)

        okis = con.fetchall()
        print(okis)

    return render_template('oki.html', okis=result, count=coun, test=okis)

@application.route('/delete/<delete_id>')
def delete(delete_id=None):

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'delete from fab where tweet_id = "' + delete_id + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/oki')

@application.route('/pro/<user_pro>')
def user_pro(user_pro=None):

    data = request.cookies.get("name", None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = "select created_at, tweet_comment, user_name, user_img, tweet.tw_id from tweet inner join users on tweet.user_id = users.log_id where log_id = '" + user_pro + "' "
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if sql is not False:

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_name, user_intro, user_img, log_id from users where log_id = "' + user_pro + '"'
        con.execute(sql)
        db.commit()
        print(sql)

        user_pro = con.fetchall()
        print(user_pro)

    return render_template('user_pro.html', user_pro=result, pros=user_pro)

@application.route('/follower')
def follower():

    count = 1
    text = 'フォロー中'
    data = request.cookies.get('name', None)
    print(data)

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'select user_name, user_img, user_intro, user_id from users inner join follow on users.log_id = follow.user_id where follow_text = "' + text + '" AND follow.log_id = "' + data + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    if result == ():

        coun = 3

        data = request.cookies.get('name', None)
        print(data)

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = "select user_name, user_img from users where log_id = '" + data + "' "
        con.execute(sql)
        db.commit()
        print(sql)

        follow = con.fetchall()
        print(follow)

        return render_template('follower.html', com='誰かフォローしたら表示されるよ！', tests=follow, count=coun)

    if sql is not False:

        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'select user_name, user_img from users where log_id = "' + data + '"'
        con.execute(sql)
        db.commit()
        print(sql)

        test = con.fetchall()
        print(test)

    return render_template('follower.html', pros=result, tests=test, count=count)

@application.route('/follow/<follow_id>')
def top(follow_id=None):

    data = request.cookies.get('name', None)
    print(data)
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(time_stamp)
    text = 'フォロー中'

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('test')

    sql = 'insert into follow(log_id, user_id, follow_time, follow_text) values(%s, %s, %s, %s) on duplicate key update user_id = "' + follow_id + '", log_id = "' + data + '", id=LAST_INSERT_ID(id) '
    con.execute(sql, [data, follow_id, time_stamp, text])
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/follower')

@application.route('/follower/delete/<follower>')
def follower_delete(follower=follower):

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'delete from follow where user_id = "' + follower + '" '
    con.execute(sql)
    db.commit()
    print(sql)

    result = con.fetchall()
    print(result)

    return redirect('http://localhost:8080/follower')

@application.route('/pay')
def pay():

    return render_template('pay.html')

@application.route('/pay', methods=['POST'])
def pay_db():

    number = request.form['number']
    print(number)
    cardname = request.form['cardname']
    print(cardname)
    expiry = request.form['expiry']
    print(expiry)
    cvc = request.form['cvc']
    print(cvc)
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')

    if number == ('') and cardname == ('') and expiry == ('') and cvc == (''):
        error = 'すべての項目に適切の内容を入力してください！'
        return render_template('pay.html', error=error)
    elif number == (''):
        error = '正しくカード番号を入力してください！'
        return render_template('pay.html', error=error)
    elif cardname == (''):
        error = 'カード保有者の名前を入力してください！'
        return render_template('pay.html', error=error)
    elif expiry == (''):
        error = 'mm/yyを入力してください！'
        return render_template('pay.html', error=error)
    elif cvc == (''):
        error = 'cvcを入力してください！'
        return render_template('pay.html', error=error)
    elif number.startswith('4') or number.startswith('5') or number.startswith('35') or number.startswith('37') or number.startswith('2222'):

        print('test')
        db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'insert into credit(cardnumber, card_name, mmyy, cvc, created_at) values(%s, %s, %s, %s, %s) on duplicate key update cardnumber = "' + number + '", card_name = "' + cardname + '", id=LAST_INSERT_ID(id)'
        con.execute(sql, [number, cardname, expiry, cvc, time_stamp])
        db.commit()
        print(sql)

        result = con.fetchall()
        print(result)

        return redirect('http://localhost:8080/check')
    else:
        error = '正しいカード番号を入力してください！'
        return render_template('pay.html', error=error)

@application.route('/info')
def info():

    return render_template('info.html')

@application.route('/yuryou')
def test():

    return render_template('yuryou.html')

@application.route('/check')
def check():

    db = MySQLdb.connect(user='root', passwd='asatai95', host='localhost', db='tukutter', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'delete from credit where cardnumber not in (select card_number from test where credit.cardnumber = test.card_number and credit.id=LAST_INSERT_ID(credit.id))'
    test = con.execute(sql)
    db.commit()
    print(sql)
    print(test)

    if test == 1:

        return render_template('pay.html', error='存在しないカードアカウントです。')

    else:

        result = con.fetchall()
        print(result)

        return render_template('check.html')

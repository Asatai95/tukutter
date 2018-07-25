import MySQLdb
from flask import Flask, render_template, redirect, request, make_response

application = Flask(__name__)

@application.route('/')
def test():

    print('test')

    return render_template('single_top.html')

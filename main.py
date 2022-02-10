#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import psycopg2

from flask import Flask
from flask import redirect, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '49-is-like-69-but-20-less'

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return redirect('/send_more')


@app.route('/send_more', methods=['POST', 'GET'])
def send_more():
    if request.method == 'GET':
        return render_template('send_more.html')
    elif request.method == 'POST':
        return redirect('/')


def main():
    cur = conn.cursor()
    cur.execute("""CREATE TABLE addressees (
        id                INTEGER NOT NULL,
        to_whom_name      VARCHAR NOT NULL,
        to_whom_surname   VARCHAR NOT NULL,
        to_whom_class     VARCHAR NOT NULL,
        from_whom_name    VARCHAR,
        from_whom_surname VARCHAR,
        from_whom_class   VARCHAR,
        your_wish         TEXT,
        valentine_type    INTEGER NOT NULL,
        PRIMARY KEY (
            id
        )
    );
    """)
    conn.close()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


main()

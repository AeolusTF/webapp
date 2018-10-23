#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/20 0020 14:25
# @Author  : Aeolus
# @File    : webapp.py
# @Software: PyCharm

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def aeolus():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return u'请先选择文件在上传'
    filename = file.filename
    #files = file.read()
    file.save('static/%s' %filename)
    return '/static/%s' %filename

if __name__ == '__main__':
    app.debug = True
    app.run()
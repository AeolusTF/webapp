#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/20 0020 14:29
# @Author  : Aeolus
# @File    : guiapp.py
# @Software: PyCharm

from Tkinter import *
from tkFileDialog import  *
import urllib2


def upload():
    askopenfilename() #打开文件 返回值：文件绝对路径
    file = open(filepath,'rb').read()
    data = '''------WebKitFormBoundaryfb2OAuAEh0TXFtvH
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: application/octect-stream

[file]
------WebKitFormBoundaryfb2OAuAEh0TXFtvH--''' %filepath.split('/')[-1])

    data = bytes(data)
    data.replace(bytes('[file]'),file)
    req = urllib2.Request('http://127.0.0.1:5000/upload')
    req.add_header('Content-Type','multipart/form-data;boundary=----WebKitFormBoundaryfb2OAuAEh0TXFtvH')
    html = urllib2.urlopen(req,data=data).read()
    ent.insert(0,'http://127.0.0.1:5000%s' %html)



def download():
    file = urllib2.urlopen(ent.get()).read()
    filepath = asksaveasfilename()
    with open(filepath,'wb') as fn :
        fn.write(file)

root = Tk()
root.title('文件上传')
root.geometry('+900+300')
ent = Entry(root,width=40)
ent.grid()
btn_upload = Button(root,text=' 上 传 ',command=upload)
btn_upload.grid()
btn_download = Button(root,text=' 下 载 ',command=download)
btn_download.grid()
mainloop()
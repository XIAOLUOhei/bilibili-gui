from tabnanny import check
from tkinter import *
from bilibili_api import settings
from bilibili_api import sync
from bilibili_api import *
from bilibili_api.session import Session, Event, EventType
from bilibili_api.utils.picture import Picture
from numpy.ma.core import choose
from selenium.webdriver.common.devtools.v85.page import create_isolated_world
from bilibili_api import session
import tkinter as tk
import time
from tkinter import *

login_top = tk.Tk()
login_top.geometry("800x600")
login_top.title("bilibili登录")
def sms():
    global p,s
    p = tk.Entry(login_top)
    code = tk.Entry(login_top)
    p.pack()
    code.pack()
def mi():
    global a,b,pass_top
    w = 0
    if w == 0:
        pass_top = tk.Tk()
        pass_top.geometry("300x200")
        pass_top.title("密码登录")
        w = 1
    elif w == 1:
        wrr = tk.Tk()
        wrr.geometry("200x200")
        wrr_text = tk.Label(wrr, text="已存在窗口", height=100, width=100, fg="rad")
        time.sleep(1)
        wrr.quit()
    user_text = tk.Label(pass_top,text="账号:")
    pass_text = tk.Label(pass_top,text="密码:")
    user_text.place(x=0,y=10,anchor = NW)
    pass_text.place(x=0,y=30,anchor = NW)
    a = tk.Entry(pass_top,text="账号")
    b = tk.Entry(pass_top,text="密码")
    a.place(x=40,y=10,anchor = NW)
    b.place(x=40,y=30,anchor = NW)
    login_btn = tk.Button(pass_top, text="登录", command=mi_login)
    login_btn.place(x=150,y=150,anchor = NW)
    pass_top.mainloop()
def mi_login():
    global username,password,name
    username = a.get()
    password = b.get()
    c = login_with_password(username, password)
    credential = c
    name = sync(get_self_info(credential))['name']
    hello = tk.Label(pass_top, text=name, height=20, width=80)
    hello.pack()

hi = tk.Label(login_top,text="选择登录方式",height=20,width=80,fg="red")
pass_btn = tk.Button(login_top,text="账号密码登录",fg ="blue",command=mi)

sms_btn.pack()
hi.pack()
pass_btn.pack()
login_top.mainloop()

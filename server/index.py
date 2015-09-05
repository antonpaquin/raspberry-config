#! /usr/bin/python3
import os
from mod_python import Cookie

def index(req):
    cookies = Cookie.get_cookies(req)
    if 'User' in cookies and cookies['User'] == 'Anton':
        return showHome(req)
    else:
        return showBlock(req)

def showHome(req):
    with open('Utils/HTML/main/home.html') as home_f:
        home = home_f
    return home

def showBlock(req):
    with open('Utils/HTML/main/block.html') as block_f:
        block = block_f
    return block

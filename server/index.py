#! /usr/bin/python3
from mod_python import Cookie

def index(req):
    cookies = Cookie.get_cookies(req)
    if cookise.has_key('User') and cookies['User'].value == 'Anton':
        return showPage(req)
    else:
        return showBlock(req)

def showPage(req):
    with open('/var/www/Utils/HTML/main/home.html') as home_f:
        home = home_f.read()
    return home

def showBlock(req):
    with open('/var/www/Utils/HTML/main/block.html') as block_f:
        block = block_f.read()
    return block

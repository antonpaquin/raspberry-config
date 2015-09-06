#! /usr/bin/python3
import os
from mod_python import Cookie

def index(req):
    cookies = Cookie.get_cookies(req)
    if cookise.has_key('User') and cookies['User'].value == 'Anton':
        return showPage(req)
    else:
        return showBlock(req)

def showPage(req):
    with open('/var/www/Utils/HTML/torrents/main.html') as home_f:
        home_h = home_f.read()
    with open('/var/www/Utils/HTML/torrents/main_listItem.html') as item_f:
        item_h = item_f.read()
    with open('/var/www/Utils/HTML/torrents/main_head.html') as head_f:
        head_h = head_f.read()
    with open('/var/www/Utils/HTML/torrents/main_cap.html') as cap_f:
        cap_h = cap_f.read()

    items_h = head_h
    items_l = getActiveTorrents()
    for item in items_l:
        item_s = item_h
        item_s = item_s.replace('#name#',item['name'])
        item_s = item_s.replace('#progress#',item['progress'])
        item_s = item_s.replace('#speed#',item['speed'])
        item_s = item_s.replace('#ratio#',item['ratio'])
        item_s = item_s.replace('#size#',item['size'])
        items_h += item_s
    items_h += cap_h
    
    home_h = home_h.replace('#torrents#',items_h)
    return home_h

def getActiveTorrents():
    return [] #TODO
    #list of dicts by age with name, progress, speed, ratio, size keys

def showBlock(req):
    with open('/var/www/Utils/HTML/main/block.html') as block_f:
        block = block_f.read()
    return block

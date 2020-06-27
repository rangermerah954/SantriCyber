# SantriCyber
Berawal Dari Kegagalan..# -*- coding: utf-8 -*-

# recode by Mr.S4N75I

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

    print '\x1b[1;91m[!] Closed'

    os.sys.exit()

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo = " \x1b[1;97m█████████\n \x1b[1;97m█▄█████▄█         \x1b[1;96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●\n \x1b[1;97m█ \x1b[1;91m▼▼▼▼▼  \x1b[1;97m- _ --_-- \x1b[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n \x1b[1;97m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n \x1b[1;97m█ \x1b[1;91m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \x1b[1;93mPRO v1.7\n \x1b[1;97m█████████         \x1b[1;96m«==========✧==========»\n \x1b[1;97m ██ ██\n \x1b[1;97m╔════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;93m* \x1b[1;97mReCode  \x1b[1;91m:          \x1b[1;96m Mr.GameOver  \x1b[1;97m            ║\n \x1b[1;97m║ \x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m:\x1b[1;92m\x1b[92mhttps://github.com/MrGameOver16\x1b[    \x1b[1;97m 

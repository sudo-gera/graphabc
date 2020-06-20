#!/data/data/com.termux/files/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen as u
from urllib.parse import unquote as uqu
from json import loads as l
from sys import argv
import os
import random
from urllib.request import urlopen
from json import loads
from json import dumps
from urllib.parse import quote
from time import sleep
from time import time
from time import asctime
from traceback import format_exc as error
from os import popen
from random import shuffle
from os.path import exists
from os.path import abspath
from os import chdir
from random import randint
from threading import Thread as thread
def mod(q):
 exec('import '+q)
 return eval(q)

pth=abspath(argv[0])
pth=pth[:-len(pth.split('/')[-1])]
chdir(pth)

users=[]

stopped=0

class MyServer(BaseHTTPRequestHandler):
 def do_GET(self):
  if stopped:
   raise KeyboardInterrupt
  self.send_response(200)
  path=self.path
  path=str(path)[1:]
  path=path.split('z')
  global users
  if len(path)<3 or not path[0].isdigit() or not path[1].isdigit():
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(str(len(users)).encode())
   return
  to=int(path[1])
  fr=int(path[0])
  path=path[2]
  while to>=len(users):
   users+=['']
  users[to]+=path
  self.send_header("Content-type", "text/html; charset=utf-8")
  self.end_headers()
  self.wfile.write(users[fr].encode())
  users[fr]=''

 def log_message(*q):
  pass

myServer=None
def __jrun():
 global MyServer
 global myServer
 myServer = HTTPServer(('127.0.0.1', 2938), MyServer)
 try:
  myServer.serve_forever()
 except:
  pass
 myServer.server_close()

def __jstop():
 global myServer
 myServer.server_close()

def serst():
 global stoped
 stoped=1

mod('atexit').register(serst)
mod('atexit').register(__jstop)

def stdreq(q=''):
 c=u('http://127.0.0.1:2938/'+q)
 t=c.read().decode()
 c.close()
 del(c)
 mod('gc').collect()
 return t

fr=to=0

gbuff=[]

def ugb(s):
 ext=[]
 for w in s.split('a'):
  try:
   d=int(w)
   ext+=[d]
  except:
   pass
 return ext

def post(*q):
 q=[str(w) for w in q]
 global gbuff
 gbuff+=ugb(stdreq(str(fr)+'z'+str(to)+'z'+'a'.join(q)+('a' if q else '')))

def reg():
 global fr,to
 fr=int(stdreq())
 to=fr+1
 post()

def __run():
 global __jrun
 thread(target=__jrun,args=()).start()
 sleep(0.1)
 reg()

__run()



def get():
 global gbuff
 while gbuff==[]:
  post()
  sleep(0.101)
 d=gbuff[0]
 gbuff=gbuff[1:]
 return d


sleep(0.1)
mod('subprocess').Popen('/home/gera/graph.exe',stdin=-1,stdout=-1,stderr=-1)

def putpixel(x,y,r,g,b):
 post(0)
 post(x)
 post(y)
 post(r)
 post(g)
 post(b)

def getpixel(x,y):
 post(1)
 post(x)
 post(y)
 return [get(),get(),get()]


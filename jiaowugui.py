#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import urllib
import re
import requests
import Image
import urllib
from bs4 import BeautifulSoup
import math

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def request():
    global s
    s=requests.Session()
    global codefanhui
    codefanhui=s.get('http://202.119.206.61/CheckCode.aspx')
    codefile=open('checkcode.gif','wb')        
    codefile.write(codefanhui.content[:-736])
    codefile.close()
    global my_headers1
    my_headers1 = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
             'Host': '202.119.206.61',
             'Referer': 'http://202.119.206.61/',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding':'gzip, deflate',
             'Cookie':codefanhui.headers['Set-Cookie'][:43],
             'Connection':'keep-alive',
             'Content-Type':'application/x-www-form-urlencoded',
             'Content-Length':'194'
             }
    global my_headers3
    my_headers3={
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
             'Host': '202.119.206.61',
             'Referer': 'http://202.119.206.61/xscj_gc.aspx?xh=01130122&xm=%B9%CB%BC%E1%B1%F2&gnmkdm=N121605',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding':'gzip, deflate',
             'Cookie':codefanhui.headers['Set-Cookie'][:43],
             'Connection':'keep-alive',
             'Content-Type':'application/x-www-form-urlencoded',
             'Content-Length':'1981'
             }


def checkcode():
    global checkcode_image
    checkcode_image=Tkinter.PhotoImage(file='checkcode.gif')
    global label_checkcode
    label_checkcode=Tkinter.Label(top,image=checkcode_image)
    label_checkcode.grid(row=3,column=0)


def resetcheckcode(event):
    request()
    checkcode()

def prepare_login_information():
    global information_login
    information_login={'__VIEWSTATE':'dDwyODE2NTM0OTg7Oz4GUd8zlUl76ima53xfnSJV4/6k1Q==',
             'txtUserName':var_stuid.get(),  #  shuru  xuehao he mima
             'TextBox2':var_passwd.get(),
             'txtSecretCode':var_checkcode.get(),
             'RadioButtonList1':u'学生',
             'Button1':'',
             'lbLanguage':'',
             'hidPdrs':'',
             'hidsc':''
             }
    

def prepare_score_information():
    global name
    name=getName(jiaowu_shouye.content)
    urldata = urllib.urlencode({
		'xh':var_stuid.get(),
		'gnmkdm': 'N121605',
                'xm':name

		})
    global scoreurl
    scoreurl='http://202.119.206.61/xscj_gc.aspx?'+urldata
    

def logincumt():
    global jiaowu_shouye
    jiaowu_shouye=s.post('http://202.119.206.61/default2.aspx',
                         data=information_login,
                         headers=my_headers1,cookies=codefanhui.cookies)

def getName(loginPage):
    page =  unicode(loginPage, 'gb2312').encode("utf-8")
    Sname = r'<span id="xhxm">(.+)同学</span>'
    Sname = re.compile(Sname)
    #try:
    return Sname.findall(page)[0]
    #except IndexError, e:
        #raise e
        #print "first User-name or password error, try again!"


def postscore():
    chengji_qingqiu_2=s.post(url=scoreurl,headers=my_headers3,data=information_chengji,cookies=codefanhui.cookies)
    cjym=open('cjym.html','wb')                      
    cjym.write(chengji_qingqiu_2.text.decode('utf-8').encode('gb2312'))
    cjym.close()


def baocuncj():
    soup=BeautifulSoup(open('cjym.html'),'lxml')
    table=soup.find('table')
    for row in table.find_all('tr'):
        cells=row.find_all('td')
        if len(cells)==20:
            kcmc=cells[3].find(text=True)
            kcmclist.append(kcmc)
            xf=cells[6].find(text=True)
            xflist.append(xf)
            jd=cells[7].find(text=True)
            jdlist.append(jd)
            qmcj=cells[12].find(text=True)
            qmcjlist.append(qmcj)
    
def jisuanpjf():
    sumxfcj=0.0    #学分和成绩总和
    sumxf=0.0
    for index,item in enumerate(qmcjlist):
        if item.isdigit():
            sumxfcj=sumxfcj+float(item)*float(xflist[index])
            sumxf=sumxf+float(xflist[index])
    return sumxfcj/sumxf

def start(event):
    prepare_login_information()
    logincumt()
    prepare_score_information()
    postscore()
    baocuncj()
    
    Tkinter.Label(frame,text=kcmclist[0]).grid(row=0,column=0)
    Tkinter.Label(frame,text=jdlist[0]).grid(row=0,column=1)
    Tkinter.Label(frame,text=xflist[0]).grid(row=0,column=2)
    Tkinter.Label(frame,text=qmcjlist[0]).grid(row=0,column=3)
    Tkinter.Label(frame,text=kcmclist[0]).grid(row=0,column=4)
    Tkinter.Label(frame,text=jdlist[0]).grid(row=0,column=5)
    Tkinter.Label(frame,text=xflist[0]).grid(row=0,column=6)
    Tkinter.Label(frame,text=qmcjlist[0]).grid(row=0,column=7)
    Tkinter.Label(frame,text=kcmclist[0]).grid(row=0,column=8)
    Tkinter.Label(frame,text=jdlist[0]).grid(row=0,column=9)
    Tkinter.Label(frame,text=xflist[0]).grid(row=0,column=10)
    Tkinter.Label(frame,text=qmcjlist[0]).grid(row=0,column=11)
    
    n=len(kcmclist)
    index=1
    while index<n:
        if index%3==1:
            Tkinter.Label(frame,text=kcmclist[index]).grid(row=index/3+2,column=0)
            Tkinter.Label(frame,text=jdlist[index]).grid(row=index/3+2,column=1)
            Tkinter.Label(frame,text=xflist[index]).grid(row=index/3+2,column=2)
            Tkinter.Label(frame,text=qmcjlist[index]).grid(row=index/3+2,column=3)
        if index%3==2:
            Tkinter.Label(frame,text=kcmclist[index]).grid(row=index/3+2,column=4)
            Tkinter.Label(frame,text=jdlist[index]).grid(row=index/3+2,column=5)
            Tkinter.Label(frame,text=xflist[index]).grid(row=index/3+2,column=6)
            Tkinter.Label(frame,text=qmcjlist[index]).grid(row=index/3+2,column=7)
        if index%3==0:
            Tkinter.Label(frame,text=kcmclist[index]).grid(row=index/3+1,column=8)
            Tkinter.Label(frame,text=jdlist[index]).grid(row=index/3+1,column=9)
            Tkinter.Label(frame,text=xflist[index]).grid(row=index/3+1,column=10)
            Tkinter.Label(frame,text=qmcjlist[index]).grid(row=index/3+1,column=11)
            
        index=index+1
    Tkinter.Label(frame,text=u'加权平均分：').grid(row=int(math.ceil(n/3))+2,column=0)
    Tkinter.Label(frame,text=jisuanpjf()).grid(row=int(math.ceil(n/3))+2,column=1)
    






global xflist
xflist=[]
global jdlist
jdlist=[]
global qmcjlist
qmcjlist=[]
global kcmclist
kcmclist=[]
global information_chengji
information_chengji={'__VIEWSTATE':'dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwwMTEzMDEyMjs+PjtsPGk8MT47PjtsPHQ8O2w8aTwxPjtpPDM+O2k8NT47aTw3PjtpPDk+O2k8MTE+O2k8MTM+O2k8MTY+O2k8MjY+O2k8Mjc+O2k8Mjg+O2k8MzU+O2k8Mzc+O2k8Mzk+O2k8NDE+O2k8NDU+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOWtpuWPt++8mjAxMTMwMTIyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrpob7lnZrlvaw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8muiuoeeul+acuuenkeWtpuS4juaKgOacr+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77yaOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlLXlrZDkv6Hmga/np5HlrabkuI7mioDmnK87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOihjOaUv+ePre+8mueUteWtkOS/oeaBr+enkeWtpuS4juaKgOacrzIwMTMtMDTnj607Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTMwODIwOz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPFhOO1hOOz4+Oz47dDxpPDQ+O0A8XGU7MjAxNS0yMDE2OzIwMTQtMjAxNTsyMDEzLTIwMTQ7PjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7MjAxMy0yMDE0Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LnByaW50KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDQ+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPFpJU1Q7Pj47Pjs7Pjs+Pjs+Pjs+Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+Oz6tOYI8CHESY/jjYzx4/a0GJHUODQ==',
                     'ddlXN':'',
                     'ddlXQ':'',
                     'Button1':u'按学期查询',
                     }
top = Tkinter.Tk()
top.title('cumt')

request()



#label_name=Tkinter.Label(top,text=u'姓名：')
#label_name.grid(row=0,column=0)
#var_name=Tkinter.StringVar(top)
#entry_name=Tkinter.Entry(top,textvariable=var_name)
#entry_name.grid(row=0,column=1,columnspan=2,sticky='w')
label_stuid=Tkinter.Label(top,text=u'学号：')
label_stuid.grid(row=1,column=0)
global var_stuid
var_stuid=Tkinter.StringVar(top)
entry_stuid=Tkinter.Entry(top,textvariable=var_stuid)
entry_stuid.grid(row=1,column=1,columnspan=2,sticky='w')

label_passwd=Tkinter.Label(top,text=u'密码：')
label_passwd.grid(row=2,column=0)
global var_passwd
var_passwd=Tkinter.StringVar(top)
entry_passwd=Tkinter.Entry(top,textvariable=var_passwd,show='*')
entry_passwd.grid(row=2,column=1,columnspan=2,sticky='w')

#label_checkcode=Tkinter.Label(top,text=u'验证码：')
#label_checkcode.grid(row=2,column=0)

checkcode()
global var_checkcode
var_checkcode=Tkinter.StringVar(top)
entry_checkcode=Tkinter.Entry(top,textvariable=var_checkcode)
entry_checkcode.grid(row=3,column=1,sticky='w')


button_submit=Tkinter.Button(top,text=u'提交',width=10)
button_submit.bind('<Button-1>',start)      ############ not end
button_submit.grid(row=2,column=4,sticky='w')

button_reset=Tkinter.Button(top,text=u'重置',width=10)
button_reset.bind('<Button-1>',resetcheckcode)############## not end
button_reset.grid(row=2,column=5,sticky='w')

frame=Tkinter.Frame(top)
frame.grid(row=4,column=0,columnspan=3,sticky='w')




Tkinter.mainloop()



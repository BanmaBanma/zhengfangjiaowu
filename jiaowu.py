#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import Image
from cjshuchu import xianshicj
###################     from io import StringIO
###################     f.content[:-736]
###################     编码
################

s=requests.Session()
code=s.get('http://202.119.206.61/CheckCode.aspx')
####################    i=Image.open(StringIO(code.content))
####################    i.show()

#windows
'''codefile=open(r'E:\computer\Python\checkcode.gif','wb')        
codefile.write(code.content[:-736])
codefile.close()                                                                                               #        写入验证码到本地  
im=Image.open(r'E:\computer\Python\checkcode.gif')          
im.show()'''
#linux
codefile=open('checkcode.gif','wb')        
codefile.write(code.content[:-736])
codefile.close()                                                                                               #        写入验证码到本地  
im=Image.open('checkcode.gif')          
im.show()
codeinfo=raw_input('请输入验证码：')
################################################################################################################
################################################################################################################
##############################　　　　　　登录请求头　　　　　##################################################
################################################################################################################
my_headers1 = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
             'Host': '202.119.206.61',
             'Referer': 'http://202.119.206.61/',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding':'gzip, deflate',
             'Cookie':code.headers['Set-Cookie'][:43],
             'Connection':'keep-alive',
             'Content-Type':'application/x-www-form-urlencoded',
             'Content-Length':'194'
 }

################################################################################################################
################################################################################################################
##############################　　　　　　成绩请求头　　　　　##################################################
################################################################################################################
my_headers3={
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
             'Host': '202.119.206.61',
             'Referer': 'http://202.119.206.61/xscj_gc.aspx?xh=01130122&xm=%B9%CB%BC%E1%B1%F2&gnmkdm=N121605',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding':'gzip, deflate',
             'Cookie':code.headers['Set-Cookie'][:43],
             'Connection':'keep-alive',
             'Content-Type':'application/x-www-form-urlencoded',
             'Content-Length':'1981'
             
 }
#####################################        多余         #####################################################

'''my_headers2 = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
             'Host': '202.119.206.61',
             'Referer': 'http://202.119.206.61/xs_main.aspx?xh=01130122',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding':'gzip, deflate',
             'Cookie':code.headers['Set-Cookie'][:43],
             'Connection':'keep-alive',
             
 }'''


################################################################################################################
################################################################################################################
##############################　　　　　　登录post数据　　　　　################################################
################################################################################################################    

information_login={'__VIEWSTATE':'dDwyODE2NTM0OTg7Oz4GUd8zlUl76ima53xfnSJV4/6k1Q==',
             'txtUserName':'studentid',  #  shuru  xuehao he mima
             'TextBox2':'passwd',
             'txtSecretCode':codeinfo,
             'RadioButtonList1':u'学生',
             'Button1':'',
             'lbLanguage':'',
             'hidPdrs':'',
             'hidsc':''
             }
################################################################################################################
################################################################################################################
##############################　　　　　　成绩请求post数据　　　　　############################################
################################################################################################################
information_chengji={'__VIEWSTATE':'dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwwMTEzMDEyMjs+PjtsPGk8MT47PjtsPHQ8O2w8aTwxPjtpPDM+O2k8NT47aTw3PjtpPDk+O2k8MTE+O2k8MTM+O2k8MTY+O2k8MjY+O2k8Mjc+O2k8Mjg+O2k8MzU+O2k8Mzc+O2k8Mzk+O2k8NDE+O2k8NDU+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOWtpuWPt++8mjAxMTMwMTIyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrpob7lnZrlvaw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8muiuoeeul+acuuenkeWtpuS4juaKgOacr+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77yaOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlLXlrZDkv6Hmga/np5HlrabkuI7mioDmnK87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOihjOaUv+ePre+8mueUteWtkOS/oeaBr+enkeWtpuS4juaKgOacrzIwMTMtMDTnj607Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTMwODIwOz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPFhOO1hOOz4+Oz47dDxpPDQ+O0A8XGU7MjAxNS0yMDE2OzIwMTQtMjAxNTsyMDEzLTIwMTQ7PjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7MjAxMy0yMDE0Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LnByaW50KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDQ+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPFpJU1Q7Pj47Pjs7Pjs+Pjs+Pjs+Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+Oz6tOYI8CHESY/jjYzx4/a0GJHUODQ==',
                     'ddlXN':'',
                     'ddlXQ':'',
                     'Button1':u'按学期查询',
                     }
#code.headers['Set-Cookie'][18:43]
cookiess=code.cookies


################################         登录教务处　　　　　#################################

jiaowu_shouye=s.post('http://202.119.206.61/default2.aspx',data=information_login,headers=my_headers1,cookies=cookiess)




#yemian=s.get('http://202.119.206.61/xs_main.aspx?xh=01130122')
#print yemian.status_code
#print yemian.text
#print jiaowuwangye.status_code
#jiaowuwangye.text
#print  jiaowuwangye.text
#chengji_qingqiu_1=s.get('http://202.119.206.61/xscj_gc.aspx?xh=01130122&xm=%B9%CB%BC%E1%B1%F2&gnmkdm=N121605',headers=my_headers2)
#print chengji_qingqiu_1.text



###################################          发起成绩请求　　　　　　　##########################
chengji_qingqiu_2=s.post('http://202.119.206.61/xscj_gc.aspx?xh=01130122&xm=%B9%CB%BC%E1%B1%F2&gnmkdm=N121605',headers=my_headers3,data=information_chengji,cookies=cookiess)


###########       测试输出样例       ######################
#print chengji_qingqiu_2.text


#windows
'''cjym=open(r'E:\computer\Python\pachong\cjym.html','wb')                      ############################################
cjym.write(chengji_qingqiu_2.text.decode('utf-8').encode('gb2312'))          #      将返回的成绩页面源码保存到本地　　　#
cjym.close()                                                                 ############################################

xianshicj(r'E:\computer\Python\pachong\cjym.html')'''


#linux
cjym=open('cjym.html','wb')                      ############################################
cjym.write(chengji_qingqiu_2.text.decode('utf-8').encode('gb2312'))          #      将返回的成绩页面源码保存到本地　　　#
cjym.close()                                                                 ############################################

xianshicj('cjym.html')





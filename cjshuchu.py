#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
################################################################################
###########################　　　格式化输出中文　　#############################
################################################################################
def alignment(str1, space, align = 'left'):
    length = len(str1.encode('gb2312'))
    space = space - length if space >=length else 0
    if align == 'left':
        str1 = str1 + ' ' * space
    elif align == 'right':
        str1 = ' '* space +str1
    elif align == 'center':
        str1 = ' ' * (space //2) +str1 + ' '* (space - space // 2)
    return str1


################################################################################
########################     显示成绩，并输出加权平均分     ####################
########################    对于成绩显示为评级的（及格，良好。。。）不计算######
################################################################################
def xianshicj(chengji):
    soup=BeautifulSoup(open(chengji),'lxml')
#soup=BeautifulSoup(chengji,'lxml')
    table=soup.find('table')
#print table              　　　　　　　 ##########　测试输出代码    ###########
#print soup.table
    xflist=[]
    jdlist=[]
    qmcjlist=[]
    for row in table.find_all('tr'):
        cells=row.find_all('td')
        if len(cells)==20:
            name=cells[0].find(text=True)
#            if not name:　　　　　　　
#                continue
            kcmc=cells[3].find(text=True)
            xf=cells[6].find(text=True)
            xflist.append(xf)
            jd=cells[7].find(text=True)
            jdlist.append(jd)
            qmcj=cells[12].find(text=True)
            qmcjlist.append(qmcj)
            print ('%s %s %s %s' %(alignment(kcmc,45),alignment(xf,4),alignment(jd,10),qmcj))
    sumxfcj=0.0    #学分和成绩总和
    sumxf=0.0
    for index,item in enumerate(qmcjlist):
        if item.isdigit():
#            print item,
#            print ':',
#            print xflist[index],
            sumxfcj=sumxfcj+float(item)*float(xflist[index])
            sumxf=sumxf+float(xflist[index])

    print
    print u'加权平均分：',
    print sumxfcj/sumxf

##############################################################################

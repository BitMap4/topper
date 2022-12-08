# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:33:57 2022

@author: ritu
"""

import pymysql as pm
conn=pm.connect(host="localhost",user="root",passwd="")
cursor=conn.cursor()
cursor.execute('create database if not exists project')
cursor.execute('use project')
cursor.execute("create table if not exists userdetails(username varchar(50),\
                Pwd varchar(20))")

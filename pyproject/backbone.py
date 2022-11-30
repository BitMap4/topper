# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:33:57 2022

@author: ritu
"""

import pymysql as pm
conn=pm.connect(host="localhost",user="root",passwd="Moody1826")
cursor=conn.cursor()
cursor.execute('create database if not exists project')
cursor.execute('use project')
cursor.execute("create table if not exists item_repository(username varchar(50),price int(9),\
                item_name varchar(90),tags varchar(200))")

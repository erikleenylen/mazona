# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:38:11 2015

Updated 3/15/16

function: py_to_postgresql_amazon_data.py

functions:
    createTable:
        purpose of createTable is to add a table to postgresql database
        inputs:
            dbName: name of database, e.g., 'testdb'
            tableName: name of table, e.g., 'Items'
            user: default username is root
    deleteTable:
        purpose of deleteTable is to delete previously existing table in postgresql database
        inputs:
            dbName: name of database, e.g., 'testdb'
            tableName: name of table, e.g., 'Items'
            user: default username is root
    insertData:
        purpose of insertData is to insert dictionary of data into previously existing table in postgresql database
        inputs:
            dbName: name of database, e.g., 'testdb'
            tableName: name of table, e.g., 'Items'
            fields: are the table fields
            dataInsert: is a dictionary of fields:values
            user: default username is root

@author: erikleenylen
"""

import psycopg2
import pdb
import re

def deleteTable(dbName,tableName,user='root'):
    '''function deletes table: tableName in database: dbName.'''
    con = None
    connectTo = "dbname='"+dbName+"' user='"+str(user)+"'"
    con = psycopg2.connect(connectTo)
    cur = con.cursor()
    # cur now points to dbName
    strToSQL = 'DROP TABLE IF EXISTS %s' % (tableName)
    cur.execute(strToSQL)
    if con:
        con.close()

def createTable(dbName,tableName,tableDict={},user='root'):
    '''function creates table: tableName in database: dbName'''
    con = None
    connectTo = "dbname='"+dbName+"' user='"+str(user)+"'"
    con = psycopg2.connect(connectTo)
    cur = con.cursor()
    
    # if no table specified, use these default values for amazon product information
    if len(tableDict) == 0:
        strToSQL = 'CREATE TABLE %s (itemID VARCHAR(20),itemName VARCHAR(300),itemURL VARCHAR(200),dateFirstAvail VARCHAR(200),itemPrice VARCHAR(200),itemDescription VARCHAR(1000),itemCategory VARCHAR(200))' % (tableName)
    else:
        # if tableDict specified, create table with table dictionary (key:value) properties:
        # key = variable name
        # value = character length
        # according to format:
        # (itemID VARCHAR(20),itemName VARCHAR(300),itemURL VARCHAR(200),dateFirstAvail VARCHAR(200),itemPrice VARCHAR(200),itemDescription VARCHAR(1000),itemCategory VARCHAR(200)
        tableItems = '('
        for itemnum,items in enumerate(tableDict.items()):
            tableItems = tableItems + items[0] + ' VARCHAR('+str(items[1])+')'
            if itemnum not len(tableDict.items())-1:
                tableItems = tableItems +','
        tableItems = tableItems+')'
        strToSQL = 'CREATE TABLE %s '+tableItems % (tableName)
    cur.execute(strToSQL)
    con.commit()
    if con:
        con.close()
        
def insertData(dbName,tableName,fields,dataInsert,user='root'):     
    '''function connects to database, insert data according to dataInsert '''   
    con = None
    connectTo = "dbname='"+dbName+"' user='"+str(user)+"'"
    con = psycopg2.connect(connectTo)
    cur = con.cursor()

    # FORMAT DATABASE INPUT BASED ON: FIELDS AND THE DATA BEING INSERTED
    tab_string = ', '.join([_ for _ in fields])
    var_string = ', '.join(['%s' for _ in range(len(dataInsert))])
    query_string = 'INSERT INTO %s (%s) VALUES (%s);' % (tableName, tab_string, var_string)

    # Insert data via query string to database
    cur.execute(query_string,dataInsert)    
    con.commit()    
    if con:
        con.close()


if __name__=='__main__':
    ''' this if-statement is called if this whole function is called directly from the command line
    --- used for debugging, but ignored when accessed by another function'''
    dbName = 'testdb'
    tableName = 'Item'
    fields = ['itemID','itemName']
    dataInsert = ('23982938532895','fake item test name')
    insertData(dbName,tableName,fields,dataInsert)



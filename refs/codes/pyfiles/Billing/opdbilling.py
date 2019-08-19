from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys

import db_conf as con
import datetime as dt,time as tm

db = con.db
cursor=db.cursor()

now = dt.datetime.now()
dtd = now.strftime('%Y')

import insertdata as ins
import updatedata as up


def getPatientRegnoBilling():
    try:
        if request.method == 'POST':
            regno = request.form['regno']
            sql="select o.regno,pfname,pmname,psname,sex,age,o.opdid,agetype,c.cname from patient_registration p,opdvisit o,admin_company c where p.regno=o.regno and p.pclass=c.cid and o.regno='{}' order by vdate desc limit 1".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getAllSubXrayName():
    try:
        sql="select subid,subxray from admin_subname where deletestatus='{0}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def getAllPhyName():
    try:
        sql="select phyid,phyname from admin_physiotherapy where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getAllTestName():
    try:
        sql="select id,test_name from admin_addtest where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getAllDressingName():
    try:
        sql="select drsid,drsname from admin_dressing where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

########################For Amount#####################################
def getsubXrayAmount(invid):
    try:
        sql="select amount from admin_subname where subid='{}'".format(invid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getphyAmount(invid):

    try:
        sql="select phyamount from admin_physiotherapy where phyid='{}'".format(invid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def getLabTestAmount(invid):

    try:
        sql="select amount from admin_addtest where id='{}'".format(invid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getDressingAmount(invid):

    try:
        sql="select drsamount from admin_dressing where drsid='{}'".format(invid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)



def insertopdbillingmain():

    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdbillingmain"
    regno=request.form['regno']
    opdid=request.form['opdid']
    try:
        if request.method == 'POST':
            dbcolumn.append('regno')
            dbcolumn.append('opdid')
            dbcolumn.append('date')
            dbcolumn.append('payment_status')
            dbcolumn.append('totalamount')
            dbcolumn.append('recievedby')



            htmlcolumn.append(regno)
            htmlcolumn.append(opdid)
            htmlcolumn.append(request.form['date'])
            htmlcolumn.append(request.form['payment_status'])
            htmlcolumn.append(request.form['totalamount'])
            htmlcolumn.append(request.form['recievedby'])




            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            if result==1:
                sql="select opmid from opdbillingmain order by opmid desc limit 1;"
                cursor.execute(sql)
                opmid=cursor.fetchall()
                result1=insertopdbillingdetail(opmid[0][0])
                print("i am none",result1)
            return result1
    except Exception as e:
        return str(e)

def insertopdbillingdetail(opmid):
    result=''
    tablename = "opdbillingdetail"
    row=len(request.form.getlist('invtype'))

    invtype = request.form.getlist('invtype') #Has Multiple Value
    invname = request.form.getlist('invname') #Has Multiple Value
    amnt = request.form.getlist('amnt') #Has Multiple Value




    try:
        if request.method == 'POST':

            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('opmid')
                dbcolumn.append('invtype')
                dbcolumn.append('invname')
                dbcolumn.append('amnt')

                htmlcolumn.append(str(opmid))
                htmlcolumn.append(invtype[i])
                htmlcolumn.append(invname[i])
                htmlcolumn.append(amnt[i])







                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result

    except Exception as e:
        return str(e)




def getopmidMain():
    try:
        sql="select opmid from opdbillingmain order by opmid desc limit 1"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)



def getOpdPrintMain():
    opmid=request.form['opmid']

    try:
        sql="select om.opmid,om.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,p.agetype,c.cname,o.opdid,om.date,om.payment_status,om.totalamount,om.recievedby from patient_registration p,opdbillingmain om,opdvisit o,admin_company c where o.opdid=om.opdid and om.regno=p.regno and p.pclass=c.cid and om.opmid='{}' order by om.date desc".format(opmid)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getOpdPrintDetails():
    opmid=request.form['opmid']

    try:
        sql="select om.opmid,ob.bdid,ob.invtype,ob.invname,ob.amnt from opdbillingmain om,opdbillingdetail ob where om.opmid=ob.opmid and om.opmid='{}'".format(opmid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

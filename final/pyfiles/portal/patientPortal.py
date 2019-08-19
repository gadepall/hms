from flask import request,url_for,json,jsonify
from mysql.connector import Error
from werkzeug import secure_filename
import os,sys
import db_conf as con
import insertdata as ins
import updatedata as up
import datetime

#DB object for hospital databse
db = con.db
cursor=db.cursor()

def getPatient_DataForPortal(regno):
    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,p.sex,ag.gsname  from patient_registration p,ipdvisit i,admin_govsch ag,ward_main w where p.regno=i.regno and i.govscheme=ag.gsid  and w.ipdid=i.ipdid and w.wardstatus=1 and i.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPatient_DischargeInfo(regno):
    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,i.ipddate,i.dischargedate from patient_registration p,ipdvisit i,admin_govsch ag,ward_main w where p.regno=i.regno and i.govscheme=ag.gsid  and w.ipdid=i.ipdid and w.wardstatus=0 and i.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getWardMainId(regno):
    try:
        sql="Select w.wrd_id,w.ipdid from ipdvisit i,ward_main w where i.ipdid=w.ipdid and w.wardstatus='1' and w.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getOpdVisits(regno):
    try:
        sql="select vdate,complaint,status from opdvisit where regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getIpdVisits(regno):
    try:
        sql="select ipddate,complaint,aw.wname,ab.bname from ipdvisit i,ward_main w,admin_wardname aw,admin_ward_bdname ab where w.ipdid=i.ipdid and w.wid=aw.wid and w.bedno=ab.bid and  i.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getXraysData(wmid):
    try:
        sql="select x.xdate,ax.xrayname,asx.subxray,x.upload from xray x,admin_xname ax,admin_subname asx,ward_main w where x.xtype=ax.xid and x.stype=asx.subid and w.wrd_id=x.pid and w.wardstatus=1 and x.location<>'OPD' and pid='{}'".format(wmid)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getDocsData(regno):
    try:
        sql="select doc_date,doc_name,doc_from,doc_file_loc from opdDocument where regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

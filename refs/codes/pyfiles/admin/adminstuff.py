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

###############################################################################
############################DISTRICT STARTS####################################
###############################################################################

def getAllDistrict():
    try:
        sql="select * from admin_district where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewDistrict():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_district'
        dbcolumn.append('disname')
        htmlcolumn.append(request.form['district'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateDistrict():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_district'
        dbcolumn.append('disname')
        dbcolumn.append('did')
        htmlcolumn.append(request.form['district'])
        htmlcolumn.append(request.form['did'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


###############################################################################
############################DISTRICT ENDS######################################
###############################################################################

#======================================================================================


###############################################################################
############################COMPANY STARTS####################################
###############################################################################

def getAllCompany():
    try:
        sql="select * from admin_company where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewCompany():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_company'
        dbcolumn.append('cname')
        htmlcolumn.append(request.form['cname'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateCompany():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_company'
        dbcolumn.append('cname')
        dbcolumn.append('cid')
        htmlcolumn.append(request.form['cname'])
        htmlcolumn.append(request.form['cid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


###############################################################################
############################COMPANY ENDS######################################
###############################################################################

#======================================================================================


###############################################################################
############################DRESSING STARTS####################################
###############################################################################
def getAllDressing():
    try:
        sql="select * from admin_dressing where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewDressingData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_dressing'
        dbcolumn.append('drsname')
        dbcolumn.append('drsamount')
        htmlcolumn.append(request.form['drsname'])
        htmlcolumn.append(request.form['drsamount'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateDressingData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_dressing'
        dbcolumn.append('drsname')
        dbcolumn.append('drsamount')
        dbcolumn.append('drsid')
        htmlcolumn.append(request.form['drsname'])
        htmlcolumn.append(request.form['drsamount'])
        htmlcolumn.append(request.form['drsid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)
###############################################################################
############################DRESSING ENDS######################################
###############################################################################

#======================================================================================

###############################################################################
############################PHYSIOTHERAPY STARTS###############################
###############################################################################
def getAllPhy():
    try:
        sql="select * from admin_physiotherapy where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewPhyData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_physiotherapy'
        dbcolumn.append('phyname')
        dbcolumn.append('phyamount')
        htmlcolumn.append(request.form['phyname'])
        htmlcolumn.append(request.form['phyamount'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdatePhyData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_physiotherapy'
        dbcolumn.append('phyname')
        dbcolumn.append('phyamount')
        dbcolumn.append('phyid')
        htmlcolumn.append(request.form['phyname'])
        htmlcolumn.append(request.form['phyamount'])
        htmlcolumn.append(request.form['phyid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)
###############################################################################
############################PHYSIOTHERAPY ENDS#################################
###############################################################################

###############################################################################
############################THERAPY STARTS####################################
###############################################################################
def getAllTherapy():
    try:
        sql="select adm_therapyid,adm_therapyname,adm_therapyamount*60,deletestatus from admin_therapy where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewTherapyData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_therapy'
        dbcolumn.append('adm_therapyname')
        dbcolumn.append('adm_therapyamount')
        htmlcolumn.append(request.form['adm_therapyname'])
        htmlcolumn.append(request.form['adm_therapyamount'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateTherapyData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_therapy'
        dbcolumn.append('adm_therapyname')
        dbcolumn.append('adm_therapyamount')
        dbcolumn.append('adm_therapyid')
        htmlcolumn.append(request.form['adm_therapyname'])
        htmlcolumn.append(request.form['adm_therapyamount'])
        htmlcolumn.append(request.form['adm_therapyid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)
###############################################################################
############################THERAPY ENDS######################################
###############################################################################



#======================================================================================



###############################################################################
############################DIAGNOSIS STARTS###################################
###############################################################################

def getAllDiagnosis():
    try:
        sql="select * from admin_diagno where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewDiagnosisData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_diagno'
        dbcolumn.append('diagnosis')
        htmlcolumn.append(request.form['diagnosis'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateDiagnosisData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_diagno'
        dbcolumn.append('diagnosis')
        dbcolumn.append('did')
        htmlcolumn.append(request.form['diagnosis'])
        htmlcolumn.append(request.form['did'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


###############################################################################
############################DIAGNOSIS ENDS#####################################
###############################################################################

#======================================================================================

###############################################################################
############################DEATH REASON STARTS################################
###############################################################################

def getAllDeathReason():
    try:
        sql="select * from admin_deathreason where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewDeathReasonData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_deathreason'
        dbcolumn.append('deathreason')
        htmlcolumn.append(request.form['deathreason'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateDeathReasonData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_deathreason'
        dbcolumn.append('deathreason')
        dbcolumn.append('deathid')
        htmlcolumn.append(request.form['deathreason'])
        htmlcolumn.append(request.form['deathid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


###############################################################################
############################DEATH REASON ENDS##################################
###############################################################################

#======================================================================================


###############################################################################
############################DEATH REASON STARTS################################
###############################################################################

def getAllGovScheme():
    try:
        sql="select * from admin_govsch where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def InsertNewGovSchemeData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_govsch'
        dbcolumn.append('gsname')
        htmlcolumn.append(request.form['gsname'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def UpdateGovSchemeData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_govsch'
        dbcolumn.append('gsname')
        dbcolumn.append('gsid')
        htmlcolumn.append(request.form['gsname'])
        htmlcolumn.append(request.form['gsid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def DeactivateGovSchemeData():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_govsch'
        dbcolumn.append('deletestatus')
        dbcolumn.append('gsid')
        htmlcolumn.append("1")
        htmlcolumn.append(request.form['gsid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


###############################################################################
############################DEATH REASON ENDS##################################
###############################################################################

#===============================Admin Xray Starts From HERE=========================================

def getAllXray():
    try:
        sql="select * from admin_xname where deletestatus=0"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getAllSubXray():
    try:
        sql="select * from admin_subname where deletestatus=0 order by subxray desc;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


###############################################################################
############################GENERAL MESSAGE STARTS####################################
###############################################################################

def InsertNewGeneralMsg():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_generalmsg'
        dbcolumn.append('genmsg')
        htmlcolumn.append(request.form['genmsg'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def getAllGenMsg():
    try:
        sql="select * from admin_generalmsg"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def UpdateGeneralMsg():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_generalmsg'
        dbcolumn.append('genmsg')
        dbcolumn.append('genid')
        htmlcolumn.append(request.form['genmsg'])
        htmlcolumn.append(request.form['genid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)



#======================================================================================
###############################################################################
############################DELIVERY MESSAGE STARTS####################################
###############################################################################

def InsertNewDeliveryMsg():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_delmsg'
        dbcolumn.append('delmsg')
        htmlcolumn.append(request.form['delmsg'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


def getAllDeliveryMsg():
    try:
        sql="select * from admin_delmsg"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def UpdateDeliveryMsg():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_delmsg'
        dbcolumn.append('delmsg')
        dbcolumn.append('delid')
        htmlcolumn.append(request.form['delmsg'])
        htmlcolumn.append(request.form['delid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

###########################################################################################
def getRandomGeneralMsg():
    try:
        sql="select genmsg from admin_generalmsg order by RAND() limit 1;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def getRandomDeliveryMsg():
    try:
        sql="select delmsg from admin_delmsg order by RAND() limit 1;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

###############################################################################
############################DELIVERY MESSAGE ENDS HERE####################################
###############################################################################

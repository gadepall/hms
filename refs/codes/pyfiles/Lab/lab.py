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
from xlsxwriter.workbook import Workbook



#This function will insert a new record in table "patient_registration" for new patient.
def newTest():
    #regno = request.form['regno']
    #pclass= request.form['pclass']
    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_addtest"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('sid')
            dbcolumn.append('pid')
            dbcolumn.append('test_name')
            dbcolumn.append('Male_Range_min')
            dbcolumn.append('Male_Range_max')
            dbcolumn.append('Female_Range_min')
            dbcolumn.append('Female_Range_max')
            dbcolumn.append('Unit')
            dbcolumn.append('amount')

            htmlcolumn.append(request.form['sample'])
            htmlcolumn.append(request.form['panel'])
            htmlcolumn.append(request.form['test_name'])
            htmlcolumn.append(request.form['Male_Range_min'])
            htmlcolumn.append(request.form['Male_Range_max'])
            htmlcolumn.append(request.form['Female_Range_min'])
            htmlcolumn.append(request.form['Female_Range_max'])
            htmlcolumn.append(request.form['Unit'])
            htmlcolumn.append(request.form['amount'])
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def newSample():
    #regno = request.form['regno']
    #pclass= request.form['pclass']
    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_addsample"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('sample_name')
            htmlcolumn.append(request.form['sample_name'])
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def newPanel():
    #regno = request.form['regno']
    #pclass= request.form['pclass']
    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_addpanel"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('sid')
            dbcolumn.append('panel_name')
            htmlcolumn.append(request.form['panel'])
            htmlcolumn.append(request.form['panel_name'])
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)



##------------TEST-------------------

def get_all_tests():
    sql = "select * from admin_addtest where deletestatus=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_all_testsBySampleId(sid):
    sql = "select id,test_name from admin_addtest where sid = '{}' and deletestatus=0".format(sid)
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_test_from_id_Nopanel(tid):
    sql="select t.*,s.sample_name,'' from admin_addtest t,admin_addsample s where s.id=t.sid and t.sid='1' and t.pid =0 and t.deletestatus=0"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1

def get_test_from_id(tid):
    sql="select t.*,s.sample_name,p.panel_name from admin_addtest t,admin_addsample s,admin_addpanel p  where s.id=t.sid and p.id=t.pid and t.id="+str(tid)+" and t.deletestatus=0"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1


def get_test_by_samid(sid):
    sql="select t.*,s.sample_name from admin_addtest t,admin_addsample s  where s.id=t.sid  and t.sid='{}' and t.pid=0 and t.deletestatus=0".format(sid)
    print(sql)
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1

def get_test_by_samid_pid(sid,pid):
    sql="select t.*,s.sample_name,p.panel_name from admin_addtest t,admin_addsample s,admin_addpanel p  where s.id=t.sid and p.id=t.pid and t.sid='{}' and t.pid='{}' and t.deletestatus=0".format(sid,pid)
    print(sql)
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1

def get_all_tests_with_panel_sample():
    sql = "select t.*,s.sample_name,p.panel_name from admin_addtest t,admin_addsample s,admin_addpanel p where s.id=t.sid and p.id=t.pid and t.deletestatus=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


##------------TEST-------------------

##------------PANEL-------------------

def get_all_panels():
    sql = "select p.*,s.sample_name from admin_addpanel p,admin_addsample s where s.id=p.sid and p.deletestatus=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_panel_from_id(pid):
    sql="select p.*,s.sample_name from admin_addpanel p,admin_addsample s where p.id = "+str(pid)+" and s.id=p.sid and p.deletestatus=0"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1

def get_panel_from_id_forSample(sid):
    sql="select p.*,s.sample_name from admin_addpanel p,admin_addsample s where p.sid = "+str(sid)+" and s.id=p.sid and p.deletestatus=0"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1

##------------PANEL-------------------

##------------SAMPLE-------------------
def get_all_samples():
    sql = "select * from admin_addsample where deletestatus=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_all_panels_with_sample():
    sql = "select p.*,s.sample_name from admin_addpanel p,admin_addsample s where s.id=p.sid and p.deletestatus=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_sample_from_id(sid):
    sql="select * from admin_addsample where id = "+str(sid)+" and deletestatus=0"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return data1







def updateSample():
    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_addsample"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('sample_name') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"
            dbcolumn.append('id')
            htmlcolumn.append(request.form['samplename'])
            htmlcolumn.append(request.form['sid'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def updatePanel():
    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_addpanel"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('panel_name') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"
            dbcolumn.append('sid')
            dbcolumn.append('id')
            htmlcolumn.append(request.form['panel_name'])
            htmlcolumn.append(request.form['sample_id'])
            htmlcolumn.append(request.form['panel_id'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def updateTest():
    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_addtest"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('sid')
            dbcolumn.append('pid')
            dbcolumn.append('test_name')
            dbcolumn.append('Male_Range_min')
            dbcolumn.append('Male_Range_max')
            dbcolumn.append('Female_Range_min')
            dbcolumn.append('Female_Range_max')
            dbcolumn.append('Unit')
            dbcolumn.append('amount')
            dbcolumn.append('id')

            htmlcolumn.append(request.form['sample'])
            htmlcolumn.append(request.form['panel'])
            htmlcolumn.append(request.form['test_name'])
            htmlcolumn.append(request.form['Male_Range_min'])
            htmlcolumn.append(request.form['Male_Range_max'])
            htmlcolumn.append(request.form['Female_Range_min'])
            htmlcolumn.append(request.form['Female_Range_max'])
            htmlcolumn.append(request.form['Unit'])
            htmlcolumn.append(request.form['amount'])
            htmlcolumn.append(request.form['test_id'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)




def getSampleDetails_1(sampleid):
    sql="select p.id,p.panel_name,p.sid from admin_addpanel p,admin_addsample s where p.sid = s.id and p.sid='{}'".format(sampleid)
    cursor.execute(sql)
    panel=cursor.fetchall()
    print(panel)
    return panel

def getSampleDetails_2(sampleid):
    sql="select t.id,t.test_name from admin_addtest t,admin_addsample s where s.id=t.sid and t.sid='{}'".format(sampleid)
    cursor.execute(sql)
    test=cursor.fetchall()
    return test

def getPanelTest_1(panelid):
    sql="select t.id from admin_addtest t,admin_addpanel p where p.id=t.sid and t.pid='{}'".format(panelid)
    cursor.execute(sql)
    paneltest=cursor.fetchall()
    return paneltest

def getpanel_1(sname):
    sql = "select * from admin_addpanel where sid = '{}'".format(sname)
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def getOpdPatientdata(regno):
	try:
                sql="select p.regno,pfname,pmname,psname,sex,age,o.opdid,'OPD' from patient_registration p,opdvisit o where o.regno=p.regno and  o.regno='{}' order by vdate desc limit 1".format(regno)
                cursor.execute(sql)
                return cursor.fetchall()
	except Exception as e:
                return str(e)

def getWardPatientdata(regno):
    try:
        sql="select p.regno,pfname,pmname,psname,sex,age,i.ipdid,wa.wname from patient_registration p,ipdvisit i,ward_main w,admin_wardname wa where i.regno=p.regno and w.ipdid = i.ipdid and w.wid=wa.wid and wardstatus=1 and w.regno='{}' order by i.ipddate desc limit 1".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def new_sample_collect():
    dbcolumn = []
    htmlcolumn = []
    tablename = "lab_sample_collect"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('regno')
            dbcolumn.append('source_id')
            dbcolumn.append('date')
            dbcolumn.append('source')
            dbcolumn.append('test_validation')

            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append((request.form['source_id']))
            htmlcolumn.append(request.form['tdate'])
            htmlcolumn.append(request.form['source'])
            htmlcolumn.append('0')

            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getTadayLabPatient():
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.source from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and test_validation=0 and ls.date=curdate()"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTadayTest():
    try:
        sql = "select ls.accession_no,t.test_name from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id and test_validation=0 and ls.date=curdate()"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def save_test_data(a):
        sql = "SELECT accession_no FROM lab_sample_collect ORDER BY accession_no DESC LIMIT 1"
        cursor.execute(sql)
        data = cursor.fetchall()

        dbcolumn = []
        htmlcolumn = []
        tablename = "lab_test_data"
        result=''
        try:
                for i in a:
                        dbcolumn.append('accession_no')
                        dbcolumn.append('tid')
                        #dbcolumn.append('test_value')

                        htmlcolumn.append(str(data[0][0]))
                        htmlcolumn.append(str(i))
                        #htmlcolumn.append(' ')
                        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                        dbcolumn = []
                        htmlcolumn = []
                return result
        except Exception as e:
                return str(e)


def getTadayLabValidationPatient():
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.validation_date,ls.source from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and test_validation=1 and ls.validation_date=curdate()"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTadayValidationTest():
    try:
        sql = "select ls.accession_no,t.test_name,lt.test_value from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id and test_validation=1 and ls.validation_date=curdate()"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getLabNotValidationPatient():
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.validation_date,ls.source from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and test_validation=0"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getNotValidationTest():
    try:
        sql = "select ls.accession_no,t.test_name,lt.test_value from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id and test_validation=0"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def validateSamplePatientDetails(accession_no):
    sqll="select p.regno,p.pfname,p.pmname,p.psname,p.age,p.sex,l.date,l.source,l.source_id,l.validation_date from lab_sample_collect l, patient_registration p where l.regno = p.regno  and accession_no ='{}'".format(accession_no)
    cursor.execute(sqll)
    return cursor.fetchall()

def validateSampleTestDetails(accession_no):
    sql = "select s.sample_name,t.test_name,t.Unit,t.Male_Range_min,t.Male_Range_max,t.Female_Range_min,t.Female_Range_max,lt.ltid,lt.test_value,lt.tid,lt.accession_no from admin_addsample s, admin_addtest t,lab_sample_collect l,lab_test_data lt where  s.id = t.sid and lt.tid = t.id and l.accession_no = lt.accession_no and lt.accession_no = '{}' order by s.sample_name desc".format(accession_no)
    cursor.execute(sql)
    return cursor.fetchall()

def update_testvalues(listt1,listt2):
    tablename = "lab_test_data"
    result=''
    try:
        for i in range(len(listt1)):
                dbcolumn = []
                htmlcolumn = []
                dbcolumn.append('test_value') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"
                dbcolumn.append('ltid')
                htmlcolumn.append(str(listt1[i]))
                htmlcolumn.append(str(listt2[i]))
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                print(result)
        if result ==1:
            dbcolumn = []
            htmlcolumn = []
            dbcolumn.append('test_validation')
            dbcolumn.append('validation_date')
            dbcolumn.append('accession_no')
            htmlcolumn.append("1")
            htmlcolumn.append(request.form['valdate'])
            htmlcolumn.append(str(request.form['accno']))
            result = up.UpdateData(dbcolumn,htmlcolumn,"lab_sample_collect")
            return result
    except Exception as e:
        return str(e)



def getLabPatientByAcno(acno,val):
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.source,ls.validation_date from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and ls.test_validation='{}' and ls.accession_no='{}'".format(val,acno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTestByAcno(acno):
    try:
        sql = "select ls.accession_no,t.test_name,lt.test_value from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id and lt.accession_no='{}'".format(acno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getLabPatientByRegno(regno,val):
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.source,ls.validation_date from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and ls.test_validation='{}' and ls.regno='{}'".format(val,regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTestByRegno(acno):
    try:
        sql = "select ls.accession_no,t.test_name,lt.test_value from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id and lt.accession_no='{}'".format(acno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getLabPatientByDate(fdate,tdate):
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.source,ls.validation_date from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and ls.test_validation=0 and ls.date BETWEEN  '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getTestByDate(acno,fdate,tdate):
    try:
        sql = "select ls.accession_no,t.test_name,lt.test_value from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id  and ls.date BETWEEN  '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getValidateLabPatientByDate(fdate,tdate):
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,ls.date,ls.source,ls.validation_date from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and ls.test_validation=1 and ls.validation_date BETWEEN  '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getValidateTestByDate(acno,fdate,tdate):
    try:
        sql = "select ls.accession_no,t.test_name,lt.test_value from lab_sample_collect ls,lab_test_data lt,admin_addtest t where  ls.accession_no = lt.accession_no and lt.tid=t.id  and ls.validation_date BETWEEN  '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def get_all_tests_with_panel_sampleByAcc(acno):
    try:
        sql = "select s.id,s.sample_name,t.id,t.test_name,lt.ltid from admin_addsample s,admin_addtest t,lab_test_data lt where s.id=t.sid and t.id = lt.tid and lt.accession_no='{}'".format(acno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getLabPatientForPrint(acno):
    try:
        sql = "select ls.accession_no,ls.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,p.rmname,p.rsname,p.age,p.agetype,p.sex,ls.date from patient_registration p, lab_sample_collect ls where ls.regno=p.regno and ls.test_validation=1 and ls.accession_no='{}'".format(acno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTestForPrint(acno):
    try:
        sql = "select ls.accession_no,s.sample_name,t.test_name,lt.test_value,t.Unit,cast(t.Male_Range_min AS DECIMAL(10,2)),cast(t.Male_Range_max AS DECIMAL(10,2)),cast(t.Female_Range_min AS DECIMAL(10,2)),cast(t.Female_Range_max AS DECIMAL(10,2)),lt.test_value REGEXP '^-?[0.0-9.0]+$' from lab_sample_collect ls,lab_test_data lt,admin_addtest t,admin_addsample s where ls.accession_no = lt.accession_no and lt.tid=t.id and s.id=t.sid and lt.accession_no='{}' order by s.sample_name ASC".format(acno)
        cursor.execute(sql)
        valu = cursor.fetchall()
        return valu
    except Exception as e:
        return str(e)

def updateTestSampleCollect():
    tablename = "lab_test_data"
    result=''
    count =len(request.form.getlist('ltid'))
    ltid =request.form.getlist('ltid')
    tid =request.form.getlist('testname')
    try:
        for i in range(count):
            dbcolumn = []
            htmlcolumn = []
            dbcolumn.append('tid')
            dbcolumn.append('ltid') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(str(tid[i]))
            htmlcolumn.append(str(ltid[i]))
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#======================Update By Sanjay=========For Report#
def getAllTestBySample(sname):
    try:
        sql="select t.id,test_name from admin_addtest t,admin_addsample s where s.id=t.sid and t.sid='{}' and t.deletestatus=0".format(sname)
        print("i zm",sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAllTestDataAck(fdate,tdate,testname,labExcel):
    labExcel=labExcel+"labExcel.xlsx"

    try:
        sql="select ls.regno,p.pfname,p.pmname,psname,p.sex,p.age,p.agetype,DATE_FORMAT(ls.date,'%d/%m/%Y'),s.sample_name,at.test_name,DATE_FORMAT(ls.validation_date,'%d/%m/%Y'),lt.test_value,ls.source from patient_registration p,lab_sample_collect ls,admin_addtest at,admin_addsample s,lab_test_data lt where lt.tid=at.id and ls.accession_no=lt.accession_no and s.id=at.sid and p.regno=ls.regno and test_validation=1 and ls.validation_date between '{}' and '{}' and at.id='{}'".format(fdate,tdate,testname)
        print(sql)
        cursor.execute(sql)
        q=cursor.fetchall()

        workbook = Workbook(labExcel)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'green'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"SURNAME",cell_format)
        sheet.write(0,4,"SEX",cell_format)
        sheet.write(0,5,"AGE",cell_format)
        sheet.write(0,6,"AGETYPE",cell_format)
        sheet.write(0,7,"Sample Collect Date",cell_format)
        sheet.write(0,8,"Sample Name",cell_format)
        sheet.write(0,9,"Test Name",cell_format)
        sheet.write(0,10,"Validation Date",cell_format)
        sheet.write(0,11,"Test Result/Value",cell_format)
        sheet.write(0,12,"Patient From",cell_format)

        for r, row in enumerate(q):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return q
    except Exception as e:
        return str(e)

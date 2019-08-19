from flask import request,url_for,json,jsonify
from mysql.connector import Error
from werkzeug import secure_filename
import os,sys
import db_conf as con
import insertdata as ins
import updatedata as up
import datetime
from xlsxwriter.workbook import Workbook


#DB object for hospital databse
db = con.db
cursor=db.cursor()


def getAllPatientVisitData(opdid):
    try:
        if request.method == 'POST':
            sql="select *,TIME_FORMAT(vtime,'%H:%i') from opdvisit where opdid='{}'".format(opdid)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("ERROR in getAllPatientVisitData:"+str(e))
        return str(e)

def getPatientVisitData(regno):
        try:
            if request.method == 'POST':
                sql="select v.opdid,v.complaint,v.vdate,v.height,v.weight,v.bmi,v.systolic,v.diastolic,v.pulse,v.temp,v.rrate,v.regno  from patient_registration p,opdvisit v where p.regno=v.regno AND v.regno='{}' order by v.vdate DESC".format(regno)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            return str(e)

#======================OPD SEARCH START ===============

def getopdSearchPatientToday():
    try:
        if request.method == 'POST':
            sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and o.vdate=curdate() order by o.vtime desc"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getopdSearchPatientViewDateData(opd):
    opd=opd+"opd.xlsx"
    fdate = request.form['fdate']
    tdate = request.form['tdate']

    try:
        sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and vdate between '{}' and '{}' order by opdid desc".format(fdate,tdate)
        print("between",sql)
        cursor.execute(sql)
        q=cursor.fetchall()

        workbook = Workbook(opd)
        print("i am workbook=",workbook)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'blue'})
        sheet.write(0,0,"pid",cell_format)
        sheet.write(0,1,"Regno.",cell_format)
        sheet.write(0,2,"FIRST NAME",cell_format)
        sheet.write(0,3,"MIDDLE NAME",cell_format)
        sheet.write(0,4,"LAST NAME",cell_format)
        sheet.write(0,5,"RelativeName",cell_format)
        sheet.write(0,6,"RFirst Name",cell_format)
        sheet.write(0,7,"RMiddle Name",cell_format)
        sheet.write(0,8,"RLast Name",cell_format)
        sheet.write(0,9,"Visit Date",cell_format)
        sheet.write(0,10,"Visit Time",cell_format)
        sheet.write(0,11,"Age",cell_format)
        sheet.write(0,12,"AgeType",cell_format)
        sheet.write(0,13,"Gender",cell_format)
        sheet.write(0,14,"Education",cell_format)
        sheet.write(0,15,"Occupation",cell_format)
        sheet.write(0,16,"Phone Number",cell_format)
        sheet.write(0,17,"Category",cell_format)
        sheet.write(0,18,"Post Office",cell_format)
        sheet.write(0,19,"Tahsil",cell_format)
        sheet.write(0,20,"District",cell_format)
        sheet.write(0,21,"Address",cell_format)
        sheet.write(0,22,"Cast",cell_format)
        sheet.write(0,23,"Aadhar No.",cell_format)
        sheet.write(0,24,"Ration Card",cell_format)
        sheet.write(0,25,"Complaint",cell_format)
        sheet.write(0,26,"Opdid",cell_format)
        sheet.write(0,27,"Visit Date",cell_format)
        sheet.write(0,28,"Height",cell_format)
        sheet.write(0,29,"Weight",cell_format)
        sheet.write(0,30,"BMI",cell_format)
        sheet.write(0,31,"Temp",cell_format)
        sheet.write(0,32,"Pulse",cell_format)
        sheet.write(0,33,"RRate",cell_format)
        sheet.write(0,34,"Systolic",cell_format)
        sheet.write(0,35,"Diastolic",cell_format)

        for r, row in enumerate(q):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return q
    except Exception as e:
        return str(e)



def getopdSearchPatientNameDateData():
    try:
        if request.method == 'POST':
            fdate = request.form['fdate']
            tdate = request.form['tdate']
            pfname = request.form['pfname']
            sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and  vdate between '{}' and '{}' and p.pfname LIKE '%{}%'".format(fdate,tdate,pfname)
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print("ERROR in getPatientNameDateData:"+str(e))
        return str(e)

def getOpdSearchPatientRegno():
    try:
        if request.method == 'POST':
            regno = request.form['regno']
            sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and o.regno='{}' order by o.vdate desc".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getopdSearchPatientFName():
    try:
        if request.method == 'POST':
            name = request.form['pfname']
            sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and pfname LIKE '%{}%' order by o.vdate desc".format(name)
            print("name",sql)

            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getopdSearchPatientViewContact():
    try:
        if request.method == 'POST':
            contact = request.form['contactno']
            sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and contactno='{}' order by o.vdate desc".format(contact)
            print("number",sql)

            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getopdSearchPatientViewAddressData():
    try:
        if request.method == 'POST':
            address = request.form['address']
            sql="select p.pid,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(o.vdate,'%d/%m/%Y'),TIME_FORMAT(o.vtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,ac.cname,p.post,p.tahsil,d.disname,p.address,p.cast,p.aadharNo,p.rationcard,o.complaint,o.opdid,DATE_FORMAT(o.vdate,'%d/%m/%Y'),o.height,o.weight,o.bmi,o.temp,o.pulse,o.rrate,o.systolic,o.diastolic from patient_registration p,admin_district d,opdvisit o,admin_company ac where p.district=d.did and p.regno=o.regno and p.pclass=ac.cid and address LIKE '%{}%'".format(address)
            print("address",sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

#=================OPD SEARCH END===============


#=====================PrintPage======================#


def getPatientDataPrintVisit():
    try:
        if request.method == 'POST':
            regno = request.form['regno']
            vdate=request.form['vdate']
            sql="select DATE_FORMAT(o.vdate,'%d-%m%-%Y'),p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,p.rmname,p.rsname,p.age,p.agetype,p.sex,p.address,p.education,p.occupation,p.contactno,o.complaint,o.height,o.weight,o.bmi,o.temp,o.pulse,o.systolic,o.diastolic,o.rrate,o.vtime from patient_registration p,opdvisit o where o.regno=p.regno and o.regno='{}' and o.vdate='{}' order by o.vdate desc limit 1".format(regno,vdate)
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        return str(e)


def getPatientDataPrintSearch():
    try:
        if request.method == 'POST':
            opdid = request.form['opdid']
            sql="select o.vdate,p.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,p.rmname,p.rsname,p.age,p.agetype,p.sex,p.address,p.education,p.occupation,p.contactno,o.complaint,o.height,o.weight,o.bmi,o.temp,o.pulse,o.systolic,o.diastolic,o.rrate,o.vtime from patient_registration p,opdvisit o where o.regno=p.regno and opdid='{}' order by o.vdate desc limit 1".format(opdid)
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        return str(e)

#===================#Data View End=================================#



#--------------THIS FUNCTION WILL RETURN TODAY PATIENT VISIT DATA FOR CONSULT------------
def getTodayPatientVisitData(regno,todaydate):
        try:
            if request.method == 'POST':
                sql="select * from opdvisit  where regno='{}' AND vdate='{}'".format(regno,todaydate)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            return str(e)

#-------------THIS FUNCTION WILL RETURN LIST OF DIAGNOSIS ACCORDING TO FILTER VARIABLE-----------------------------
def getDiagnosis():
        dia = request.form['pdiagno']
        record=[]
        print("i am here")
        try:
            if request.method == 'POST':
                sql="select diagnosis,did from admin_diagno  where diagnosis LIKE '{}%'".format(dia)
                cursor.execute(sql)
                result = cursor.fetchall()
                if cursor.rowcount >0:
                    for i in range(0,len(result)):
                        record.append(str(result[i][1])+"# "+result[i][0])
                    return record
                else:
                    return 0
        except Exception as e:
            return str(e)


def getPatientConsultData(regno):
    try:
        if request.method == 'POST':
            sql="select c.conid,o.vdate,o.complaint,c.regno from opdvisit o,opdconsultmain c where o.opdid = c.opdid and c.regno='{}' order by o.vdate DESC".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)



def getOpdConsultHistory(conid):
    try:
        if request.method == 'POST':
            sql="select * from opdClinicalHistory  where conid='{}'".format(conid)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getOpdConsultRefer(conid):
    try:
        if request.method == 'POST':
            sql="select * from opdreferInfo  where conid='{}'".format(conid)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)


def getOpdConsultDiagnosis(conid):
    try:
        if request.method == 'POST':
            sql="select d.did,d.diagnosisId,ad.diagnosis,d.diagnosisType,d.conid from opdDiagnosis d,admin_diagno ad where d.diagnosisId=ad.did and d.conid='{}'".format(conid)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)



def opdConsultDeleteDiagnosis(did):
    try:
        if request.method == 'POST':
            sql="delete from opdDiagnosis where did='{}'".format(did)
            cursor.execute(sql)
            db.commit()
            return "SUCCESSFULLY DELETED."
    except Exception as e:
        return str(e)


def opdConsultUpdateHistory():
    dbcolumn=[]
    htmlcolumn=[]
    result=''
    tablename = "opdClinicalHistory"
    try:
        dbcolumn.append('hiscli')
        dbcolumn.append('hcid')

        htmlcolumn.append(request.form['hiscli'])
        htmlcolumn.append(request.form['hcid'])

        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def opdConsultUpdateRefer():
    dbcolumn=[]
    htmlcolumn=[]
    result=''
    tablename = "opdreferInfo"
    try:
        dbcolumn.append('reason')
        dbcolumn.append('hname')
        dbcolumn.append('referby')
        dbcolumn.append('referto')
        dbcolumn.append('refid')

        htmlcolumn.append(request.form['reason'])
        htmlcolumn.append(request.form['hname'])
        htmlcolumn.append(request.form['referby'])
        htmlcolumn.append(request.form['referto'])
        htmlcolumn.append(request.form['refid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


def opdConsultUpdateDiagnosis():
    result=''
    tablename = "opdDiagnosis"
    rowno=len(request.form.getlist('did'))

    diaid = request.form.getlist('diaid')
    dtype = request.form.getlist('diagnosisType')
    did = request.form.getlist('did')

    try:
        if request.method == 'POST':
            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                dbcolumn.append('diagnosisId')
                dbcolumn.append('diagnosisType')
                dbcolumn.append('did')

                htmlcolumn.append(diaid[i])
                htmlcolumn.append(dtype[i])
                htmlcolumn.append(did[i])
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)



def insertUpdateOpdDiagnosis():
    result=''
    tablename = "opdDiagnosis"
    conid=request.form['conid']
    rowno=len(request.form.getlist('diagnosisIdnew'))
    diaId = request.form.getlist('diagnosisIdnew') #Has Multiple Value
    diaType = request.form.getlist('diagnosisTypenew')  #Has Multiple Value
    try:
        if request.method == 'POST':

            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('conid')
                dbcolumn.append('diagnosisId')
                dbcolumn.append('diagnosisType')


                #Name of html component e.g request.form['nameofcomponenet']
                htmlcolumn.append(conid)
                htmlcolumn.append(diaId[i])
                htmlcolumn.append(diaType[i])

                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)




# ACKNOWLEDGE START




'''
def getCensusAcknowledgeData(fildate):
    try:
        sql="select count(case when p.sex='Male' then p.sex end) as Male,count(case when p.sex='Female' then p.sex end) as Female,count(case when o.ptype='NEW' then o.ptype end) as New,count(case when o.ptype='OLD' then o.ptype end) as Old from patient_registration p,opdvisit o where p.regno=o.regno AND o.vdate='{}'".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
'''

def getPtypeTodayAck(fildate):
    try:
        sql="select count(case when o.ptype='NEW' then o.ptype end) as New,count(case when o.ptype='OLD' then o.ptype end) as Old from opdvisit o where o.vdate='{}'".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getGeneralPtype(fildate):
    try:
        sql="select count(case when o.ptype='NEW' then o.ptype end) as New,count(case when o.ptype='OLD' then o.ptype end) as Old,count(case when o.ptype='NEW' then o.ptype end)*20 + count(case when o.ptype='OLD' then o.ptype end)*10 as totalamount from patient_registration p,opdvisit o where p.regno=o.regno AND p.pclass='-1' AND o.vdate='{}' ".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPcatTodayAck(fildate):
    try:
        sql="select count(case when p.pclass='-1' then p.pclass end) as General,count(case when p.pclass='-2' then p.pclass end) as staff,count(case when p.pclass='-3' then p.pclass end) as CMSS,count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as Company  from patient_registration p,opdvisit o where p.regno=o.regno AND  o.vdate='{}'".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getCompanyDetail(fildate):
    try:
        sql="select c.cname,count(*) from patient_registration p,opdvisit o,admin_company c where p.regno=o.regno AND p.pclass=c.cid  AND pclass<>'-1' AND pclass<>'-2' AND pclass<>'-3' AND o.vdate='{}'  group by pclass".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getPtypeRangeAck(fdate,tdate):
    try:
        sql="select o.vdate,count(case when o.ptype='NEW' then o.ptype end) as New,count(case when o.ptype='OLD' then o.ptype end) as Old,count(case when o.ptype='NEW' then o.ptype end)+count(case when o.ptype='OLD' then o.ptype end) as total  from opdvisit o where o.vdate BETWEEN '{}' AND '{}' group by o.vdate".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getTotalPtypeRangeAck(fdate,tdate):
    try:
        sql="select count(case when o.ptype='NEW' then o.ptype end) as New,count(case when o.ptype='OLD' then o.ptype end) as Old,count(case when o.ptype='NEW' then o.ptype end)+count(case when o.ptype='OLD' then o.ptype end) as total  from opdvisit o where o.vdate BETWEEN '{}' AND '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPcatRangeAck(fdate,tdate):
    try:
        sql="select o.vdate,count(case when p.pclass='-1' then p.pclass end) as General,count(case when p.pclass='-2' then p.pclass end) as staff,count(case when p.pclass='-3' then p.pclass end) as CMSS,count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as Company,count(case when p.pclass='-1' then p.pclass end)+count(case when p.pclass='-2' then p.pclass end)+count(case when p.pclass='-3' then p.pclass end)+count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as total from patient_registration p,opdvisit o where p.regno=o.regno AND  o.vdate BETWEEN '{}' AND '{}' group by o.vdate".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTotalPcatRangeAck(fdate,tdate):
    try:
        sql="select count(case when p.pclass='-1' then p.pclass end) as General,count(case when p.pclass='-2' then p.pclass end) as staff,count(case when p.pclass='-3' then p.pclass end) as CMSS,count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as Company,count(case when p.pclass='-1' then p.pclass end)+count(case when p.pclass='-2' then p.pclass end)+count(case when p.pclass='-3' then p.pclass end)+count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as total from patient_registration p,opdvisit o where p.regno=o.regno AND  o.vdate BETWEEN '{}' AND '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


# ACKNOWLEDGE END



def visitOpdInsert():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdvisit"
    try:
        if request.method == 'POST':
#Name of database Attribute
            dbcolumn.append('regno')
            dbcolumn.append('ptype')
            dbcolumn.append('vdate')
            dbcolumn.append('vtime')
            dbcolumn.append('height')
            dbcolumn.append('weight')
            dbcolumn.append('bmi')
            dbcolumn.append('temp')
            dbcolumn.append('pulse')
            dbcolumn.append('rrate')
            dbcolumn.append('systolic')
            dbcolumn.append('diastolic')
            dbcolumn.append('complaint')

#Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['ptype'])
            htmlcolumn.append(request.form['vdate'])
            htmlcolumn.append(request.form['vtime'])
            htmlcolumn.append(request.form['height'])
            htmlcolumn.append(request.form['weight'])
            htmlcolumn.append(request.form['bmi'])
            htmlcolumn.append(request.form['temp'])
            htmlcolumn.append(request.form['pulse'])
            htmlcolumn.append(request.form['rrate'])
            htmlcolumn.append(request.form['systolic'])
            htmlcolumn.append(request.form['diastolic'])
            htmlcolumn.append(request.form['complaint'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def insertOpdConsultRefer():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdreferInfo"
    try:
        if request.method == 'POST':
            sql ="SELECT conid from opdconsultmain where regno='{}' order by condate DESC LIMIT 1".format(request.form['regno']);
            cursor.execute(sql)
            conid = str(cursor.fetchall()[0][0])

            #Name of database Attribute
            dbcolumn.append('conid')
            dbcolumn.append('reason')
            dbcolumn.append('hname')
            dbcolumn.append('referby')
            dbcolumn.append('referto')


            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(conid)
            htmlcolumn.append(request.form['reason'])
            htmlcolumn.append(request.form['hname'])
            htmlcolumn.append(request.form['referby'])
            htmlcolumn.append(request.form['referto'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def insertOpdConsultHistory():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdconsultmain"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('opdid')
            dbcolumn.append('regno')
            dbcolumn.append('condate')
            dbcolumn.append('docid')



            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['opdid'])
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['consdate'])
            htmlcolumn.append(request.form['docid'])
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            if result == 1:
                dbcolumn=[]
                htmlcolumn=[]
                tablename='opdClinicalHistory'

                sql = "SELECT conid from opdconsultmain where regno='{}' order by condate DESC LIMIT 1".format(request.form['regno'])
                cursor.execute(sql)
                conid = str(cursor.fetchall()[0][0])

                dbcolumn.append('conid')
                dbcolumn.append('hiscli')

                htmlcolumn.append(conid)
                htmlcolumn.append(request.form['hiscli'])
                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                return result
    except Exception as e:
        return str(e)



def insertOpdDiagnosis():
    result=''
    tablename = "opdDiagnosis"
    rowno=len(request.form.getlist('diagnosisId'))
    diaId = request.form.getlist('diagnosisId') #Has Multiple Value
    diaType = request.form.getlist('diagnosisType')  #Has Multiple Value
    try:
        if request.method == 'POST':
            sql ="SELECT conid from opdconsultmain where regno='{}' order by condate DESC LIMIT 1".format(request.form['regno']);
            print("i am diagno sql",sql)
            cursor.execute(sql)
            conid = str(cursor.fetchall()[0][0])

            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('conid')
                dbcolumn.append('diagnosisId')
                dbcolumn.append('diagnosisType')


                #Name of html component e.g request.form['nameofcomponenet']
                htmlcolumn.append(conid)
                htmlcolumn.append(diaId[i])
                htmlcolumn.append(diaType[i])

                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def insertOpdDocUpload(uploadloc):
    result=''
    tablename = "opdDocument"
    rowno=len(request.form.getlist('doc_name'))
    print(rowno)
    regno = request.form['regno']
    docname = request.form.getlist('doc_name') #Has Multiple Value
    docdate = request.form.getlist('doc_date') #Has Multiple Value
    docloc = request.files.getlist('doc_file') #Has Multiple Value

    docfrom = request.form.getlist('doc_from') #Has Multiple Value
    entrydate=request.form['entrydate']
    print(docname,docdate)
    try:
        if request.method == 'POST':
            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('regno')
                dbcolumn.append('doc_name')
                dbcolumn.append('doc_date')
                dbcolumn.append('doc_file_loc')
                dbcolumn.append('doc_from')
                dbcolumn.append('entry_date')

                #Name of html component e.g request.form['nameofcomponenet']
                htmlcolumn.append(regno)
                htmlcolumn.append(docname[i])
                htmlcolumn.append(docdate[i])

                fname,fileext = os.path.splitext(docloc[i].filename)
                filename=secure_filename(regno+'_'+'{0:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'_'+fname+fileext)
                dst_path=os.path.join(uploadloc, filename)
                docloc[i].save(dst_path)

                htmlcolumn.append(filename)
                htmlcolumn.append(docfrom[i])
                htmlcolumn.append(entrydate)
                #print(request.form['opdid'],diaId[i],diaType[i],request.form['diagnosisDate'])
                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#UPDATE PATIENT VISIT DATA
def opdVisitUpdate():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdvisit"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('vdate')
            dbcolumn.append('vtime')
            dbcolumn.append('height')
            dbcolumn.append('weight')
            dbcolumn.append('bmi')
            dbcolumn.append('temp')
            dbcolumn.append('pulse')
            dbcolumn.append('rrate')
            dbcolumn.append('systolic')
            dbcolumn.append('diastolic')
            dbcolumn.append('complaint')
            dbcolumn.append('opdid')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            #Name of html component e.g request.form['nameofcomponenet']

            htmlcolumn.append(request.form['vdate'])
            htmlcolumn.append(request.form['vtime'])
            htmlcolumn.append(request.form['height'])
            htmlcolumn.append(request.form['weight'])
            htmlcolumn.append(request.form['bmi'])
            htmlcolumn.append(request.form['temp'])
            htmlcolumn.append(request.form['pulse'])
            htmlcolumn.append(request.form['rrate'])
            htmlcolumn.append(request.form['systolic'])
            htmlcolumn.append(request.form['diastolic'])
            htmlcolumn.append(request.form['complaint'])
            htmlcolumn.append(request.form['opdid'])  # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


######################################################################################################
def getallcomplaint():
        complaint = request.form['complaint']
        record=[]
        print("i am here")
        try:
            if request.method == 'POST':
                sql="select complaint from opdvisit where complaint LIKE '{}%'".format(complaint)
                #print("i am query",sql)
                cursor.execute(sql)
                result = cursor.fetchall()
                #print("i am rs1",result)
                if cursor.rowcount >0:
                    for i in range(0,len(result)):
                        record.append(str(result[i][0]))
                    return record
                    #print("i am record",record)
                else:
                    return 0
        except Exception as e:
            return str(e)

from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys
import db_conf as con
import datetime as dt,time as tm
import insertdata as ins
import updatedata as up
from xlsxwriter.workbook import Workbook


db = con.db
cursor=db.cursor()
now = dt.datetime.now()
dtd = now.strftime('%Y')


def getAvalableWardData():
    try:
        sql="select aw.*,count(aw.wid) from admin_wardname aw,admin_ward_bdname ab where aw.wid=ab.wid and ab.bstatus=1 and  aw.deletestatus=0 and ab.deletestatus=0 group by ab.wid order by count(aw.wid) desc"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getAllWardData():
    try:
        sql="select * from admin_wardname where deletestatus='{0}' Order by wname ASC"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def insertWardData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_wardname"
    try:
        if request.method == 'POST':
            dbcolumn.append('wname')
            htmlcolumn.append(request.form['wname'])
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def editWardData():
    try:
        sql="select * from admin_wardname where wid='{}'".format(request.args['wid'])
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def updateWardData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_wardname"
    try:
        if request.method == 'POST':
            dbcolumn.append('wname')
            dbcolumn.append('wid')

            htmlcolumn.append(request.form['wname'])
            htmlcolumn.append(request.form['wid'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getWardBeds(wid):
    try:
        sql="select bname,bid from admin_ward_bdname where deletestatus=0 AND wid='{}'".format(wid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getBeds(wid):
    try:
        sql="select bname,bid,bstatus from admin_ward_bdname where bstatus=1 and deletestatus=0 AND wid='{}' order by bname ASC".format(wid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def insertWardBed():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_ward_bdname"
    try:
        if request.method == 'POST':
            dbcolumn.append('bname')
            dbcolumn.append('wid')

            htmlcolumn.append(request.form['bname'])
            htmlcolumn.append(request.form['wid'])
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getWardBedNo(wid):
    try:
        sql="select bname,bid from admin_ward_bdname where deletestatus=0 AND bid='{}'".format(wid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def updateWardBedData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_ward_bdname"
    try:
        if request.method == 'POST':
            dbcolumn.append('bname')
            dbcolumn.append('bid')

            htmlcolumn.append(request.form['bname'])
            htmlcolumn.append(request.form['bid'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def updateBedStatus(bedno):
    print("BNO",bedno)
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_ward_bdname"
    try:
        dbcolumn.append('bstatus')
        dbcolumn.append('bid')

        htmlcolumn.append(str(0))
        htmlcolumn.append(bedno)
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)

        return result
    except Exception as e:
        return str(e)

def getPatientDetails(regno,wid):
    try:
        sql="select *, ipdid from patient_registration p, ipdvisit i where p.regno=i.regno AND i.regno='{}' and i.wardid='{}' order by ipdid DESC limit 1 ".format(regno,wid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getpatientWardStatus(regno):
    try:
        sql="select wname from ward_main w,admin_wardname aw where w.wid=aw.wid and  wardstatus='1' and regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def insertWardMainData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_main"
    try:
        if request.method == 'POST':
            dbcolumn.append('ipdid')
            dbcolumn.append('regno')
            dbcolumn.append('wid')
            dbcolumn.append('bedno')


            htmlcolumn.append(request.form['ipdid'])
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['wid'])
            htmlcolumn.append(request.form['bedno'])

            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def showWardAdmitPatient(wid):
    try:
        sql="select p.pfname,p.pmname,p.psname,p.regno,bd.wid,bd.bname,i.ipddate,w.wrd_id,w.dischargestatus,w.wid,w.bedno from ward_main w,admin_ward_bdname bd,patient_registration p,ipdvisit i where w.bedno=bd.bid and p.regno=i.regno and w.ipdid=i.ipdid and wardstatus=1 and w.wid='{}' order by wrd_id desc".format(wid)
        print("SQL",sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTransferPatientDetails(wrd_id):
    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,p.sex,i.ipddate,wn.wname,bd.bname from patient_registration p, ipdvisit i,admin_wardname wn,admin_ward_bdname bd,ward_main w where w.ipdid=i.ipdid and w.wid=wn.wid and w.bedno=bd.bid and w.regno=p.regno and w.wrd_id={}".format(wrd_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def InsertPatientTransferData():
    try:
        if request.method == 'POST':
            dbcolumn = []
            htmlcolumn = []
            result=''
            tablename = "ward_main"
            dbcolumn.append('wid')
            dbcolumn.append('bedno')
            dbcolumn.append('wrd_id')

            htmlcolumn.append(request.form['wardname'])
            htmlcolumn.append(request.form['beds'])
            htmlcolumn.append(request.form['wrd_id'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            print("I RUN SUCCESSFULLY ward_main")

            if result==1:
                dbcolumn = []
                htmlcolumn = []
                result=''
                tablename = "ward_patient_transfer"

                dbcolumn.append('wrd_id')
                dbcolumn.append('date')
                dbcolumn.append('time')
                dbcolumn.append('from_wid')
                dbcolumn.append('from_bid')
                dbcolumn.append('to_wid')
                dbcolumn.append('to_bid')
                dbcolumn.append('trans_reason')
                dbcolumn.append('transfer_by')
                print(dbcolumn,"roiht")

                htmlcolumn.append(request.form['wrd_id'])
                htmlcolumn.append(request.form['date'])
                htmlcolumn.append(request.form['time'])
                htmlcolumn.append(request.form['wid'])
                htmlcolumn.append(request.form['bid'])
                htmlcolumn.append(request.form['wardname'])
                htmlcolumn.append(request.form['beds'])
                htmlcolumn.append(request.form['treason'])
                htmlcolumn.append(request.form['transferby'])
                print(htmlcolumn,"jaiswar")
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                print("I RUN SUCCESSFULLY ward_patient_transfer")
                if result == 1:
                    dbcolumn = []
                    htmlcolumn = []
                    result=''
                    tablename = "admin_ward_bdname"


                    dbcolumn.append('bstatus')
                    dbcolumn.append('bid')

                    htmlcolumn.append("0")
                    htmlcolumn.append(request.form['beds'])
                    result = up.UpdateData(dbcolumn,htmlcolumn,tablename)

                if result == 1:
                    dbcolumn = []
                    htmlcolumn = []
                    result=''
                    tablename = "admin_ward_bdname"


                    dbcolumn.append('bstatus')
                    dbcolumn.append('bid')

                    htmlcolumn.append("1")
                    htmlcolumn.append(request.form['bid'])
                    result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    print("I RUN SUCCESSFULLY admin_ward_bdname")
                    return result
    except Exception as e:
        print(str(e))
        return str(e)

def getDrugsAvailableInWard(wardnameid,drugtype,drugname):
    try:
        sql="select i.inv_id,mm.drugname,mm.medicine_type,i.batch_no,DATE_FORMAT(i.manufacturing_date, '%d-%m-%Y'),DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),sum(mo.issued_qty),sum(mo.issued_qty),od.ward_id,mm.med_id,od.outw_id,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id='{}' and mm.medicine_type='{}' and mm.drugname LIKE '{}%' group by(i.batch_no)".format(wardnameid,drugtype,drugname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getInvIdFromMedicineDetail(inve_id,toWard):
    try:
        sql="select i.inv_id from inventory_detail i,main_medicine m,outward_detail o,medicine_outward_detail d where d.outw_id=o.outw_id and d.inv_id=i.inv_id and m.med_id=i.med_id and i.inv_id='{}' and o.ward_id='{}'".format(inve_id,toWard)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getSelectedFromWard(wardnameid):
    try:
        sql="select * from admin_wardname where wid!='{}'".format(wardnameid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def OutwardDetailUpdateFromWard():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "outward_detail"
    try:
        if request.method == 'POST':
            dbcolumn.append('ward_id')
            dbcolumn.append('issued_date')
            dbcolumn.append('person_name')
            dbcolumn.append('time')

            htmlcolumn.append(request.form['toWard'])
            htmlcolumn.append(request.form['issued_date'])
            htmlcolumn.append(request.form['recivedby'])
            htmlcolumn.append(request.form['time'])
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            print(result,"I am from outward_detail")
            if result == 1:
                sql = "SELECT LAST_INSERT_ID()";
                cursor.execute(sql)
                owtid = cursor.fetchall()[0][0]
                row=len(request.form.getlist('inve_id')) #Has Multiple Value
                inv_id=request.form.getlist('inve_id') #Has Multiple Value
                print(inv_id,"ssss")
                Iqty = request.form.getlist('issuedqty') #Has Multiple Value
                print(Iqty,"oooooo")
                row1=len(Iqty) #Has Multiple Value
                for i in range(row):
                    dbcolumn = []
                    htmlcolumn = []
                    tablename = "medicine_outward_detail"
                    dbcolumn.append('outw_id')
                    dbcolumn.append('inv_id')
                    dbcolumn.append('issued_qty')
                    dbcolumn.append('fix_issued_qty')
                    htmlcolumn.append(str(owtid))
                    htmlcolumn.append(str(inv_id[i]))
                    htmlcolumn.append(str(Iqty[i]))
                    htmlcolumn.append(str(Iqty[i]))
                    result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                    print(result,"I am from medicine_outward_detail")
                    if result ==1:
                        sql = "SELECT LAST_INSERT_ID()";
                        cursor.execute(sql)
                        meddet_id = cursor.fetchall()[0][0]
                        dbcolumn = []
                        htmlcolumn = []
                        tablename = "ward_medicine_transfer"
                        dbcolumn.append('fromward')
                        dbcolumn.append('trans_by')
                        dbcolumn.append('toward')
                        dbcolumn.append('reciverd_by')
                        dbcolumn.append('trans_date')
                        dbcolumn.append('trans_time')
                        dbcolumn.append('outw_id')
                        dbcolumn.append('meddet_id')

                        htmlcolumn.append(request.form['wardnameid'])
                        htmlcolumn.append(request.form['person_name'])
                        htmlcolumn.append(request.form['toWard'])
                        htmlcolumn.append(request.form['recivedby'])
                        htmlcolumn.append(request.form['issued_date'])
                        htmlcolumn.append(str(request.form['time']))
                        htmlcolumn.append(str(owtid))
                        htmlcolumn.append(str(meddet_id))
                        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                        print(result,"I am from ward_medicine_transfer")
                        if result ==1:
                            remqty=request.form.getlist('remainingqty')
                            meddet_id=request.form.getlist('meddet_id')
                            print("fdfdf",meddet_id)
                            dbcolumn = []
                            htmlcolumn = []
                            tablename = "medicine_outward_detail"
                            dbcolumn.append('issued_qty')
                            dbcolumn.append('meddet_id')

                            htmlcolumn.append(str(remqty[i]))
                            htmlcolumn.append(str(meddet_id[i]))
                            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                            #result=1
        return result
    except Exception as e:
        return str(e)
############################################################################################################################################################################################################################################################################################
#################################################  SURGERY CODES START  ####################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################################################

def insertSurgeryProcedure():

    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_surgery_procedure"
    try:
        if request.method == 'POST':
            dbcolumn.append('sprocedure')
            dbcolumn.append('spamount')

            htmlcolumn.append(request.form['sprocedure'])
            htmlcolumn.append(request.form['spamount'])
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def showSurgeryProcedureList():
    try:
        sql="select * from admin_surgery_procedure order by sprocedure"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def editSprocedure(sid):
    try:
        sql="select * from admin_surgery_procedure where sid='{}'".format(sid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def EditSurgeryName():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "admin_surgery_procedure"
    try:
        if request.method == 'POST':
            dbcolumn.append('sprocedure')
            dbcolumn.append('spamount')
            dbcolumn.append('sid')

            htmlcolumn.append(request.form['sprocedure'])
            htmlcolumn.append(request.form['spamount'])
            htmlcolumn.append(request.form['sid'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getSurgeryPatientDetailsOpd(regno):
    try:
        sql="select p.*,o.vdate,o.opdid,o.complaint from patient_registration p, opdvisit o where p.regno=o.regno and p.regno='{}' order by vdate desc limit 1".format(regno)
        cursor.execute(sql)
        print(sql,"o")
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getSurgeryPatientDetailsIpd(regno):
    try:
        sql="select p.*,i.ipddate,w.wrd_id,i.complaint from patient_registration p, ipdvisit i,ward_main w where p.regno=i.regno and i.ipdid=w.ipdid and  p.regno='{}' order by ipddate desc limit 1".format(regno)
        cursor.execute(sql)
        print(sql,"o")
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def insertSurgeryDetails():

    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "surgery_details"
    try:
        if request.method == 'POST':
            dbcolumn.append('regno')
            dbcolumn.append('sdate')
            dbcolumn.append('stime')
            dbcolumn.append('surgeon')
            dbcolumn.append('anesthesiologist')
            dbcolumn.append('ksurgerytype')
            dbcolumn.append('stype')
            dbcolumn.append('anstype')
            dbcolumn.append('psurgery')
            dbcolumn.append('spamount')
            dbcolumn.append('disease')
            dbcolumn.append('pfrom')
            dbcolumn.append('wrd_id')

            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['sdate'])
            htmlcolumn.append(request.form['stime'])
            htmlcolumn.append(request.form['surgeon'])
            htmlcolumn.append(request.form['anesthesiologist'])
            htmlcolumn.append(request.form['ksurgerytype'])
            htmlcolumn.append(request.form['stype'])
            htmlcolumn.append(request.form['anstype'])
            htmlcolumn.append(request.form['psurgery'])
            htmlcolumn.append(request.form['spamount'])
            htmlcolumn.append(request.form['disease'])
            htmlcolumn.append(request.form['pfrom'])
            htmlcolumn.append(request.form['wrd_id'])
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getTodaySurgeryPatient():
    try:
        sql="select s.*,p.pfname,p.pmname,p.psname,sp.sprocedure from patient_registration p, surgery_details s,admin_surgery_procedure sp where p.regno=s.regno and s.sdate=curdate() and s.psurgery=sp.sid  order by sid desc"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getCurrentSurgeryPatientOpd(sid):
    try:
        sql="select s.*,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,p.rmname,p.rsname,p.age,p.agetype,p.sex,p.education,p.address,o.opdid,o.vdate,o.complaint,TIME_FORMAT(stime,'%H:%i'),sp.sprocedure from surgery_details s,opdvisit o, patient_registration p,admin_surgery_procedure sp where sp.sid=s.psurgery and  s.regno=p.regno and o.opdid=s.wrd_id and s.sid={}".format(sid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getCurrentSurgeryPatientIpd(sid):
    try:
        sql="select s.*,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,p.rmname,p.rsname,p.age,p.agetype,p.sex,p.education,p.address,i.ipdid,i.ipddate,i.complaint,TIME_FORMAT(stime,'%H:%i'),sp.sprocedure from surgery_details s,ipdvisit i, patient_registration p,admin_surgery_procedure sp where sp.sid=s.psurgery and s.regno=p.regno and i.ipdid=s.wrd_id and s.sid={}".format(sid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def UpdateSurgeryDetails(sid):

    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "surgery_details"
    try:
        if request.method == 'POST':

            dbcolumn.append('sdate')
            dbcolumn.append('stime')
            dbcolumn.append('surgeon')
            dbcolumn.append('anesthesiologist')
            dbcolumn.append('ksurgerytype')
            dbcolumn.append('stype')
            dbcolumn.append('anstype')
            dbcolumn.append('psurgery')
            dbcolumn.append('spamount')
            dbcolumn.append('disease')
            dbcolumn.append('sid')

            htmlcolumn.append(request.form['sdate'])
            htmlcolumn.append(request.form['stime'])
            htmlcolumn.append(request.form['surgeon'])
            htmlcolumn.append(request.form['anesthesiologist'])
            htmlcolumn.append(request.form['ksurgerytype'])
            htmlcolumn.append(request.form['stype'])
            htmlcolumn.append(request.form['anstype'])
            htmlcolumn.append(request.form['psurgery'])
            htmlcolumn.append(request.form['spamount'])
            htmlcolumn.append(request.form['disease'])
            htmlcolumn.append(request.form['sid'])
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getAllSurgeryPatientByDate(surgery):
    surgery=surgery+"surgery.xlsx"
    fdate=request.form['fdate']
    tdate=request.form['tdate']
    pfrom=request.form['pfrom']
    try:
        if (pfrom=='OUTPATIENT'):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and sdate between '{}' and '{}'  and s.pfrom='{}'  order by sdate desc".format(fdate,tdate,pfrom)
        elif (pfrom=='INPATIENT'):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and sdate between '{}' and '{}'  and s.pfrom='{}'  order by sdate desc".format(fdate,tdate,pfrom)
        else:
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' order by sdate desc".format(fdate,tdate)

        cursor.execute(sql)
        p=cursor.fetchall()
        workbook = Workbook(surgery)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'magenta'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"Patient From",cell_format)
        sheet.write(0,2,"FIRST NAME",cell_format)
        sheet.write(0,3,"MIDDLE NAME",cell_format)
        sheet.write(0,4,"SURNAME",cell_format)
        sheet.write(0,5,"Surgery Date",cell_format)
        sheet.write(0,6,"Surgery Procedure",cell_format)
        sheet.write(0,7,"Surgeon Name",cell_format)
        sheet.write(0,8,"Anesthesiologist",cell_format)
        sheet.write(0,9,"Kind of Surgery",cell_format)
        sheet.write(0,10,"Surgery Type",cell_format)
        sheet.write(0,11,"Anesthesia Type",cell_format)
        sheet.write(0,12,"Disease",cell_format)
        sheet.write(0,13,"Sid",cell_format)
        for r, row in enumerate(p):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return p
    except Exception as e:
        return str(e)


def getSurgeryPatientSearchExcel(surgeryExcel):
    surgeryExcel=surgeryExcel+"surgeryExcel.xlsx"
    fdate=request.form['fdate']
    tdate=request.form['tdate']
    ksurgerytype=request.form['ksurgerytype']
    stype=request.form['stype']
    anstype=request.form['anstype']
    psurgery=request.form['psurgery']
    try:
        if(fdate != '' and tdate != '' and   ksurgerytype!='' and stype!='' and anstype!='' and psurgery != ''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.ksurgerytype='{}' and s.stype='{}' and s.anstype='{}' and s.psurgery='{}' order by sdate desc".format(fdate,tdate,ksurgerytype,stype,anstype,psurgery)

        elif(fdate != '' and tdate != '' and   ksurgerytype!='' and stype!='' and psurgery != ''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and   s.ksurgerytype='{}' and s.stype='{}' and s.psurgery = '{}' order by sdate desc".format(fdate,tdate,ksurgerytype,stype,psurgery)

        elif(fdate != '' and tdate != '' and   ksurgerytype!=''  and anstype!='' and psurgery != ''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and   s.ksurgerytype='{}' and s.anstype='{}' and s.psurgery = '{}' order by sdate desc".format(fdate,tdate,ksurgerytype,anstype,psurgery)

        elif(fdate != '' and tdate != '' and   anstype!='' and psurgery != ''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.anstype='{}' and s.psurgery = '{}' order by sdate desc".format(fdate,tdate,anstype,psurgery)

        elif(fdate != '' and tdate != '' and   stype!='' and psurgery != ''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.stype='{}' and s.psurgery = '{}' order by sdate desc".format(fdate,tdate,stype,psurgery)

        elif(fdate != '' and tdate != '' and   stype!='' and anstype!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.stype='{}' and s.anstype = '{}' order by sdate desc".format(fdate,tdate,stype,anstype)

        elif(fdate != '' and tdate != '' and   ksurgerytype!='' and psurgery != ''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.ksurgerytype='{}' and s.psurgery = '{}' order by sdate desc".format(fdate,tdate,ksurgerytype,psurgery)

        elif(fdate != '' and tdate != '' and   ksurgerytype!='' and stype!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,s.sdate,sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.ksurgerytype='{}' and s.stype = '{}' order by sdate desc".format(fdate,tdate,ksurgerytype,stype)

        elif(fdate != '' and tdate != '' and   ksurgerytype!='' and anstype!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.ksurgerytype='{}' and s.anstype = '{}' order by sdate desc".format(fdate,tdate,ksurgerytype,anstype)

        elif(fdate != '' and tdate != '' and   ksurgerytype!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.ksurgerytype='{}' order by sdate desc".format(fdate,tdate,ksurgerytype)

        elif(fdate != '' and tdate != '' and   stype!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.stype='{}' order by sdate desc".format(fdate,tdate,stype)

        elif(fdate != '' and tdate != '' and   anstype!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.anstype='{}' order by sdate desc".format(fdate,tdate,anstype)

        elif(fdate != '' and tdate != '' and   psurgery!=''):
            sql="select s.regno,s.pfrom,p.pfname,p.pmname,p.psname,DATE_FORMAT(s.sdate,'%d/%m/%Y'),sp.sprocedure,s.surgeon,s.anesthesiologist,s.ksurgerytype,s.stype,s.anstype,s.disease,s.sid from surgery_details s,patient_registration p,admin_surgery_procedure sp  where s.regno=p.regno and s.psurgery=sp.sid and s.sdate between '{}' and '{}' and s.psurgery='{}' order by sdate desc".format(fdate,tdate,psurgery)

        cursor.execute(sql)
        p=cursor.fetchall()
        workbook = Workbook(surgeryExcel)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'royalblue'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"Patient From",cell_format)
        sheet.write(0,2,"FIRST NAME",cell_format)
        sheet.write(0,3,"MIDDLE NAME",cell_format)
        sheet.write(0,4,"SURNAME",cell_format)
        sheet.write(0,5,"Surgery Date",cell_format)
        sheet.write(0,6,"Surgery Procedure",cell_format)
        sheet.write(0,7,"Surgeon Name",cell_format)
        sheet.write(0,8,"Anesthesiologist",cell_format)
        sheet.write(0,9,"Kind of Surgery",cell_format)
        sheet.write(0,10,"Surgery Type",cell_format)
        sheet.write(0,11,"Anesthesia Type",cell_format)
        sheet.write(0,12,"Disease",cell_format)
        sheet.write(0,13,"Sid",cell_format)
        for r, row in enumerate(p):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return p
    except Exception as e:
        return str(e)

def getSurgerySPamount(sid):
    try:
        sql="select * from admin_surgery_procedure where sid='{}' and deletestatus=0".format(sid)
        cursor.execute(sql)
        er=cursor.fetchall()
        print(er)
        return er
    except Exception as e:
        return str(e)

############################################################################################################################################################################################################################################################################################
#################################################  SURGERY CODES END  ######################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################################################

#====================Delivery Admin============================#
def InsertNewDelType():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_deliverytype'
        dbcolumn.append('deliverytype')
        dbcolumn.append('amount')
        htmlcolumn.append(request.form['deltype'])
        htmlcolumn.append(request.form['dtamount'])
        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def getAllDelType():
    try:
        sql="select * from admin_deliverytype where deletestatus=0"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getFilterDelType(did):
    try:
        sql="select * from admin_deliverytype where dtid='{}' and deletestatus=0".format(did)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def UpdateDelType():
    try:
        dbcolumn = []
        htmlcolumn= []
        tablename='admin_deliverytype'
        dbcolumn.append('deliverytype')
        dbcolumn.append('amount')
        dbcolumn.append('dtid')
        htmlcolumn.append(request.form['deltype'])
        htmlcolumn.append(request.form['dtamount'])
        htmlcolumn.append(request.form['dtid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)


#====================Delivery Child Insert Starts From Here====================#
def getDeliveryPatientDetail(regno):
    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,i.ipddate,w.wrd_id,a.wname,agetype,p.education from patient_registration p,ipdvisit i,ward_main w,admin_wardname a where p.regno=w.regno and w.ipdid=i.ipdid and w.wid=a.wid and w.wardstatus=1 and a.wid=1 and w.regno='{}'".format(regno)
        #print("i am qwe",sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def insertdeliveryDetails():

    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_delivery"
    wrd_id=request.form['wrd_id']
    regno=request.form['regno']
    try:
        if request.method == 'POST':
            dbcolumn.append('wrd_id')
            dbcolumn.append('regno')
            dbcolumn.append('deliverydate')
            dbcolumn.append('m_edu')
            dbcolumn.append('f_edu')
            dbcolumn.append('gravida')
            dbcolumn.append('noflivechild')
            dbcolumn.append('ut_height')
            dbcolumn.append('dtype')
            dbcolumn.append('mstatus')
            dbcolumn.append('dreason')
            dbcolumn.append('deathtime')
            dbcolumn.append('ddate')
            dbcolumn.append('doctorname')
            dbcolumn.append('sistername')
            dbcolumn.append('bcareby')
            dbcolumn.append('enterby')
            dbcolumn.append('nofbaby')
            dbcolumn.append('damount')
            dbcolumn.append('placenta_delivered')
            dbcolumn.append('pph')
            dbcolumn.append('pstatus')



            htmlcolumn.append(wrd_id)
            htmlcolumn.append(regno)
            htmlcolumn.append(request.form['deliverydate'])
            htmlcolumn.append(request.form['m_edu'])
            htmlcolumn.append(request.form['f_edu'])
            htmlcolumn.append(request.form['gravida'])
            htmlcolumn.append(request.form['noflivechild'])
            htmlcolumn.append(request.form['ut_height'])
            htmlcolumn.append(request.form['dtype'])
            htmlcolumn.append(request.form['mstatus'])
            htmlcolumn.append(request.form['dreason'])
            htmlcolumn.append(request.form['deathtime'])
            htmlcolumn.append(request.form['ddate'])
            htmlcolumn.append(request.form['doctorname'])
            htmlcolumn.append(request.form['sistername'])
            htmlcolumn.append(request.form['bcareby'])
            htmlcolumn.append(request.form['enterby'])
            htmlcolumn.append(request.form['nofbaby'])
            htmlcolumn.append(request.form['damount'])
            htmlcolumn.append(request.form['placenta_delivered'])
            htmlcolumn.append(request.form['pph'])
            htmlcolumn.append(request.form['pstatus'])



            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            print("i am one",result)

            if result==1:
                sql="select delivery_id from ward_delivery order by delivery_id  desc limit 1;"
                cursor.execute(sql)
                delivery_id=cursor.fetchall()
                result1=insertChildDetail(delivery_id[0][0])
                print("i am none",result1)
            return result1
    except Exception as e:
        return str(e)

def insertChildDetail(delivery_id):
    result=''
    tablename = "delivery_child"
    row=len(request.form.getlist('born_time'))

    bdate = request.form.getlist('born_date') #Has Multiple Value
    btime = request.form.getlist('born_time') #Has Multiple Value
    csex = request.form.getlist('child_sex') #Has Multiple Value
    cwt = request.form.getlist('child_weight')  #Has Multiple Value
    cstatus = request.form.getlist('child_status') #Has Multiple Value

    lchild= request.form.getlist('live_child') #Has Multiple Value
    cdtime= request.form.getlist('cdtime') #Has Multiple Value
    cddate= request.form.getlist('cddate') #Has Multiple Value
    cdreason= request.form.getlist('cdreason') #Has Multiple Value
    cabnormal= request.form.getlist('cabnormal') #Has Multiple Value

    for i in range(row):
        if cstatus[i]=='Alive':
            cdtime[i]="0"
            cddate[i]="0"
            cdreason[i]=""
        elif cstatus=='Dead':
            lchild[i]=""


    ppart= request.form.getlist('presenting_part') #Has Multiple Value
    as1= request.form.getlist('apgar_score1') #Has Multiple Value
    as2= request.form.getlist('apgar_score2') #Has Multiple Value
    as3= request.form.getlist('apgar_score3') #Has Multiple Value




    try:
        if request.method == 'POST':

            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('delivery_id')
                dbcolumn.append('born_date')
                dbcolumn.append('born_time')
                dbcolumn.append('child_sex')
                dbcolumn.append('child_weight')
                dbcolumn.append('child_status')
                dbcolumn.append('live_child')
                dbcolumn.append('cdtime')
                dbcolumn.append('cddate')
                dbcolumn.append('cdreason')
                dbcolumn.append('presenting_part')
                dbcolumn.append('apgar_score1')
                dbcolumn.append('apgar_score2')
                dbcolumn.append('apgar_score3')
                dbcolumn.append('cabnormal')





                htmlcolumn.append(str(delivery_id))
                htmlcolumn.append(bdate[i])
                htmlcolumn.append(btime[i])
                htmlcolumn.append(csex[i])
                htmlcolumn.append(str(cwt[i]))
                htmlcolumn.append(cstatus[i])

                if cstatus[i] =='Alive':
                    htmlcolumn.append(lchild[i])
                    htmlcolumn.append(cdtime[i])
                    htmlcolumn.append(cddate[i])
                    htmlcolumn.append(cdreason[i])
                elif cstatus[i] =='Dead':
                    htmlcolumn.append(lchild[i])
                    htmlcolumn.append(cdtime[i])
                    htmlcolumn.append(cddate[i])
                    htmlcolumn.append(cdreason[i])


                htmlcolumn.append(ppart[i])
                htmlcolumn.append(str(as1[i]))
                htmlcolumn.append(str(as2[i]))
                htmlcolumn.append(str(as3[i]))
                htmlcolumn.append(cabnormal[i])







                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result

    except Exception as e:
        return str(e)


#==================Delivery Edit/Update Starts From Here====================#

def getDeliveryDetailsbyReg():
    regno=request.form['regno']

    try:
        sql="select d.delivery_id,p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,a.wname,d.deliverydate,d.m_edu,d.f_edu,d.noflivechild,d.mstatus,d.nofbaby from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i where p.regno=d.regno and w.ipdid=i.ipdid and w.wid=a.wid and d.wrd_id=w.wrd_id and w.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


################################ Current Month Delivery Count######################################
def getDeliveryCount():

    try:
        sql="SELECT count(*),MONTHNAME(CURRENT_DATE()) FROM ward_delivery WHERE MONTH(deliverydate) = MONTH(CURRENT_DATE()) AND YEAR(deliverydate) = YEAR(CURRENT_DATE())"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

################################ Current Month DeliveryDataChild Count Here######################################
def getCurrentMonthDeliveryChildCount():
    try:
        sql="SELECT (select count(*) from ward_delivery where MONTH(deliverydate) = MONTH(CURRENT_DATE()) AND YEAR(deliverydate) = YEAR(CURRENT_DATE())),MONTHNAME(CURRENT_DATE()),COUNT(CASE WHEN UPPER(c.child_sex) = 'MALE' THEN 1 END) Male, COUNT(CASE WHEN UPPER(c.child_sex) = 'FEMALE' THEN 1 END) Female, COUNT(CASE WHEN UPPER(c.child_sex) = 'TRANSGENDER' THEN 1 END) Transgender FROM delivery_child c,ward_delivery d WHERE MONTH(deliverydate) = MONTH(CURRENT_DATE()) AND YEAR(deliverydate) = YEAR(CURRENT_DATE()) and c.delivery_id=d.delivery_id"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


################################ Current Year DeliveryDataChild Count Here######################################

def getCurrentYearDeliveryChildCount():

    try:
        sql="SELECT (select count(*) from ward_delivery where YEAR(deliverydate) = YEAR(CURRENT_DATE())),year(CURRENT_DATE()), COUNT(CASE WHEN UPPER(c.child_sex) = 'MALE' THEN 1 END) Male, COUNT(CASE WHEN UPPER(c.child_sex) = 'FEMALE' THEN 1 END) Female, COUNT(CASE WHEN UPPER(c.child_sex) = 'TRANSGENDER' THEN 1 END) Transgender FROM delivery_child c,ward_delivery d WHERE YEAR(deliverydate) = YEAR(CURRENT_DATE()) and c.delivery_id=d.delivery_id"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


################################ Previous Year DeliveryDataChild Count Here######################################

def getPreviousYearDeliveryChildCount():

    try:
        sql="SELECT (select count(*) from ward_delivery where YEAR(deliverydate) = YEAR(DATE_SUB(CURDATE(), INTERVAL 1 YEAR))),year(deliverydate), COUNT(CASE WHEN UPPER(c.child_sex) = 'MALE' THEN 1 END) Male, COUNT(CASE WHEN UPPER(c.child_sex) = 'FEMALE' THEN 1 END) Female, COUNT(CASE WHEN UPPER(c.child_sex) = 'TRANSGENDER' THEN 1 END) Transgender FROM delivery_child c,ward_delivery d WHERE YEAR(deliverydate) = YEAR(DATE_SUB(CURDATE(), INTERVAL 1 YEAR)) and c.delivery_id=d.delivery_id"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


################################Counts End Here##################################################################


def getDeliveryDetailsbyName():
    pfname=request.form['pfname']

    try:
        sql="select d.delivery_id,p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,a.wname,d.deliverydate,d.m_edu,d.f_edu,d.noflivechild,d.mstatus,d.nofbaby,w.ipdid from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and p.pfname like '{}%'".format(pfname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getDeliveryDetailsbyDate():
    deliverydate=request.form['deliverydate']

    try:
        sql="select d.delivery_id,p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,a.wname,d.deliverydate,d.m_edu,d.f_edu,d.noflivechild,d.mstatus,d.nofbaby from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i where p.regno=d.regno and w.ipdid=i.ipdid and w.wid=a.wid and d.wrd_id=w.wrd_id and d.deliverydate='{}' order by deliverydate desc".format(deliverydate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getDeliveryDetailsbtdate(fdate,tdate):
    fdate=request.form['fdate']
    tdate=request.form['tdate']
    try:
        sql="select d.delivery_id,p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,a.wname,d.deliverydate,d.m_edu,d.f_edu,d.noflivechild,d.mstatus,d.nofbaby from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i where p.regno=d.regno and w.ipdid=i.ipdid and w.wid=a.wid and d.wrd_id=w.wrd_id and d.deliverydate between '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#=================================Getting Mother Data==========================#
def getDeliveryData(delivery_id):

    try:
        sql="select d.delivery_id,d.wrd_id,d.regno,d.deliverydate,d.m_edu,d.f_edu,d.gravida,d.noflivechild,d.ut_height,d.dtype,d.mstatus,d.dreason,TIME_FORMAT(d.deathtime,'%H:%i'),d.ddate,d.doctorname,d.sistername,d.bcareby,d.enterby,d.nofbaby,d.damount,d.placenta_delivered,d.pph,d.pstatus from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and d.delivery_id='{}'".format(delivery_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#============================Getting Child Data===============================#
def getDeliveryChildData(delivery_id):

    try:
        sql="select c.delivery_id,c.born_date,TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),c.cddate,c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,c.child_id,cabnormal from ward_delivery d,delivery_child c where d.delivery_id=c.delivery_id and d.delivery_id='{}'".format(delivery_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#============================== Main Update Starts From Here================== #
def UpdatedeliveryDetails():

    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_delivery"
    delivery_id=request.form['delivery_id']
    wrd_id=request.form['wrd_id']
    regno=request.form['regno']
    try:
        if request.method == 'POST':

            dbcolumn.append('deliverydate')
            dbcolumn.append('m_edu')
            dbcolumn.append('f_edu')
            dbcolumn.append('gravida')
            dbcolumn.append('noflivechild')
            dbcolumn.append('ut_height')
            dbcolumn.append('dtype')
            dbcolumn.append('mstatus')
            dbcolumn.append('dreason')
            dbcolumn.append('deathtime')
            dbcolumn.append('ddate')
            dbcolumn.append('doctorname')
            dbcolumn.append('sistername')
            dbcolumn.append('bcareby')
            dbcolumn.append('enterby')
            dbcolumn.append('nofbaby')
            dbcolumn.append('damount')
            dbcolumn.append('placenta_delivered')
            dbcolumn.append('pph')
            dbcolumn.append('pstatus')
            dbcolumn.append('delivery_id')



            htmlcolumn.append(request.form['deliverydate'])
            htmlcolumn.append(request.form['m_edu'])
            htmlcolumn.append(request.form['f_edu'])
            htmlcolumn.append(request.form['gravida'])
            htmlcolumn.append(request.form['noflivechild'])
            htmlcolumn.append(request.form['ut_height'])
            htmlcolumn.append(request.form['dtype'])
            htmlcolumn.append(request.form['mstatus'])
            htmlcolumn.append(request.form['dreason'])
            htmlcolumn.append(request.form['deathtime'])
            htmlcolumn.append(request.form['ddate'])
            htmlcolumn.append(request.form['doctorname'])
            htmlcolumn.append(request.form['sistername'])
            htmlcolumn.append(request.form['bcareby'])
            htmlcolumn.append(request.form['enterby'])
            htmlcolumn.append(request.form['nofbaby'])
            htmlcolumn.append(request.form['damount'])
            htmlcolumn.append(request.form['placenta_delivered'])
            htmlcolumn.append(request.form['pph'])
            htmlcolumn.append(request.form['pstatus'])
            htmlcolumn.append(delivery_id)

            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            if result==1:
                result1=updateChildDetails()
            return result1
    except Exception as e:
        print("MOM",str(e))
        return str(e)

def updateChildDetails():
    result=''
    tablename = "delivery_child"

    row=len(request.form.getlist('born_time'))
    print("row",row)
    child_id=request.form.getlist('child_id') #Has Multiple Value
    bdate = request.form.getlist('born_date') #Has Multiple Value
    btime = request.form.getlist('born_time') #Has Multiple Value
    csex = request.form.getlist('child_sex') #Has Multiple Value
    cwt = request.form.getlist('child_weight')  #Has Multiple Value
    cstatus = request.form.getlist('child_status') #Has Multiple Value

    lchild= request.form.getlist('live_child') #Has Multiple Value
    cdtime= request.form.getlist('cdtime') #Has Multiple Value
    cddate= request.form.getlist('cddate') #Has Multiple Value
    cdreason= request.form.getlist('cdreason') #Has Multiple Value
    cabnormal= request.form.getlist('cabnormal') #Has Multiple Value


    for i in range(row):
        if cstatus[i]=='Alive':
            cdtime[i]="0"
            cddate[i]="0"
            cdreason[i]=""
        elif cstatus=='Dead':
            lchild[i]=""

    ppart= request.form.getlist('presenting_part') #Has Multiple Value
    as1= request.form.getlist('apgar_score1') #Has Multiple Value
    as2= request.form.getlist('apgar_score2') #Has Multiple Value
    as3= request.form.getlist('apgar_score3') #Has Multiple Value


    try:
        if request.method == 'POST':

            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute

                dbcolumn.append('born_date')
                dbcolumn.append('born_time')
                dbcolumn.append('child_sex')
                dbcolumn.append('child_weight')
                dbcolumn.append('child_status')
                dbcolumn.append('live_child')
                dbcolumn.append('cdtime')
                dbcolumn.append('cddate')
                dbcolumn.append('cdreason')
                dbcolumn.append('presenting_part')
                dbcolumn.append('apgar_score1')
                dbcolumn.append('apgar_score2')
                dbcolumn.append('apgar_score3')
                dbcolumn.append('cabnormal')
                dbcolumn.append('child_id')

                htmlcolumn.append(bdate[i])
                htmlcolumn.append(btime[i])
                htmlcolumn.append(csex[i])
                htmlcolumn.append(str(cwt[i]))
                htmlcolumn.append(cstatus[i])


                if cstatus[i] =='Alive':
                    htmlcolumn.append(lchild[i])
                    htmlcolumn.append(cdtime[i])
                    htmlcolumn.append(cddate[i])
                    htmlcolumn.append(cdreason[i])
                elif cstatus[i] =='Dead':
                    htmlcolumn.append(lchild[i])
                    htmlcolumn.append(cdtime[i])
                    htmlcolumn.append(cddate[i])
                    htmlcolumn.append(cdreason[i])

                htmlcolumn.append(ppart[i])
                htmlcolumn.append(str(as1[i]))
                htmlcolumn.append(str(as2[i]))
                htmlcolumn.append(str(as3[i]))
                htmlcolumn.append(cabnormal[i])
                htmlcolumn.append(str(child_id[i])) # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getDeliveryAllDataRegno():
    regno=request.form['regno']

    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),a.wname,DATE_FORMAT(d.deliverydate,'%d/%m/%Y'),d.m_edu,d.f_edu,d.gravida,d.noflivechild,d.ut_height,d.dtype,d.mstatus,d.dreason,TIME_FORMAT(d.deathtime,'%H:%i'),DATE_FORMAT(d.ddate,'%d/%m/%Y') ,d.doctorname,d.sistername,d.bcareby,d.enterby,d.nofbaby,d.placenta_delivered,d.pph,d.pstatus,DATE_FORMAT(c.born_date,'%d/%m/%Y'),TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),DATE_FORMAT(c.cddate,'%d/%m/%Y'),c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,cabnormal from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i,delivery_child c where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and w.wardstatus=1 and d.delivery_id=c.delivery_id and w.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)



def getDeliveryAllDataName():
    pfname=request.form['pfname']

    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),a.wname,DATE_FORMAT(d.deliverydate,'%d/%m/%Y'),d.m_edu,d.f_edu,d.gravida,d.noflivechild,d.ut_height,d.dtype,d.mstatus,d.dreason,TIME_FORMAT(d.deathtime,'%H:%i'),DATE_FORMAT(d.ddate,'%d/%m/%Y') ,d.doctorname,d.sistername,d.bcareby,d.enterby,d.nofbaby,d.placenta_delivered,d.pph,d.pstatus,DATE_FORMAT(c.born_date,'%d/%m/%Y'),TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),DATE_FORMAT(c.cddate,'%d/%m/%Y'),c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,cabnormal from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i,delivery_child c where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and w.wardstatus=1 and d.delivery_id=c.delivery_id and p.pfname like '{}%'".format(pfname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getDeliveryAllDataByDate():
    deliverydate=request.form['deliverydate']

    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),a.wname,DATE_FORMAT(d.deliverydate,'%d/%m/%Y'),d.m_edu,d.f_edu,d.gravida,d.noflivechild,d.ut_height,d.dtype,d.mstatus,d.dreason,TIME_FORMAT(d.deathtime,'%H:%i'),DATE_FORMAT(d.ddate,'%d/%m/%Y') ,d.doctorname,d.sistername,d.bcareby,d.enterby,d.nofbaby,d.placenta_delivered,d.pph,d.pstatus,DATE_FORMAT(c.born_date,'%d/%m/%Y'),TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),DATE_FORMAT(c.cddate,'%d/%m/%Y'),c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,cabnormal from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i,delivery_child c where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and w.wardstatus=1 and d.delivery_id=c.delivery_id and d.deliverydate='{}' order by deliverydate desc".format(deliverydate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getDeliveryAllDataBTDate(fdate,tdate,delivery):
    delivery=delivery+"delivery.xlsx"
    print("i am path",delivery)
    fdate=request.form['fdate']
    tdate=request.form['tdate']

    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),a.wname,DATE_FORMAT(d.deliverydate,'%d/%m/%Y'),d.m_edu,d.f_edu,d.gravida,d.noflivechild,d.ut_height,d.dtype,d.mstatus,d.dreason,TIME_FORMAT(d.deathtime,'%H:%i'),DATE_FORMAT(d.ddate,'%d/%m/%Y') ,d.doctorname,d.sistername,d.bcareby,d.enterby,d.nofbaby,d.placenta_delivered,d.pph,d.pstatus,DATE_FORMAT(c.born_date,'%d/%m/%Y'),TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),DATE_FORMAT(c.cddate,'%d/%m/%Y'),c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,cabnormal from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i,delivery_child c where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and w.wardstatus=1 and d.delivery_id=c.delivery_id and d.deliverydate between '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        q=cursor.fetchall()

        workbook = Workbook(delivery)
        print("i am workbook=",workbook)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'blue'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"FIRST NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"LAST NAME",cell_format)
        sheet.write(0,4,"SEX",cell_format)
        sheet.write(0,5,"AGE",cell_format)
        sheet.write(0,6,"IPD VisitDate",cell_format)
        sheet.write(0,7,"Ward Name",cell_format)
        sheet.write(0,8,"Delivery Date",cell_format)
        sheet.write(0,9,"Mother EDUCATION",cell_format)
        sheet.write(0,10,"Father EDUCATION",cell_format)
        sheet.write(0,11,"Gravida",cell_format)
        sheet.write(0,12,"No.of Live Child",cell_format)
        sheet.write(0,13,"UT Height",cell_format)
        sheet.write(0,14,"Delivery Type",cell_format)
        sheet.write(0,15,"Mother Status",cell_format)
        sheet.write(0,16,"Death Reason",cell_format)
        sheet.write(0,17,"Death Time",cell_format)
        sheet.write(0,18,"Death Date",cell_format)
        sheet.write(0,19,"Doctor Name",cell_format)
        sheet.write(0,20,"Sister Name",cell_format)
        sheet.write(0,21,"BabyCare By",cell_format)
        sheet.write(0,22,"Enter By",cell_format)
        sheet.write(0,23,"No of Baby",cell_format)
        sheet.write(0,24,"Placenta Delivered",cell_format)
        sheet.write(0,25,"PPH",cell_format)
        sheet.write(0,26,"PPH Status",cell_format)
        sheet.write(0,27,"Child Born Date",cell_format)
        sheet.write(0,28,"Child Born Time",cell_format)
        sheet.write(0,29,"Child Sex",cell_format)
        sheet.write(0,30,"Child Weight",cell_format)
        sheet.write(0,31,"Child Status",cell_format)
        sheet.write(0,32,"Live Child Status",cell_format)
        sheet.write(0,33,"Child Death Time",cell_format)
        sheet.write(0,34,"Child Death Date",cell_format)
        sheet.write(0,35,"Child Death Reason",cell_format)
        sheet.write(0,36,"Presenting Part",cell_format)
        sheet.write(0,37,"APGAR Score1",cell_format)
        sheet.write(0,38,"APGAR Score2",cell_format)
        sheet.write(0,39,"APGAR Score3",cell_format)
        sheet.write(0,40,"Congenital Anamalies",cell_format)

        for r, row in enumerate(q):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return q
        print("i am 2nd q=",q)
    except Exception as e:
        return str(e)


##################################Delivery Print Page#######################################################
def getDeliveryId():
    try:
        sql="select delivery_id from ward_delivery order by delivery_id desc limit 1"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getPatientMotherDetails(delivery_id):
    try:
        sql="select d.delivery_id,p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,p.agetype,i.ipddate,p.address,p.contactno,ag.gsname,i.patientfrom,w.wrd_id,a.wname,aw.bname,d.deliverydate,d.m_edu,d.f_edu,d.gravida,d.noflivechild,d.ut_height,ad.deliverytype,d.mstatus,d.dreason,TIME_FORMAT(d.deathtime,'%H:%i'),d.ddate,d.doctorname,d.sistername,d.bcareby,d.enterby,d.nofbaby,d.damount,d.placenta_delivered,d.pph,d.pstatus from patient_registration p,ward_main w,ward_delivery d,admin_wardname a,ipdvisit i,admin_govsch ag,admin_ward_bdname aw,admin_deliverytype ad where w.ipdid=i.ipdid and w.wrd_id=d.wrd_id and w.regno=p.regno and a.wid=w.wid and w.bedno=aw.bid and ag.gsid=i.govscheme and ad.dtid=d.dtype and  d.delivery_id='{}'".format(delivery_id)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getDeliveryChildDetails(delivery_id):
    try:
        sql="select c.delivery_id,c.born_date,TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),c.cddate,c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,c.child_id,cabnormal from ward_delivery d,delivery_child c where d.delivery_id=c.delivery_id and d.delivery_id='{}'".format(delivery_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
#=============Getting Data For Discharge Using wrd_id
def getPatientMotherDetailsForDischarge(wmid):
    try:
        sql="select *,ad.deliverytype from ward_delivery d,admin_deliverytype ad where d.dtype=ad.dtid and d.wrd_id='{}' order by deliverydate".format(wmid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getDeliveryChildDetailsForDischarge(delid):
    try:
        sql="select c.delivery_id,c.born_date,TIME_FORMAT(c.born_time,'%H:%i'),c.child_sex,c.child_weight,c.child_status,c.live_child,TIME_FORMAT(c.cdtime,'%H:%i'),c.cddate,c.cdreason,c.presenting_part,c.apgar_score1,c.apgar_score2,c.apgar_score3,c.child_id,cabnormal from ward_delivery d,delivery_child c where d.delivery_id=c.delivery_id and d.delivery_id='{}'".format(delid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
#=============Getting Data For Discharge Using wrd_id =========================#

#========================== Nursery Starts From Here ==========================#

#This function will insert a new record in table "ward_nursery" for new patient.
def insertNurseryDetails():
    dbcolumn = []
    htmlcolumn = []
    result1=''
    tablename = "ward_main"

    try:
        if request.method == 'POST':
            dbcolumn.append('ipdid')
            dbcolumn.append('regno')
            dbcolumn.append('wid')
            dbcolumn.append('bedno')

            htmlcolumn.append(request.form['ipdid'])
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['wid'])
            htmlcolumn.append(request.form['bedno'])

            result1 = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            if result1 == 1:

                sql="select wrd_id,regno from ward_main order by wrd_id desc limit 1;"
                cursor.execute(sql)
                t=cursor.fetchall()
                dbcolumn = []
                htmlcolumn = []
                tablename = "ward_nursery"
                result=''
                complaints= request.form.getlist('ns_complaints') #Has Multiple Value
                complaints_val=  ",".join(complaints)
                ns_mod=request.form['ns_mod']
                ns_cdd=request.form['ns_cdd']
                ns_baby=request.form['ns_baby']
                ns_color=request.form['ns_color']
                ns_thrive=request.form['ns_thrive']
                ns_sucking=request.form['ns_sucking']


                dbcolumn.append('wrd_id')
                dbcolumn.append('regno')
                dbcolumn.append('ns_mother_name')
                dbcolumn.append('ns_mother_regno')
                dbcolumn.append('ns_mother_bedno')
                dbcolumn.append('ns_doa')
                dbcolumn.append('ns_toa')
                dbcolumn.append('ns_wt_adm')
                dbcolumn.append('ns_dob')
                dbcolumn.append('ns_tob')
                dbcolumn.append('ns_wt_birth')
                dbcolumn.append('ns_edd')
                dbcolumn.append('ns_apgar0')
                dbcolumn.append('ns_apgar1')
                dbcolumn.append('ns_apgar5')
                dbcolumn.append('ns_delivery_from')
                dbcolumn.append('ns_mod')
                dbcolumn.append('ns_cdd')
                dbcolumn.append('ns_baby')
                dbcolumn.append('ns_color')
                dbcolumn.append('ns_thrive')
                dbcolumn.append('ns_sucking')
                dbcolumn.append('ns_complaints')
                dbcolumn.append('ns_others')
                dbcolumn.append('ns_diagnosis')
                dbcolumn.append('ns_registered_by')

                htmlcolumn.append(str(t[0][0]))
                htmlcolumn.append(t[0][1])
                htmlcolumn.append(request.form['ns_mother_name'])
                htmlcolumn.append(request.form['ns_mother_regno'])
                htmlcolumn.append(request.form['ns_mother_bedno'])
                htmlcolumn.append(request.form['ns_doa'])
                htmlcolumn.append(request.form['ns_toa'])
                htmlcolumn.append(request.form['ns_wt_adm'])
                htmlcolumn.append(request.form['ns_dob'])
                htmlcolumn.append(request.form['ns_tob'])
                htmlcolumn.append(request.form['ns_wt_birth'])
                htmlcolumn.append(request.form['ns_edd'])
                htmlcolumn.append(request.form[str('ns_apgar0')])
                htmlcolumn.append(request.form[str('ns_apgar1')])
                htmlcolumn.append(request.form[str('ns_apgar5')])
                htmlcolumn.append(request.form['ns_delivery_from'])

                if ns_mod =='Others':
                    htmlcolumn.append(request.form['other_ns_mod'])
                else:
                    htmlcolumn.append(request.form['ns_mod'])

                if ns_cdd=='Others':
                    htmlcolumn.append(request.form['other_ns_cdd'])
                else:
                    htmlcolumn.append(request.form['ns_cdd'])

                if ns_baby=='Others':
                    htmlcolumn.append(request.form['other_ns_baby'])
                else:
                    htmlcolumn.append(request.form['ns_baby'])

                if ns_color=='Others':
                    htmlcolumn.append(request.form['other_ns_color'])
                else:
                    htmlcolumn.append(request.form['ns_color'])

                if ns_thrive=='Others':
                    htmlcolumn.append(request.form['other_ns_thrive'])
                else:
                    htmlcolumn.append(request.form['ns_thrive'])

                if ns_sucking=='Others':
                    htmlcolumn.append(request.form['other_ns_sucking'])
                else:
                    htmlcolumn.append(request.form['ns_sucking'])

                htmlcolumn.append(complaints_val)
                htmlcolumn.append(request.form['ns_others'])
                htmlcolumn.append(request.form['ns_diagnosis'])
                htmlcolumn.append(request.form['ns_registered_by'])


                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                return result
    except Exception as e:
        return str(e)

############################# Nursery Ends #####################################



############################ Ward View/Update Starts ###########################

def getwardsViewUpdate(regno):
    try:
        sql="select p.regno,pfname,pmname,psname,regdate,age,agetype,sex,i.ipdid,complaint,patientfrom,i.ipddate,wrd_id,w.ipdid,w.wid,dischargestatus,bname,b.wid,bstatus,wname,wn.wid,wn.deletestatus from patient_registration p,ipdvisit i,ward_main w,admin_ward_bdname b,admin_wardname wn where p.regno=w.regno and i.ipdid=w.ipdid and w.wid=b.wid and w.wid=wn.wid and dischargestatus=0 and bstatus=0 and wn.deletestatus=0 and p.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

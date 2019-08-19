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

def getBillPatientData():
    try:
        regno=request.form['regno']
        sql="select o.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,p.agetype,c.cname,o.vdate,o.opdid from patient_registration p,opdvisit o,admin_company c where  p.regno=o.regno and p.pclass=c.cid and o.regno='{}' order by o.vdate desc limit 1".format(regno)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getMedicineForPharmacy(drugname):
    arr_rows=[]
    try:
        if len(drugname)>=1:
            sql="select mm.drugname,mm.medicine_type,sum(mo.issued_qty),i.unitprice,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od,admin_wardname aw where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id=aw.wid and mo.issued_qty>0 and od.ward_id='7' and  mm.drugname LIKE '{}%' group by(i.batch_no) order by i.expiry_date ASC".format(drugname)
            print(sql)
            cursor.execute(sql)
            dt = cursor.fetchall()
            for i in range(0,len(dt)):
                med = dt[i][0] + " > [" + dt[i][1] + "] > " + str(dt[i][2])+" > " + str(dt[i][3])+" > " + str(dt[i][4])
                arr_rows.append(med)
            print("fgfg",arr_rows)
            return arr_rows
        else:
            return arr_rows
    except Exception as e:
        return str(e)

def insertPatientDetailBillingData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "billing_medicine"

    bmdate = request.form['bmdate']
    regno = request.form['regno']
    givenby = request.form['mgivenby']
    docid = request.form['docid']
    billstatus = request.form['pstatus']
    opdid = request.form['opdid']
    netamount = request.form['netamount']
    try:
        if request.method == 'POST':
            #INSERTING PATIENT BILLING DETAILS
            dbcolumn.append('bmdate')
            dbcolumn.append('regno')
            dbcolumn.append('givenby')
            dbcolumn.append('docid')
            dbcolumn.append('billstatus')
            dbcolumn.append('opdid')
            dbcolumn.append('netamount')
            #dbcolumn.append('printstatus')

            htmlcolumn.append(bmdate)
            htmlcolumn.append(regno)
            htmlcolumn.append(givenby)
            htmlcolumn.append(docid)
            htmlcolumn.append(billstatus)
            htmlcolumn.append(opdid)
            htmlcolumn.append(netamount)
            #htmlcolumn.append("1")
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            #INSERTING MEDICINE DETAILS
            if result == 1:
                sql="select bmid from billing_medicine order by bmid desc limit 1"
                cursor.execute(sql)
                bmid=cursor.fetchall()

                result=''
                tablename = "billing_medicine_detail"

                row=len(request.form.getlist('med_id'))
                meddet_id=request.form.getlist('med_id')
                qty=request.form.getlist('quantity')
                amount=request.form.getlist('unitamount')
                for i in range(row):
                    dbcolumn = []
                    htmlcolumn = []
                    dbcolumn.append('bmid')
                    dbcolumn.append('meddet_id')
                    dbcolumn.append('iqty')
                    dbcolumn.append('amount')

                    htmlcolumn.append(str(bmid[0][0]))
                    htmlcolumn.append(str(meddet_id[i]))
                    htmlcolumn.append(str(qty[i]))
                    htmlcolumn.append(str(amount[i]))
                    print(htmlcolumn)
                    result = ins.InsertData(dbcolumn,htmlcolumn,tablename)


                #UPDATING THE medicine_outward_detail

                if result==1:
                    result=''
                    tablename = "medicine_outward_detail"
                    row=len(request.form.getlist('med_id'))
                    meddet_id=request.form.getlist('med_id')
                    remqty=request.form.getlist('remquantity')
                    print("remqty",remqty)
                    for i in range(row):
                        dbcolumn = []
                        htmlcolumn = []
                        dbcolumn.append('issued_qty')
                        dbcolumn.append('meddet_id')

                        htmlcolumn.append(str(remqty[i]))
                        htmlcolumn.append(meddet_id[i])
                        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    return result
    except Exception as e:
        print("ERROR",str(e))
        return str(e)


def getDocMedicineDetail():
    try:
        sql="select bm.bmid,bm.regno,p.pfname,p.pmname,p.psname,o.vdate from patient_registration p,opdvisit o,billing_medicine bm where p.regno=o.regno and o.opdid=bm.opdid and o.vdate=curdate() and docid <> '-1' and printstatus=0"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getMedDetails(bmid):
    try:
        sql="select m.medicine_type,m.drugname,i.unitprice,md.issued_qty,bmd.meddet_id,bmd.iqty,bmd.amount,bm.bmid,bmd.mbmid from main_medicine m,inventory_detail i,medicine_outward_detail md,outward_detail od,billing_medicine bm,billing_medicine_detail bmd where bm.bmid=bmd.bmid and bmd.meddet_id = md.meddet_id and od.outw_id = md.outw_id and md.inv_id=i.inv_id and i.med_id=m.med_id and bm.bmid='{}'".format(bmid)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def updateBillingDetail():
    try:
        result=''
        tablename = "billing_medicine"
        dbcolumn = []
        htmlcolumn = []
        dbcolumn.append('givenby')
        dbcolumn.append('billstatus')
        dbcolumn.append('bmid')
        htmlcolumn.append(request.form['mgivenby'])
        htmlcolumn.append(request.form['pstatus'])
        htmlcolumn.append(request.form['bmid'])
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

def getPatientDetailsPharmacy():
    try:
        sql="select b.bmid,b.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,p.sex,c.cname,b.billstatus,b.netamount,b.givenby,round(b.netamount)-b.netamount,round(b.netamount) from patient_registration p,billing_medicine b,admin_company c where p.regno=b.regno and p.pclass=c.cid and docid=-1 order by bmid desc limit 1"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getPharDetailsForBilling(bmid):
    try:
        sql="select m.medicine_type,m.drugname,i.unitprice,bmd.iqty,bmd.amount from main_medicine m,inventory_detail i,medicine_outward_detail md,outward_detail od,billing_medicine bm,billing_medicine_detail bmd where bm.bmid=bmd.bmid and bmd.meddet_id = md.meddet_id and od.outw_id = md.outw_id and md.inv_id=i.inv_id and i.med_id=m.med_id and bm.bmid='{}'".format(bmid)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getPatientDetailsDoctor(bmid):
    try:
        sql="select b.bmid,b.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,p.sex,c.cname,b.billstatus,b.netamount,b.givenby,round(b.netamount)-b.netamount,round(b.netamount) from patient_registration p,billing_medicine b,admin_company c where p.regno=b.regno and p.pclass=c.cid and b.bmid='{}'".format(bmid)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def getDocDetailsForBilling(bmid):
    try:
        sql="select m.medicine_type,m.drugname,i.unitprice,bmd.iqty,bmd.amount from main_medicine m,inventory_detail i,medicine_outward_detail md,outward_detail od,billing_medicine bm,billing_medicine_detail bmd where bm.bmid=bmd.bmid and bmd.meddet_id = md.meddet_id and od.outw_id = md.outw_id and md.inv_id=i.inv_id and i.med_id=m.med_id and bm.bmid='{}'".format(bmid)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


def updatePrintStatus(bmid):
    try:
        result=''
        tablename = "billing_medicine"
        dbcolumn = []
        htmlcolumn = []

        dbcolumn.append('printstatus')
        dbcolumn.append('bmid')

        htmlcolumn.append("1")
        htmlcolumn.append(bmid)
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)

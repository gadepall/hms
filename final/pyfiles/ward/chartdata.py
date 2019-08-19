from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys
import db_conf as con
import datetime as dt,time as tm
import insertdata as ins
import updatedata as up

db = con.db
cursor=db.cursor()

now = dt.datetime.now()
dtd = now.strftime('%Y')

def getChartDataByRegno(regno):
    try:
        sql="select p.regno,p.pfname,pmname,psname,p.age,p.agetype,p.sex,i.ipddate,i.complaint,w.wrd_id from patient_registration p,ipdvisit i,ward_main w where p.regno=w.regno and i.ipdid=w.ipdid and w.wardstatus=1 and w.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def insertTPRdata():
    result=''
    tablename = "ward_tpr_chart"

    row=len(request.form.getlist('temp'))
    ttime=request.form.getlist('tprtime')
    ttemp=request.form.getlist('temp')
    tpulse=request.form.getlist('pulse')
    tsystolic=request.form.getlist('systolic')
    tdiastolic=request.form.getlist('diastolic')
    trespiration=request.form.getlist('respiration')
    tfhs=request.form.getlist('fhs')
    tspo2=request.form.getlist('spo2')
    try:
        if request.method == 'POST':
            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                dbcolumn.append('wrd_id')
                dbcolumn.append('tdate')
                dbcolumn.append('ttime')
                dbcolumn.append('ttemp')
                dbcolumn.append('tpulse')
                dbcolumn.append('tsystolic')
                dbcolumn.append('tdiastolic')
                dbcolumn.append('trespiration')
                dbcolumn.append('tfhs')
                dbcolumn.append('tspo2')
                dbcolumn.append('tgivenby')

                htmlcolumn.append(request.form['wrd_id'])
                htmlcolumn.append(request.form['tdate'])
                htmlcolumn.append(ttime[i])
                htmlcolumn.append(ttemp[i])
                htmlcolumn.append(tpulse[i])
                htmlcolumn.append(tsystolic[i])
                htmlcolumn.append(tdiastolic[i])
                htmlcolumn.append(trespiration[i])
                htmlcolumn.append(tfhs[i])
                htmlcolumn.append(tspo2[i])
                htmlcolumn.append(request.form['tgivenby'])

            # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getMedicineForWard(drugname,medtype,wrd_id):
    arr_rows=[]
    try:
        if len(drugname)>=1:
            sql="select mm.drugname,mm.medicine_type,sum(mo.issued_qty),i.unitprice,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od,admin_wardname aw where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id=aw.wid and mm.medicine_type='{}' and wid='{}' and mo.issued_qty<>0 and mm.drugname LIKE '{}%' group by batch_no order by expiry_date ASC".format(medtype,wrd_id,drugname)
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

def insertWardMedicineData():
    try:
        result=''
        dtype=request.form.getlist('drugtype')
        wrd_id=request.form['wrd_id']# will store
        mdate=request.form['mdate']# will store
        givenby=request.form['givenby']# will store

        row=len(request.form.getlist('mid'))
        print("HELLLLLLE=",row)
        mid=request.form.getlist('mid')# will store
        remqty=request.form.getlist('remqty')
        print("remqty",remqty)
        schedule = request.form.getlist('schedule')# will store
        unitprice = request.form.getlist('unitprice')#not going to store
        print("schedule ",schedule)
        amount=[]
        tdu=[]
        totaldose=[]
        unit=[]
        schno=request.form.getlist('schno')
        print("schno ",schno)
        ttime=request.form.getlist('mtime')
        print("ttime= ",ttime)
        drugdose=request.form.getlist('drugdose')
        doseunit=request.form.getlist('doseunit')
        k=0
        for i in range(row):
            temp=''
            tdose=0.0
            u=''
            for j in range(int(schno[i])):
                temp=temp+str(ttime[k])+","+str(drugdose[k])+"|"
                tdose=tdose+float(drugdose[k])
                u=str(doseunit[i])
                k=k+1
            tdu.append(temp)# will store
            unit.append(u)# will store
            totaldose.append(str(tdose))#not going to store
            if dtype[i]=='Tablet' or dtype[i]=='Capsule':
                amount.append(str(float(unitprice[i])*float(totaldose[i])))# will store
            else:
                amount.append(str(float(unitprice[i])))# will store
            dbcolumn=[]
            htmlcolumn=[]
            tablename = "ward_medicine_chart"

            dbcolumn.append('wrd_id')
            dbcolumn.append('meddet_id')
            dbcolumn.append('wmcdate')
            dbcolumn.append('schedule')
            dbcolumn.append('time_dose')
            dbcolumn.append('unit')
            dbcolumn.append('givenby')
            dbcolumn.append('quantity')
            dbcolumn.append('amount')

            htmlcolumn.append(str(wrd_id))
            htmlcolumn.append(str(mid[i]))
            htmlcolumn.append(mdate)
            htmlcolumn.append(schedule[i])
            htmlcolumn.append(tdu[i])
            htmlcolumn.append(unit[i])
            htmlcolumn.append(givenby)
            htmlcolumn.append(totaldose[i])
            htmlcolumn.append(amount[i])
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            if result == 1:
                dbcolumn=[]
                htmlcolumn=[]
                tablename="medicine_outward_detail"
                dbcolumn.append('issued_qty')
                dbcolumn.append('meddet_id')
                htmlcolumn.append(str(remqty[i]))
                htmlcolumn.append(mid[i])
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        return result
    except Exception as e:
        return str(e)



def getMedicineForWardIntake(intakename,wardid):
    arr_rows=[]
    try:
        if len(intakename)>=1:
            sql="select mm.drugname,mm.medicine_type,sum(mo.issued_qty),i.unitprice,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od,admin_wardname aw where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id=aw.wid and od.ward_id='{}' and (mm.medicine_type='Saline' or mm.medicine_type='Injection') and mo.issued_qty<>0 and  mm.drugname LIKE '{}%' group by batch_no order by expiry_date ASC".format(wardid,intakename)
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

def insertWardIntakeData():
    result=''
    wrd_id=request.form['wrd_id']
    idate=request.form['idate']
    igivenby=request.form['igivenby']
    rowno=len(request.form.getlist('med_id'))
    itime=request.form.getlist('intime')
    iintaketype=request.form.getlist('intaketype')
    meddet_id=request.form.getlist('med_id')
    idose=request.form.getlist('idose')
    iunit=request.form.getlist('iunit')
    iamount=request.form.getlist('iamount')
    remqty=request.form.getlist('remqty')
    try:
        if request.method == 'POST':
            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                tablename = "ward_intake_chart"
                dbcolumn.append('wrd_id')
                dbcolumn.append('idate')
                dbcolumn.append('itime')
                dbcolumn.append('iintaketype')
                dbcolumn.append('meddet_id')
                dbcolumn.append('idose')
                dbcolumn.append('iunit')
                dbcolumn.append('igivenby')
                dbcolumn.append('iamount')

                htmlcolumn.append(wrd_id)
                htmlcolumn.append(idate)
                htmlcolumn.append(itime[i])
                htmlcolumn.append(iintaketype[i])
                htmlcolumn.append(meddet_id[i])
                htmlcolumn.append(idose[i])
                htmlcolumn.append(iunit[i])
                htmlcolumn.append(igivenby)
                htmlcolumn.append(iamount[i])
            # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                if result == 1:
                    dbcolumn=[]
                    htmlcolumn=[]
                    tablename="medicine_outward_detail"
                    dbcolumn.append('issued_qty')
                    dbcolumn.append('meddet_id')
                    htmlcolumn.append(str(remqty[i]))
                    htmlcolumn.append(meddet_id[i])
                    result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getMedicineForWardSugar(insuline,wardid):
    arr_rows=[]
    try:
        if len(insuline)>=1:
            sql="select mm.drugname,mm.medicine_type,sum(mo.issued_qty),i.unitprice,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od,admin_wardname aw where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id=aw.wid and od.ward_id='{}' and mm.medicine_type='Injection' and mo.issued_qty<>0 and mm.drugname LIKE '{}%' group by batch_no order by expiry_date ASC".format(wardid,insuline)
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


def insertWardSugarData():
    result=''
    wrd_id=request.form['wrd_id']
    sdate=request.form['sdate']
    stime=request.form['stime']
    sugarlevel=request.form['sugarlevel']
    sinsuline=request.form['med_id']
    sdose=request.form['sdose']
    sunit=request.form['sunit']
    sgivenby=request.form['givenby']
    samount=request.form['sprice']
    remqty=request.form['remqty']
    try:
        if request.method == 'POST':
                dbcolumn = []
                htmlcolumn = []
                tablename = "ward_sugar_chart"
                dbcolumn.append('wrd_id')
                dbcolumn.append('sdate')
                dbcolumn.append('stime')
                dbcolumn.append('sugarlevel')
                dbcolumn.append('sinsuline')
                dbcolumn.append('sdose')
                dbcolumn.append('sunit')
                dbcolumn.append('sgivenby')
                dbcolumn.append('samount')


                htmlcolumn.append(wrd_id)
                htmlcolumn.append(sdate)
                htmlcolumn.append(stime)
                htmlcolumn.append(sugarlevel)
                htmlcolumn.append(sinsuline)
                htmlcolumn.append(sdose)
                htmlcolumn.append(sunit)
                htmlcolumn.append(sgivenby)
                htmlcolumn.append(samount)

            # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                if result == 1:
                    dbcolumn=[]
                    htmlcolumn=[]
                    tablename="medicine_outward_detail"
                    dbcolumn.append('issued_qty')
                    dbcolumn.append('meddet_id')
                    htmlcolumn.append(str(remqty))
                    htmlcolumn.append(sinsuline)
                    result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                return result
    except Exception as e:
        return str(e)



def getMedicineForWardPoison(injection,wardid):
    arr_rows=[]
    try:
        if len(injection)>=1:
            sql="select mm.drugname,mm.medicine_type,sum(mo.issued_qty),i.unitprice,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od,admin_wardname aw where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id=aw.wid and od.ward_id='{}' and mo.issued_qty<>0 and mm.medicine_type='Injection' and mm.drugname LIKE '{}%' group by batch_no order by expiry_date ASC".format(wardid,injection)
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


def insertWardPoisonData():
    result=''
    wrd_id=request.form['wrd_id']
    pdate=request.form['pdate']
    ptime=request.form['ptime']
    pinjection=request.form['pmed_id']
    pdose=request.form['pdose']
    punit=request.form['punit']
    pgivenby=request.form['pgivenby']
    pamount=request.form['pprice']
    remqty=request.form['remqty']

    try:
        if request.method == 'POST':
                dbcolumn = []
                htmlcolumn = []
                tablename = "ward_poision_chart"
                dbcolumn.append('wrd_id')
                dbcolumn.append('pdate')
                dbcolumn.append('ptime')
                dbcolumn.append('pinjection')
                dbcolumn.append('pdose')
                dbcolumn.append('punit')
                dbcolumn.append('pgivenby')
                dbcolumn.append('pamount')

                htmlcolumn.append(wrd_id)
                htmlcolumn.append(pdate)
                htmlcolumn.append(ptime)
                htmlcolumn.append(pinjection)
                htmlcolumn.append(pdose)
                htmlcolumn.append(punit)
                htmlcolumn.append(pgivenby)
                htmlcolumn.append(pamount)

            # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                if result == 1:
                    dbcolumn=[]
                    htmlcolumn=[]
                    tablename="medicine_outward_detail"
                    dbcolumn.append('issued_qty')
                    dbcolumn.append('meddet_id')
                    htmlcolumn.append(str(remqty))
                    htmlcolumn.append(pinjection)
                    result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                return result
    except Exception as e:
        return str(e)



def getMedicineForWardConsume(consume,wrd_id):
    arr_rows=[]
    try:
        if len(consume)>=1:
            sql="select mm.drugname,mm.medicine_type,sum(mo.issued_qty),i.unitprice,mo.meddet_id from main_medicine mm,inventory_detail i,medicine_outward_detail mo,outward_detail od,admin_wardname aw where mm.med_id=i.med_id and i.inv_id=mo.inv_id and mo.outw_id=od.outw_id and od.ward_id=aw.wid and od.ward_id='{}' and mm.medicine_type='Consumable' and  mo.issued_qty<>0 and mm.drugname LIKE '{}%' group by batch_no order by expiry_date ASC".format(wrd_id,consume)
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



def insertWardConsumeData():
    result=''
    wrd_id=request.form['wrd_id']
    wccdate=request.form['cdate']
    givenby=request.form['cgivenby']
    row=len(request.form.getlist('conmed_id'))
    wcctime=request.form.getlist('contime')
    conname=request.form.getlist('conmed_id')
    cqty=request.form.getlist('conqty')
    camount=request.form.getlist('conprice')
    remqty=request.form.getlist('remqty')

    try:
        if request.method == 'POST':
            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                tablename = "ward_consume_chart"
                dbcolumn.append('wrd_id')
                dbcolumn.append('wccdate')
                dbcolumn.append('wcctime')
                dbcolumn.append('cgivenby')
                dbcolumn.append('conname')
                dbcolumn.append('cqty')
                dbcolumn.append('camount')

                htmlcolumn.append(wrd_id)
                htmlcolumn.append(wccdate)
                htmlcolumn.append(wcctime[i])
                htmlcolumn.append(givenby)
                htmlcolumn.append(conname[i])
                htmlcolumn.append(cqty[i])
                htmlcolumn.append(str(float(cqty[i])*float(camount[i])))
            # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                if result == 1:
                    dbcolumn=[]
                    htmlcolumn=[]
                    tablename="medicine_outward_detail"
                    dbcolumn.append('issued_qty')
                    dbcolumn.append('meddet_id')
                    htmlcolumn.append(str(remqty[i]))
                    htmlcolumn.append(conname[i])
                    result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getAllDressingAmount(dname):
    try:
        sql="select drsamount from admin_dressing where drsid='{}'".format(dname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def insertWardDressingData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_dressing"
    try:
        if request.method == 'POST':
            dbcolumn.append('wrd_id')
            dbcolumn.append('dressing_date')
            dbcolumn.append('dressing_name')
            dbcolumn.append('dressing_amount')
            dbcolumn.append('dressing_doneby')

            htmlcolumn.append(request.form['wrd_id'])
            htmlcolumn.append(request.form['dressing_date'])
            htmlcolumn.append(request.form['dname'])
            htmlcolumn.append(request.form[str('dressing_amount')])
            htmlcolumn.append(request.form['dressing_doneby'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getAllPhysiotherapyAmount(pname):
    try:
        sql="select phyamount from admin_physiotherapy where phyid='{}'".format(pname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def insertWardPhysiotherapyData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_physiotherapy"
    try:
        if request.method == 'POST':
            dbcolumn.append('wrd_id')
            dbcolumn.append('physiotherapy_date')
            dbcolumn.append('physiotherapy_name')
            dbcolumn.append('physiotherapy_amount')

            htmlcolumn.append(request.form['wrd_id'])
            htmlcolumn.append(request.form['physiotherapy_date'])
            htmlcolumn.append(request.form['pname'])
            htmlcolumn.append(request.form[str('physiotherapy_amount')])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


########################### Ward Charts Ends ###################################



######################## Nursery Charts Starts #################################

def insertNurseryTPRChart():
    result=''
    tablename = "ward_nursery_tprchart"
    row=len(request.form.getlist('tpr_temp'))

    ttime=request.form.getlist('tpr_time')
    ttemp=request.form.getlist('tpr_temp')
    trespiration=request.form.getlist('tpr_respiration')
    turine=request.form.getlist('tpr_urine')
    tstool=request.form.getlist('tpr_stool')
    tspo2=request.form.getlist('tpr_spo2')
    tweight=request.form.getlist('tpr_weight')
    try:
        if request.method == 'POST':
            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                dbcolumn.append('wrd_id')
                dbcolumn.append('tpr_date')
                dbcolumn.append('tpr_givenby')
                dbcolumn.append('tpr_time')
                dbcolumn.append('tpr_temp')
                dbcolumn.append('tpr_respiration')
                dbcolumn.append('tpr_urine')
                dbcolumn.append('tpr_stool')
                dbcolumn.append('tpr_spo2')
                dbcolumn.append('tpr_weight')

                htmlcolumn.append(request.form['wrd_id'])
                htmlcolumn.append(request.form['tpr_date'])
                htmlcolumn.append(request.form['tpr_givenby'])
                htmlcolumn.append(ttime[i])
                htmlcolumn.append(ttemp[i])
                htmlcolumn.append(trespiration[i])
                htmlcolumn.append(turine[i])
                htmlcolumn.append(tstool[i])
                htmlcolumn.append(tspo2[i])
                htmlcolumn.append(tweight[i])

                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getAllTherapyAmount(tname):
    try:
        sql="select adm_therapyamount from admin_therapy where adm_therapyid='{}'".format(tname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def insertNurseryTherapy():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_nursery_therapy"
    try:
        if request.method == 'POST':

            dbcolumn.append('wrd_id')
            dbcolumn.append('therapy_date')
            dbcolumn.append('therapy_givenby')
            dbcolumn.append('therapy_name')
            dbcolumn.append('therapy_starttime')
            dbcolumn.append('therapy_endtime')
            dbcolumn.append('therapy_duration')
            dbcolumn.append('therapy_amount')


            htmlcolumn.append(request.form['wrd_id'])
            htmlcolumn.append(request.form['therapy_date'])
            htmlcolumn.append(request.form['therapy_givenby'])
            htmlcolumn.append(request.form['tname'])
            htmlcolumn.append(request.form['therapy_starttime'])
            htmlcolumn.append(request.form['therapy_endtime'])
            htmlcolumn.append(request.form['therapy_duration'])
            htmlcolumn.append(request.form[str('therapy_amount')])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)






####################### Nursery Charts Ends ####################################


#========================= Nursery Charts View Update =========================#
def getAllNurseryData(wrd_id):
    try:
        sql="select ns_id,wrd_id,regno,ns_mother_name,ns_mother_regno,ns_mother_bedno,ns_doa,TIME_FORMAT(ns_toa,'%H:%i'),ns_wt_adm,ns_dob,TIME_FORMAT(ns_tob,'%H:%i'),ns_wt_birth,ns_edd,ns_apgar0,ns_apgar1,ns_apgar5,ns_delivery_from,ns_mod,ns_cdd,ns_baby,ns_color,ns_thrive,ns_sucking,ns_complaints,ns_others,ns_diagnosis,ns_registered_by from ward_nursery where wrd_id='{}'".format(wrd_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def UpdateNurSheetData():
    ns_id = request.form['ns_id']
    dbcolumn = []
    htmlcolumn = []
    tablename = "ward_nursery"
    result=''
    ns_mod=request.form['ns_mod']
    ns_cdd=request.form['ns_cdd']
    ns_baby=request.form['ns_baby']
    ns_color=request.form['ns_color']
    ns_thrive=request.form['ns_thrive']
    ns_sucking=request.form['ns_sucking']

    try:
        if request.method == 'POST':

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
            dbcolumn.append('ns_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

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

            htmlcolumn.append(request.form['ns_complaints'])
            htmlcolumn.append(request.form['ns_others'])
            htmlcolumn.append(request.form['ns_diagnosis'])
            htmlcolumn.append(request.form['ns_registered_by'])
            htmlcolumn.append(request.form['ns_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getAllNurTPRChartData(wrd_id):
    try:
        sql="select ns_tpr_id,wrd_id,tpr_date,tpr_givenby,TIME_FORMAT(tpr_time,'%H:%i'),tpr_temp,tpr_respiration,tpr_urine,tpr_stool,tpr_spo2,tpr_weight from ward_nursery_tprchart where wrd_id='{}' order by tpr_date desc".format(wrd_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def UpdateNurTPRChartData():
    ns_tpr_id=request.form['ns_tpr_id']
    result=''
    tablename = "ward_nursery_tprchart"
    row=len(request.form.getlist('tpr_temp'))
    ttime=request.form.getlist('tpr_time')
    ttemp=request.form.getlist('tpr_temp')
    trespiration=request.form.getlist('tpr_respiration')
    turine=request.form.getlist('tpr_urine')
    tstool=request.form.getlist('tpr_stool')
    tspo2=request.form.getlist('tpr_spo2')
    tweight=request.form.getlist('tpr_weight')
    try:
        if request.method == 'POST':
            for i in range(row):
                dbcolumn = []
                htmlcolumn = []

                dbcolumn.append('tpr_date')
                dbcolumn.append('tpr_givenby')
                dbcolumn.append('tpr_time')
                dbcolumn.append('tpr_temp')
                dbcolumn.append('tpr_respiration')
                dbcolumn.append('tpr_urine')
                dbcolumn.append('tpr_stool')
                dbcolumn.append('tpr_spo2')
                dbcolumn.append('tpr_weight')
                dbcolumn.append('ns_tpr_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


                htmlcolumn.append(request.form['tpr_date'])
                htmlcolumn.append(request.form['tpr_givenby'])
                htmlcolumn.append(ttime[i])
                htmlcolumn.append(ttemp[i])
                htmlcolumn.append(trespiration[i])
                htmlcolumn.append(turine[i])
                htmlcolumn.append(tstool[i])
                htmlcolumn.append(tspo2[i])
                htmlcolumn.append(tweight[i])
                htmlcolumn.append(request.form['ns_tpr_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

                # Here we are calling UpdateData that have a  common  code for update record.
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getAllDressingData(wrd_id):
    try:
        sql="select drsid,drsname,dressing_id,wrd_id,dressing_date,dressing_name,dressing_amount,dressing_doneby from admin_dressing,ward_dressing where drsid=dressing_name and wrd_id='{}' order by dressing_date desc".format(wrd_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def UpdateWardDressingData():
    dressing_id=request.form['dressing_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_dressing"

    try:
        if request.method == 'POST':
            dbcolumn.append('dressing_date')
            dbcolumn.append('dressing_name')
            dbcolumn.append('dressing_amount')
            dbcolumn.append('dressing_doneby')
            dbcolumn.append('dressing_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(request.form['dressing_date'])
            htmlcolumn.append(request.form['dname'])
            htmlcolumn.append(request.form[str('dressing_amount')])
            htmlcolumn.append(request.form['dressing_doneby'])
            htmlcolumn.append(request.form['dressing_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            print(result,"ooooooooooooooooooooooooooooo")
            return result
    except Exception as e:
        return str(e)

def getAllTherapyData(wrd_id):
    try:
        sql="select adm_therapyid,adm_therapyname,therapy_id,wrd_id,therapy_date,therapy_name,TIME_FORMAT(therapy_starttime,'%H:%i'),TIME_FORMAT(therapy_endtime,'%H:%i'),therapy_duration,therapy_amount,therapy_givenby from admin_therapy,ward_nursery_therapy where adm_therapyid=therapy_name and wrd_id='{}' order by therapy_date desc".format(wrd_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def UpdateNurseryTherapyData():
    therapy_id=request.form['therapy_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_nursery_therapy"

    try:
        if request.method == 'POST':

            dbcolumn.append('therapy_date')
            dbcolumn.append('therapy_givenby')
            dbcolumn.append('therapy_name')
            dbcolumn.append('therapy_starttime')
            dbcolumn.append('therapy_endtime')
            dbcolumn.append('therapy_duration')
            dbcolumn.append('therapy_amount')
            dbcolumn.append('therapy_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(request.form['therapy_date'])
            htmlcolumn.append(request.form['therapy_givenby'])
            htmlcolumn.append(request.form['tname'])
            htmlcolumn.append(request.form['therapy_starttime'])
            htmlcolumn.append(request.form['therapy_endtime'])
            htmlcolumn.append(request.form['therapy_duration'])
            htmlcolumn.append(request.form[str('therapy_amount')])
            htmlcolumn.append(request.form['therapy_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getAllMedicineChartData(wrd_id):
    try:
        sql="select wmcid,wrd_id,wmc.meddet_id,wmcdate,schedule,time_dose,unit,givenby,wmc.quantity,wmc.amount,drugname from ward_medicine_chart wmc,medicine_outward_detail m,inventory_detail id,main_medicine mm where wmc.meddet_id=m.meddet_id and m.inv_id=id.inv_id and id.med_id=mm.med_id and wrd_id='{}' order by wmcdate desc".format(wrd_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#----retreiving data from main medicine  in one text box(drugname)
def GetAllMeddata():
    drugname=request.form['drugname']
    arr_rows=[]
    try:
        if len(drugname)>=1:
            sql="select drugname,medicine_type,med_id from main_medicine where drugname like '{}%'".format(drugname)
            cursor.execute(sql)
            outdata=cursor.fetchall()
            for i in range(0,len(outdata)):
                med = outdata[i][0] + " >  " +outdata[i][1] + " > medid: "+ str(outdata[i][2])
                arr_rows.append(med)
            return arr_rows
        else:
            return arr_rows
    except Exception as e:
        return str(e)




########################## Nursery Chart Update Ends ###########################

############################################### CHART UPDATE START #####################################################

def getPatientTPRData(wmid):
    try:
        sql="select tpr_id,wrd_id,tdate,TIME_FORMAT(ttime,'%H:%i'),ttemp,tpulse,tsystolic,tdiastolic,trespiration,tfhs,tspo2,tgivenby from ward_tpr_chart where wrd_id='{}' order by tdate desc".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def UpdatePatientTPRData():
    tpr_id=request.form['tpr_id']
    result=''
    tablename = "ward_tpr_chart"
    row=len(request.form.getlist('ttemp'))
    ttime=request.form.getlist('ttime')
    ttemp=request.form.getlist('ttemp')
    tpulse=request.form.getlist('tpulse')
    tsystolic=request.form.getlist('tsystolic')
    tdiastolic=request.form.getlist('tdiastolic')
    trespiration=request.form.getlist('trespiration')
    tfhs=request.form.getlist('tfhs')
    tspo2=request.form.getlist('tspo2')
    try:
        if request.method == 'POST':
            for i in range(row):
                dbcolumn = []
                htmlcolumn = []

                dbcolumn.append('tdate')
                dbcolumn.append('tgivenby')
                dbcolumn.append('ttime')
                dbcolumn.append('ttemp')
                dbcolumn.append('tpulse')
                dbcolumn.append('tsystolic')
                dbcolumn.append('tdiastolic')
                dbcolumn.append('trespiration')
                dbcolumn.append('tfhs')
                dbcolumn.append('tspo2')
                dbcolumn.append('tpr_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

                htmlcolumn.append(request.form['tdate'])
                htmlcolumn.append(request.form['tgivenby'])
                htmlcolumn.append(ttime[i])
                htmlcolumn.append(ttemp[i])
                htmlcolumn.append(tpulse[i])
                htmlcolumn.append(tsystolic[i])
                htmlcolumn.append(tdiastolic[i])
                htmlcolumn.append(trespiration[i])
                htmlcolumn.append(tfhs[i])
                htmlcolumn.append(tspo2[i])
                htmlcolumn.append(request.form['tpr_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

                # Here we are calling UpdateData that have a  common  code for update record.
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getPatientDressingData(wmid):
    try:
        sql="select drsid,drsname,dressing_id,wrd_id,dressing_date,dressing_name,dressing_amount,dressing_doneby from admin_dressing,ward_dressing where drsid=dressing_name and wrd_id='{}' order by dressing_date desc".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def UpdateWardDressing():
    dressing_id=request.form['dressing_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_dressing"

    try:
        if request.method == 'POST':
            dbcolumn.append('dressing_date')
            dbcolumn.append('dressing_name')
            dbcolumn.append('dressing_amount')
            dbcolumn.append('dressing_doneby')
            dbcolumn.append('dressing_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(request.form['dressing_date'])
            htmlcolumn.append(request.form['dname'])
            htmlcolumn.append(request.form[str('dressing_amount')])
            htmlcolumn.append(request.form['dressing_doneby'])
            htmlcolumn.append(request.form['dressing_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            print(result,"ooooooooooooooooooooooooooooo")
            return result
    except Exception as e:
        return str(e)


def getPatientPhysioData(wmid):
    try:
        sql="select ap.phyid,ap.phyname,wp.physiotherapy_id,wp.wrd_id,wp.physiotherapy_date,wp.physiotherapy_name,wp.physiotherapy_amount from admin_physiotherapy ap, ward_physiotherapy wp where ap.phyid=wp.physiotherapy_name and wp.wrd_id='{}' order by wp.physiotherapy_date desc".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAllPhysioAmount(physioname):
    try:
        sql="select phyamount from admin_physiotherapy where phyid= '{}'".format(physioname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def updatePhysiotherepyData():
    dressing_id=request.form['physio_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_physiotherapy"

    try:
        if request.method == 'POST':
            dbcolumn.append('physiotherapy_date')
            dbcolumn.append('physiotherapy_name')
            dbcolumn.append('physiotherapy_amount')
            dbcolumn.append('physiotherapy_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(request.form['phydate'])
            htmlcolumn.append(request.form['physioname'])
            htmlcolumn.append(request.form[str('physio_amount')])
            htmlcolumn.append(request.form['physio_id']) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            print(result,"ooooooooooooooooooooooooooooo")
            return result
    except Exception as e:
        return str(e)

############################################### CHART UPDATE ENDS ######################################################

############################################### POISON UPDATE START #####################################################
def getPatientPoisonData(wmid):
    try:
        sql="select pos_id,wrd_id,pdate,TIME_FORMAT(ptime,'%H:%i'),pinjection,pdose,punit,pgivenby,pamount from ward_poision_chart where wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPoisonName(injection):
    try:
        sql="".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
############################################### POISON UPDATE START #####################################################

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


#This function will return entire row of patient_registration with respect to RegNo.
def getNewPatientVisit(regno):
    try:
        sql="select regno,pfname,pmname,psname,DATE_FORMAT(regdate,'%d/%m/%Y'),age,agetype,sex,education from patient_registration where regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#This function will return the status of patient with respect to RegNo.
def getANCMainData(regno):
    try:
        sql="select count(*),IFNULL(anc_status, 'NONE') from anc_main where regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getFilterCountANCData(regno):
    try:
        sql="select count(*) from anc_main where anc_status = 1 and regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function will insert new patient in ANC
def insertNewANCData():
    dbcolumn = []
    htmlcolumn = []
    tablename = "anc_main"
    result = ''
    if request.method == 'POST':
        try:
            dbcolumn.append('regno')
            dbcolumn.append('anc_date')

            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['anc_date'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
        except Exception as e:
            return str(e)

#This function will return the entire row from anc_main
def getAllANCData(regno):
    try:
        sql="select * from anc_main where regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getFilterAllANCData(regno):
    try:
        sql="select * from anc_main where anc_status=1 AND regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function will show the count of Patient History
def getAllPhCount(anc_id):
    try:
        sql="select count(*) from anc_patient_history where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchone()[0]
    except Exception as e:
        return str(e)

#This function will show the count of Gravida History
def getAllGhCount(anc_id):
    try:
        sql="select count(*) from anc_gravida_history where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchone()[0]
    except Exception as e:
        return str(e)

#This function will show the count of First Visit
def getAllFiVCount(anc_id):
    try:
        sql="select count(*) from anc_first_visit where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchone()[0]
    except Exception as e:
        return str(e)

#This function will show the count of Follow Up Visit
def getAllFoVCount(anc_id):
    try:
        sql="select count(*) from anc_followup_visit where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchone()[0]
    except Exception as e:
        return str(e)

#This function will show the count of Lab Check Up
def getAllLcCount(anc_id):
    try:
        sql="select count(*) from anc_lab_checkup where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchone()[0]
    except Exception as e:
        return str(e)

#This function will show the count of USG Report
def getAllUsgCount(anc_id):
    try:
        sql="select count(*) from anc_usg_report where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchone()[0]
    except Exception as e:
        return str(e)

#This function will deactivate the particular anc_id
def ANCIdDeactive(anc_id):
    anc_id = request.form['anc_id']
    dbcolumn = []
    htmlcolumn = []
    tablename = "anc_main"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('anc_status')
            dbcolumn.append('anc_id')  # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append("0")
            htmlcolumn.append(anc_id) # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#This function will insert a new record in table "anc_patient_history" for new patient.
def insertANCPatientHistory():
    anc_id= request.form['anc_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_patient_history"
    try:
            if request.method == 'POST':
                dbcolumn.append('anc_id')
                dbcolumn.append('ph_date')
                dbcolumn.append('ph_age')
                dbcolumn.append('duration')
                dbcolumn.append('cycle')
                dbcolumn.append('lmp')
                dbcolumn.append('edd')
                dbcolumn.append('occupation')
                dbcolumn.append('martial_status')
                dbcolumn.append('past_history')
                dbcolumn.append('family_history')
                dbcolumn.append('contraceptive_history')
                dbcolumn.append('ph_others')

                htmlcolumn.append(anc_id)
                htmlcolumn.append(request.form['ph_date'])
                htmlcolumn.append(request.form['ph_age'])
                htmlcolumn.append(request.form['duration'])
                htmlcolumn.append(request.form['cycle'])
                htmlcolumn.append(request.form['lmp'])
                htmlcolumn.append(request.form['edd'])
                htmlcolumn.append(request.form['occupation'])
                htmlcolumn.append(request.form['martial_status'])
                htmlcolumn.append(request.form['past_history'])
                htmlcolumn.append(request.form['family_history'])
                htmlcolumn.append(request.form['contraceptive_history'])
                htmlcolumn.append(request.form['ph_others'])

                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                if result == 1:
                    try:
                        sql="select count(*) from anc_patient_history where anc_id='{}'".format(anc_id)
                        cursor.execute(sql)
                        ph= str(cursor.fetchone()[0])
                        dbcolumn = []
                        htmlcolumn = []
                        result1=''
                        tablename = "anc_main"
                        dbcolumn.append('patient_history')
                        dbcolumn.append('anc_id')
                        htmlcolumn.append(ph)
                        htmlcolumn.append(anc_id)
                        result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                        return result1
                    except Exception as e:
                        return str(e)
    except Exception as e:
        return str(e)

#This function will insert a new record in table "anc_gravida_history" for new patient.
def insertANCGravidaHistory():
    anc_id= request.form['anc_id']
    tablename = "anc_gravida_history"
    dbcolumn = []
    htmlcolumn = []
    result=''
    rowno=len(request.form.getlist('dopa'))
    dopa = request.form.getlist('dopa') #Has Multiple Value
    dop = request.form.getlist('dop')  #Has Multiple Value
    aop = request.form.getlist('aop')  #Has Multiple Value
    lsch = request.form.getlist('lsch')  #Has Multiple Value
    delivery_type = request.form.getlist('delivery_type')  #Has Multiple Value
    no_babies = request.form.getlist('no_babies')  #Has Multiple Value
    baby_status = request.form.getlist('baby_status')  #Has Multiple Value
    puerperium = request.form.getlist('puerperium')  #Has Multiple Value
    childsex = request.form.getlist('childsex')  #Has Multiple Value
    baby_wt = request.form.getlist('baby_wt')  #Has Multiple Value
    brstfed_btlefed = request.form.getlist('brstfed_btlefed')  #Has Multiple Value
    gh_others = request.form.getlist('gh_others')  #Has Multiple Value

    try:
        if request.method == 'POST':
            for i in range(rowno):

                dbcolumn = []
                htmlcolumn = []

                dbcolumn.append('anc_id')
                dbcolumn.append('gh_date')
                dbcolumn.append('gravida')
                dbcolumn.append('parity_live')
                dbcolumn.append('dopa')
                dbcolumn.append('dop')
                dbcolumn.append('aop')
                dbcolumn.append('lsch')
                dbcolumn.append('delivery_type')
                dbcolumn.append('no_babies')
                dbcolumn.append('baby_status')
                dbcolumn.append('puerperium')
                dbcolumn.append('childsex')
                dbcolumn.append('baby_wt')
                dbcolumn.append('brstfed_btlefed')
                dbcolumn.append('gh_others')

                htmlcolumn.append(anc_id)
                htmlcolumn.append(request.form['gh_date'])
                htmlcolumn.append(request.form['gravida'])
                htmlcolumn.append(request.form['parity_live'])
                htmlcolumn.append(dopa[i])
                htmlcolumn.append(dop[i])
                htmlcolumn.append(aop[i])
                htmlcolumn.append(lsch[i])
                htmlcolumn.append(delivery_type[i])
                htmlcolumn.append(no_babies[i])
                htmlcolumn.append(baby_status[i])
                htmlcolumn.append(puerperium[i])
                htmlcolumn.append(childsex[i])
                htmlcolumn.append(baby_wt[i])
                htmlcolumn.append(brstfed_btlefed[i])
                htmlcolumn.append(gh_others[i])

                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            if result == 1:
                try:
                    sql="select count(*) from anc_gravida_history where anc_id='{}'".format(anc_id)
                    cursor.execute(sql)
                    gh= str(cursor.fetchone()[0])
                    dbcolumn = []
                    htmlcolumn = []
                    result1=''
                    tablename = "anc_main"
                    dbcolumn.append('gravida_history')
                    dbcolumn.append('anc_id')
                    htmlcolumn.append(gh)
                    htmlcolumn.append(anc_id)
                    result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    return result1
                except Exception as e:
                    return str(e)
    except Exception as e:
        return str(e)



#This function will insert a new record in table "anc_first_visit" for new patient.
def insertANCFirstVisit():
    anc_id= request.form['anc_id']
    dbcolumn = []
    htmlcolumn = []
    tablename = "anc_first_visit"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('anc_id')
            dbcolumn.append('FiV_seen_doctor')
            dbcolumn.append('FiV_seen_sister')
            dbcolumn.append('FiV_date')
            dbcolumn.append('FiV_wt')
            dbcolumn.append('FiV_ht')
            dbcolumn.append('FiV_bmi')
            dbcolumn.append('FiV_systolic')
            dbcolumn.append('FiV_diastolic')
            dbcolumn.append('FiV_pulse')
            dbcolumn.append('FiV_heart')
            dbcolumn.append('FiV_lungs')
            dbcolumn.append('FiV_breast')
            dbcolumn.append('FiV_anaemia')
            dbcolumn.append('FiV_jaundice')
            dbcolumn.append('FiV_tongue')
            dbcolumn.append('FiV_thyroid')
            dbcolumn.append('FiV_neckglds')
            dbcolumn.append('FiV_teeth')
            dbcolumn.append('FiV_gum')
            dbcolumn.append('FiV_throat')
            dbcolumn.append('FiV_kidneys')
            dbcolumn.append('FiV_oedema')
            dbcolumn.append('FiV_spleen')
            dbcolumn.append('FiV_liver')
            dbcolumn.append('FiV_variveins')
            dbcolumn.append('FiV_pallor')
            dbcolumn.append('FiV_icterus')
            dbcolumn.append('FiV_others')

            htmlcolumn.append(anc_id)
            htmlcolumn.append(request.form['FiV_seen_doctor'])
            htmlcolumn.append(request.form['FiV_seen_sister'])
            htmlcolumn.append(request.form['FiV_date'])
            htmlcolumn.append(request.form['FiV_wt'])
            htmlcolumn.append(request.form['FiV_ht'])
            htmlcolumn.append(request.form['FiV_bmi'])
            htmlcolumn.append(request.form['FiV_systolic'])
            htmlcolumn.append(request.form['FiV_diastolic'])
            htmlcolumn.append(request.form['FiV_pulse'])
            htmlcolumn.append(request.form['FiV_heart'])
            htmlcolumn.append(request.form['FiV_lungs'])
            htmlcolumn.append(request.form['FiV_breast'])
            htmlcolumn.append(request.form['FiV_anaemia'])
            htmlcolumn.append(request.form['FiV_jaundice'])
            htmlcolumn.append(request.form['FiV_tongue'])
            htmlcolumn.append(request.form['FiV_thyroid'])
            htmlcolumn.append(request.form['FiV_neckglds'])
            htmlcolumn.append(request.form['FiV_teeth'])
            htmlcolumn.append(request.form['FiV_gum'])
            htmlcolumn.append(request.form['FiV_throat'])
            htmlcolumn.append(request.form['FiV_kidneys'])
            htmlcolumn.append(request.form['FiV_oedema'])
            htmlcolumn.append(request.form['FiV_spleen'])
            htmlcolumn.append(request.form['FiV_liver'])
            htmlcolumn.append(request.form['FiV_variveins'])
            htmlcolumn.append(request.form['FiV_pallor'])
            htmlcolumn.append(request.form['FiV_icterus'])
            htmlcolumn.append(request.form['FiV_others'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            if result == 1:
                try:
                    sql="select count(*) from anc_first_visit where anc_id='{}'".format(anc_id)
                    cursor.execute(sql)
                    fiv= str(cursor.fetchone()[0])
                    dbcolumn = []
                    htmlcolumn = []
                    result1=''
                    tablename = "anc_main"
                    dbcolumn.append('first_visit')
                    dbcolumn.append('anc_id')
                    htmlcolumn.append(fiv)
                    htmlcolumn.append(anc_id)
                    result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    return result1
                except Exception as e:
                    return str(e)
    except Exception as e:
        return str(e)


#This function will insert a new record in table "anc_followup_visit" for new patient.
def insertANCFollowUpVisit():
    anc_id= request.form['anc_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_followup_visit"
    rowno=int(request.form['FoV_no_foetus'])
    fhs = request.form.getlist('FoV_fhs') #Has Multiple Value
    fhs_val=  ",".join(fhs)
    try:
        if request.method == 'POST':
            dbcolumn.append('anc_id')
            dbcolumn.append('FoV_seen_doctor')
            dbcolumn.append('FoV_seen_sister')
            dbcolumn.append('FoV_date')
            dbcolumn.append('FoV_wt')
            dbcolumn.append('FoV_ht')
            dbcolumn.append('FoV_bmi')
            dbcolumn.append('FoV_systolic')
            dbcolumn.append('FoV_diastolic')
            dbcolumn.append('FoV_pulse')
            dbcolumn.append('FoV_bodytemp')
            dbcolumn.append('FoV_resprate')
            dbcolumn.append('FoV_utsize')
            dbcolumn.append('FoV_oedema')
            dbcolumn.append('FoV_no_foetus')
            dbcolumn.append('FoV_fhs')
            dbcolumn.append('FoV_pallor')
            dbcolumn.append('FoV_cyanosis')
            dbcolumn.append('FoV_icterus')
            dbcolumn.append('FoV_variveins')
            dbcolumn.append('FoV_immstatus')
            dbcolumn.append('FoV_others')

            htmlcolumn.append(anc_id)
            htmlcolumn.append(request.form['FoV_seen_doctor'])
            htmlcolumn.append(request.form['FoV_seen_sister'])
            htmlcolumn.append(request.form['FoV_date'])
            htmlcolumn.append(request.form['FoV_wt'])
            htmlcolumn.append(request.form['FoV_ht'])
            htmlcolumn.append(request.form['FoV_bmi'])
            htmlcolumn.append(request.form['FoV_systolic'])
            htmlcolumn.append(request.form['FoV_diastolic'])
            htmlcolumn.append(request.form['FoV_pulse'])
            htmlcolumn.append(request.form['FoV_bodytemp'])
            htmlcolumn.append(request.form['FoV_resprate'])
            htmlcolumn.append(request.form['FoV_utsize'])
            htmlcolumn.append(request.form['FoV_oedema'])
            htmlcolumn.append(request.form['FoV_no_foetus'])
            htmlcolumn.append(fhs_val)
            htmlcolumn.append(request.form['FoV_pallor'])
            htmlcolumn.append(request.form['FoV_cyanosis'])
            htmlcolumn.append(request.form['FoV_icterus'])
            htmlcolumn.append(request.form['FoV_variveins'])
            htmlcolumn.append(request.form['FoV_immstatus'])
            htmlcolumn.append(request.form['FoV_others'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            if result == 1:
                try:
                    sql="select count(*) from anc_followup_visit where anc_id='{}'".format(anc_id)
                    cursor.execute(sql)
                    fov= str(cursor.fetchone()[0])
                    dbcolumn = []
                    htmlcolumn = []
                    result1=''
                    tablename = "anc_main"
                    dbcolumn.append('follow_visit')
                    dbcolumn.append('anc_id')
                    htmlcolumn.append(fov)
                    htmlcolumn.append(anc_id)
                    result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    return result1
                except Exception as e:
                    return str(e)
    except Exception as e:
        return str(e)


#This function will insert a new record in table "anc_lab_checkup" for new patient.
def insertANCLabCheckUp():
    anc_id= request.form['anc_id']
    dbcolumn = []
    htmlcolumn = []
    tablename = "anc_lab_checkup"
    result=''
    try:
        if request.method == 'POST':

            dbcolumn.append('anc_id')
            dbcolumn.append('lc_date')
            dbcolumn.append('lc_testdone')
            dbcolumn.append('lc_sugar')
            dbcolumn.append('lc_albumin')
            dbcolumn.append('lc_microscopy')
            dbcolumn.append('lc_hb')
            dbcolumn.append('lc_bldgrp')
            dbcolumn.append('lc_sickling')
            dbcolumn.append('lc_vdrl')
            dbcolumn.append('lc_hbsag')
            dbcolumn.append('lc_hiv')
            dbcolumn.append('lc_rbs')
            dbcolumn.append('lc_tsh')
            dbcolumn.append('lc_others')

            htmlcolumn.append(anc_id)
            htmlcolumn.append(request.form['lc_date'])
            htmlcolumn.append(request.form['lc_testdone'])
            htmlcolumn.append(request.form['lc_sugar'])
            htmlcolumn.append(request.form['lc_albumin'])
            htmlcolumn.append(request.form['lc_microscopy'])
            htmlcolumn.append(request.form['lc_hb'])
            htmlcolumn.append(request.form['lc_bldgrp'])
            htmlcolumn.append(request.form['lc_sickling'])
            htmlcolumn.append(request.form['lc_vdrl'])
            htmlcolumn.append(request.form['lc_hbsag'])
            htmlcolumn.append(request.form['lc_hiv'])
            htmlcolumn.append(request.form['lc_rbs'])
            htmlcolumn.append(request.form['lc_tsh'])
            htmlcolumn.append(request.form['lc_others'])

# Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            if result == 1:
                try:
                    sql="select count(*) from anc_lab_checkup where anc_id='{}'".format(anc_id)
                    cursor.execute(sql)
                    lc= str(cursor.fetchone()[0])
                    dbcolumn = []
                    htmlcolumn = []
                    result1=''
                    tablename = "anc_main"
                    dbcolumn.append('lab_checkup')
                    dbcolumn.append('anc_id')
                    htmlcolumn.append(lc)
                    htmlcolumn.append(anc_id)
                    result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    return result1
                except Exception as e:
                    return str(e)
    except Exception as e:
        return str(e)


#This function will insert a new record in table "anc_usg_report" for new patient.
def insertANCUsgReport():
    anc_id= request.form['anc_id']
    usg_foetus=request.form['usg_foetus']
    usg_presentation=request.form['usg_presentation']
    usg_placenta=request.form['usg_placenta']
    usg_liquor=request.form['usg_liquor']
    dbcolumn = []
    htmlcolumn = []
    tablename = "anc_usg_report"
    result=''
    try:
        if request.method == 'POST':

            dbcolumn.append('anc_id')
            dbcolumn.append('usg_date')
            dbcolumn.append('usg_testdone')
            dbcolumn.append('usg_gravida')
            dbcolumn.append('usg_lmp')
            dbcolumn.append('usg_edd')
            dbcolumn.append('usg_foetus')
            dbcolumn.append('usg_presentation')
            dbcolumn.append('usg_placenta')
            dbcolumn.append('usg_liquor')
            dbcolumn.append('usg_crl')
            dbcolumn.append('usg_fa1')
            dbcolumn.append('usg_edd1')
            dbcolumn.append('usg_bpd')
            dbcolumn.append('usg_fa2')
            dbcolumn.append('usg_edd2')
            dbcolumn.append('usg_hc')
            dbcolumn.append('usg_fa3')
            dbcolumn.append('usg_edd3')
            dbcolumn.append('usg_ac')
            dbcolumn.append('usg_fa4')
            dbcolumn.append('usg_edd4')
            dbcolumn.append('usg_fl')
            dbcolumn.append('usg_fa5')
            dbcolumn.append('usg_edd5')
            dbcolumn.append('usg_fa6')
            dbcolumn.append('usg_edd6')
            dbcolumn.append('usg_fhr')
            dbcolumn.append('usg_fwt')
            dbcolumn.append('usg_hc_ae')
            dbcolumn.append('usg_fl_he')
            dbcolumn.append('usg_fl_ae')
            dbcolumn.append('usg_others')


            htmlcolumn.append(anc_id)
            htmlcolumn.append(request.form['usg_date'])
            htmlcolumn.append(request.form['usg_testdone'])
            htmlcolumn.append(request.form['usg_gravida'])
            htmlcolumn.append(request.form['usg_lmp'])
            htmlcolumn.append(request.form['usg_edd'])

            if usg_foetus=='Others':
                htmlcolumn.append(str(request.form['otherFoetus']))
            else:
                htmlcolumn.append(str(request.form['usg_foetus']))

            if usg_presentation=='Others':
                htmlcolumn.append(str(request.form['otherPresentation']))
            else:
                htmlcolumn.append(str(request.form['usg_presentation']))

            if usg_placenta=='Others':
                htmlcolumn.append(str(request.form['otherPlacenta']))
            else:
                htmlcolumn.append(str(request.form['usg_placenta']))

            if usg_liquor=='Others':
                htmlcolumn.append(str(request.form['otherLiquor']))
            else:
                htmlcolumn.append(str(request.form['usg_liquor']))

            htmlcolumn.append(request.form['usg_crl'])
            htmlcolumn.append(request.form['usg_fa1'])
            htmlcolumn.append(request.form['usg_edd1'])
            htmlcolumn.append(request.form['usg_bpd'])
            htmlcolumn.append(request.form['usg_fa2'])
            htmlcolumn.append(request.form['usg_edd2'])
            htmlcolumn.append(request.form['usg_hc'])
            htmlcolumn.append(request.form['usg_fa3'])
            htmlcolumn.append(request.form['usg_edd3'])
            htmlcolumn.append(request.form['usg_ac'])
            htmlcolumn.append(request.form['usg_fa4'])
            htmlcolumn.append(request.form['usg_edd4'])
            htmlcolumn.append(request.form['usg_fl'])
            htmlcolumn.append(request.form['usg_fa5'])
            htmlcolumn.append(request.form['usg_edd5'])
            htmlcolumn.append(request.form['usg_fa6'])
            htmlcolumn.append(request.form['usg_edd6'])
            htmlcolumn.append(request.form['usg_fhr'])
            htmlcolumn.append(request.form['usg_fwt'])
            htmlcolumn.append(request.form['usg_hc_ae'])
            htmlcolumn.append(request.form['usg_fl_he'])
            htmlcolumn.append(request.form['usg_fl_ae'])
            htmlcolumn.append(request.form['usg_others'])

# Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            if result == 1:
                try:
                    sql="select count(*) from anc_usg_report where anc_id='{}'".format(anc_id)
                    cursor.execute(sql)
                    usg= str(cursor.fetchone()[0])
                    dbcolumn = []
                    htmlcolumn = []
                    result1=''
                    tablename = "anc_main"
                    dbcolumn.append('usg_report')
                    dbcolumn.append('anc_id')
                    htmlcolumn.append(usg)
                    htmlcolumn.append(anc_id)
                    result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                    return result1
                except Exception as e:
                    return str(e)
    except Exception as e:
        return str(e)


#This function will fetch the current id of Lab for Print
def GetANClcid():
    try:
        sql="select lc_id from anc_lab_checkup order by lc_id desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)


#This function will fetch the current id of Lab for Print
def GetANCusgid():
    try:
        sql="select usg_id from anc_usg_report order by usg_id desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

#This function will fetch the current data of Lab for Print
def ANCUsgPrint(usg_id):
    usg_id=request.form['usg_id']
    try:
        sql="select p.regno,pfname,pmname,psname,sex,age,agetype,regdate,address,contactno,o.regno,complaint,a.regno,a.anc_id,anc_date, usg_id,usg.anc_id,DATE_FORMAT(usg_date,'%d/%m/%Y'),usg_testdone,usg_gravida,usg_lmp,usg_edd,usg_foetus,usg_presentation,usg_placenta,usg_liquor,usg_crl,usg_fa1,usg_edd1,usg_bpd,usg_fa2,usg_edd2,usg_hc,usg_fa3,usg_edd3,usg_ac,usg_fa4,usg_edd4,usg_fl,usg_fa5,usg_edd5,usg_fa6,usg_edd6,usg_fhr,usg_fwt,usg_hc_ae,usg_fl_he,usg_fl_ae,usg_others from patient_registration p,opdvisit o,anc_main a,anc_usg_report usg where p.regno=o.regno and p.regno=a.regno and a.anc_id=usg.anc_id and usg_id='{}' order by usg_date desc limit 1".format(usg_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

################################################################################

###=================== ANC View Update ======================================###

#This function will fetch the required regno and check its status in anc for a patient.
def getANCView_Update(regno):
    try:
        sql="select p.regno,pfname,pmname,psname,DATE_FORMAT(regdate,'%d/%m/%Y'),age,agetype,sex,education,anc_id,patient_history,gravida_history,first_visit,follow_visit,lab_checkup,usg_report,anc_status from patient_registration p,anc_main a where a.regno=p.regno and anc_status=1 and p.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function is for viewing Patient's History in ANC.
def getANCPhView_Update(anc_id):
    try:
        sql="select * from anc_patient_history where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#This function is for viewing Patient's Gravida History in ANC.
def getANCGhView_Update(anc_id):
    try:
        sql="select * from anc_gravida_history where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function is for viewing First Visit of a Patient in ANC.
def getANCFiVView_Update(anc_id):
    try:
        sql="select * from anc_first_visit where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function is for viewing Follow Up Visit in ANC.
def getANCFoVView_Update(anc_id):
    try:
        sql="select * from anc_followup_visit where anc_id='{}' order by FoV_date desc".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function is for viewing Lab Check Up in ANC.
def getANCLcView_Update(anc_id):
    try:
        sql="select * from anc_lab_checkup where anc_id='{}' order by lc_date desc".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function is for viewing USG Report in ANC.
def getANCUsrView_Update(anc_id):
    try:
        sql="select * from anc_usg_report where anc_id='{}' order by usg_date desc".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function is for Updating Patient's History in ANC.

def updateANCPatientHistory():
    ph_id = request.form['ph_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_patient_history"
    try:
        if request.method == 'POST':

            #Name of database Attribute
            dbcolumn.append('ph_date')
            dbcolumn.append('ph_age')
            dbcolumn.append('duration')
            dbcolumn.append('cycle')
            dbcolumn.append('lmp')
            dbcolumn.append('edd')
            dbcolumn.append('occupation')
            dbcolumn.append('martial_status')
            dbcolumn.append('past_history')
            dbcolumn.append('family_history')
            dbcolumn.append('contraceptive_history')
            dbcolumn.append('ph_others')
            dbcolumn.append('ph_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(request.form['ph_date'])
            htmlcolumn.append(request.form['ph_age'])
            htmlcolumn.append(request.form['duration'])
            htmlcolumn.append(request.form['cycle'])
            htmlcolumn.append(request.form['lmp'])
            htmlcolumn.append(request.form['edd'])
            htmlcolumn.append(request.form['occupation'])
            htmlcolumn.append(request.form['martial_status'])
            htmlcolumn.append(request.form['past_history'])
            htmlcolumn.append(request.form['family_history'])
            htmlcolumn.append(request.form['contraceptive_history'])
            htmlcolumn.append(request.form['ph_others'])
            htmlcolumn.append(ph_id) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#This function is for Updating Patient's Gravida History in ANC.
def updateANCGravidaHistory():
    gh_id = request.form['gh_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_gravida_history"
    try:
        if request.method == 'POST':

            #Name of database Attribute
            dbcolumn.append('gh_date')
            dbcolumn.append('gravida')
            dbcolumn.append('parity_live')
            dbcolumn.append('dopa')
            dbcolumn.append('dop')
            dbcolumn.append('aop')
            dbcolumn.append('lsch')
            dbcolumn.append('delivery_type')
            dbcolumn.append('no_babies')
            dbcolumn.append('baby_status')
            dbcolumn.append('puerperium')
            dbcolumn.append('childsex')
            dbcolumn.append('baby_wt')
            dbcolumn.append('brstfed_btlefed')
            dbcolumn.append('gh_others')
            dbcolumn.append('gh_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            htmlcolumn.append(request.form['gh_date'])
            htmlcolumn.append(request.form['gravida'])
            htmlcolumn.append(request.form['parity_live'])
            htmlcolumn.append(request.form['dopa'])
            htmlcolumn.append(request.form['dop'])
            htmlcolumn.append(request.form['aop'])
            htmlcolumn.append(request.form['lsch'])
            htmlcolumn.append(request.form['delivery_type'])
            htmlcolumn.append(request.form['no_babies'])
            htmlcolumn.append(request.form['baby_status'])
            htmlcolumn.append(request.form['puerperium'])
            htmlcolumn.append(request.form['childsex'])
            htmlcolumn.append(request.form['baby_wt'])
            htmlcolumn.append(request.form['brstfed_btlefed'])
            htmlcolumn.append(request.form['gh_others'])
            htmlcolumn.append(gh_id) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#This function is for deleting row from table in ANC Gravida History
def ANCGravidaDeleteRow(gh_id):
    try:
        if request.method == 'POST':
            sql="delete from anc_gravida_history where gh_id='{}'".format(gh_id)
            cursor.execute(sql)
            db.commit()
            return "SUCCESSFULLY DELETED."
    except Exception as e:
        return str(e)

#This function is for Updating Patient's First Visit in ANC.

def updateANCFirstVisit():
    FiV_id = request.form['FiV_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_first_visit"
    try:
        if request.method == 'POST':

            #Name of database Attribute
            dbcolumn.append('FiV_seen_doctor')
            dbcolumn.append('FiV_seen_sister')
            dbcolumn.append('FiV_date')
            dbcolumn.append('FiV_wt')
            dbcolumn.append('FiV_ht')
            dbcolumn.append('FiV_bmi')
            dbcolumn.append('FiV_systolic')
            dbcolumn.append('FiV_diastolic')
            dbcolumn.append('FiV_pulse')
            dbcolumn.append('FiV_heart')
            dbcolumn.append('FiV_lungs')
            dbcolumn.append('FiV_breast')
            dbcolumn.append('FiV_anaemia')
            dbcolumn.append('FiV_jaundice')
            dbcolumn.append('FiV_tongue')
            dbcolumn.append('FiV_thyroid')
            dbcolumn.append('FiV_neckglds')
            dbcolumn.append('FiV_teeth')
            dbcolumn.append('FiV_gum')
            dbcolumn.append('FiV_throat')
            dbcolumn.append('FiV_kidneys')
            dbcolumn.append('FiV_oedema')
            dbcolumn.append('FiV_spleen')
            dbcolumn.append('FiV_liver')
            dbcolumn.append('FiV_variveins')
            dbcolumn.append('FiV_pallor')
            dbcolumn.append('FiV_icterus')
            dbcolumn.append('FiV_others')
            dbcolumn.append('FiV_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            htmlcolumn.append(request.form['FiV_seen_doctor'])
            htmlcolumn.append(request.form['FiV_seen_sister'])
            htmlcolumn.append(request.form['FiV_date'])
            htmlcolumn.append(request.form['FiV_wt'])
            htmlcolumn.append(request.form['FiV_ht'])
            htmlcolumn.append(request.form['FiV_bmi'])
            htmlcolumn.append(request.form['FiV_systolic'])
            htmlcolumn.append(request.form['FiV_diastolic'])
            htmlcolumn.append(request.form['FiV_pulse'])
            htmlcolumn.append(request.form['FiV_heart'])
            htmlcolumn.append(request.form['FiV_lungs'])
            htmlcolumn.append(request.form['FiV_breast'])
            htmlcolumn.append(request.form['FiV_anaemia'])
            htmlcolumn.append(request.form['FiV_jaundice'])
            htmlcolumn.append(request.form['FiV_tongue'])
            htmlcolumn.append(request.form['FiV_thyroid'])
            htmlcolumn.append(request.form['FiV_neckglds'])
            htmlcolumn.append(request.form['FiV_teeth'])
            htmlcolumn.append(request.form['FiV_gum'])
            htmlcolumn.append(request.form['FiV_throat'])
            htmlcolumn.append(request.form['FiV_kidneys'])
            htmlcolumn.append(request.form['FiV_oedema'])
            htmlcolumn.append(request.form['FiV_spleen'])
            htmlcolumn.append(request.form['FiV_liver'])
            htmlcolumn.append(request.form['FiV_variveins'])
            htmlcolumn.append(request.form['FiV_pallor'])
            htmlcolumn.append(request.form['FiV_icterus'])
            htmlcolumn.append(request.form['FiV_others'])
            htmlcolumn.append(FiV_id) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#This function is for Updating Patient's Follow Up Visit in ANC.

def updateANCFollowupVisit():
    FoV_id = request.form['FoV_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_followup_visit"
    #rowno=int(request.form['FoV_no_foetus'])
    #fhs = request.form.getlist('FoV_fhs') #Has Multiple Value
    #print(fhs)
    #fhs_val=  ",".join(fhs)
    #print(fhs_val)
    try:
        if request.method == 'POST':

            #Name of database Attribute
            dbcolumn.append('FoV_seen_doctor')
            dbcolumn.append('FoV_seen_sister')
            dbcolumn.append('FoV_date')
            dbcolumn.append('FoV_wt')
            dbcolumn.append('FoV_ht')
            dbcolumn.append('FoV_bmi')
            dbcolumn.append('FoV_systolic')
            dbcolumn.append('FoV_diastolic')
            dbcolumn.append('FoV_pulse')
            dbcolumn.append('FoV_bodytemp')
            dbcolumn.append('FoV_resprate')
            dbcolumn.append('FoV_utsize')
            dbcolumn.append('FoV_oedema')
            dbcolumn.append('FoV_no_foetus')
            dbcolumn.append('FoV_fhs')
            dbcolumn.append('FoV_pallor')
            dbcolumn.append('FoV_cyanosis')
            dbcolumn.append('FoV_icterus')
            dbcolumn.append('FoV_variveins')
            dbcolumn.append('FoV_immstatus')
            dbcolumn.append('FoV_others')
            dbcolumn.append('FoV_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"


            htmlcolumn.append(request.form['FoV_seen_doctor'])
            htmlcolumn.append(request.form['FoV_seen_sister'])
            htmlcolumn.append(request.form['FoV_date'])
            htmlcolumn.append(request.form['FoV_wt'])
            htmlcolumn.append(request.form['FoV_ht'])
            htmlcolumn.append(request.form['FoV_bmi'])
            htmlcolumn.append(request.form['FoV_systolic'])
            htmlcolumn.append(request.form['FoV_diastolic'])
            htmlcolumn.append(request.form['FoV_pulse'])
            htmlcolumn.append(request.form['FoV_bodytemp'])
            htmlcolumn.append(request.form['FoV_resprate'])
            htmlcolumn.append(request.form['FoV_utsize'])
            htmlcolumn.append(request.form['FoV_oedema'])
            htmlcolumn.append(request.form['FoV_no_foetus'])
            htmlcolumn.append(request.form['FoV_fhs'])
            htmlcolumn.append(request.form['FoV_pallor'])
            htmlcolumn.append(request.form['FoV_cyanosis'])
            htmlcolumn.append(request.form['FoV_icterus'])
            htmlcolumn.append(request.form['FoV_variveins'])
            htmlcolumn.append(request.form['FoV_immstatus'])
            htmlcolumn.append(request.form['FoV_others'])
            htmlcolumn.append(FoV_id)


            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#This function is for Updating Patient's Lab Check Up in ANC.

def updateANCLabCheckUpVisit():
    lc_id = request.form['lc_id']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_lab_checkup"
    try:
        if request.method == 'POST':

            #Name of database Attribute
            dbcolumn.append('lc_date')
            dbcolumn.append('lc_testdone')
            dbcolumn.append('lc_sugar')
            dbcolumn.append('lc_albumin')
            dbcolumn.append('lc_microscopy')
            dbcolumn.append('lc_hb')
            dbcolumn.append('lc_bldgrp')
            dbcolumn.append('lc_sickling')
            dbcolumn.append('lc_vdrl')
            dbcolumn.append('lc_hbsag')
            dbcolumn.append('lc_hiv')
            dbcolumn.append('lc_rbs')
            dbcolumn.append('lc_tsh')
            dbcolumn.append('lc_others')
            dbcolumn.append('lc_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            htmlcolumn.append(request.form['lc_date'])
            htmlcolumn.append(request.form['lc_testdone'])
            htmlcolumn.append(request.form['lc_sugar'])
            htmlcolumn.append(request.form['lc_albumin'])
            htmlcolumn.append(request.form['lc_microscopy'])
            htmlcolumn.append(request.form['lc_hb'])
            htmlcolumn.append(request.form['lc_bldgrp'])
            htmlcolumn.append(request.form['lc_sickling'])
            htmlcolumn.append(request.form['lc_vdrl'])
            htmlcolumn.append(request.form['lc_hbsag'])
            htmlcolumn.append(request.form['lc_hiv'])
            htmlcolumn.append(request.form['lc_rbs'])
            htmlcolumn.append(request.form['lc_tsh'])
            htmlcolumn.append(request.form['lc_others'])
            htmlcolumn.append(lc_id) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def updateANCUsgReportVisit():
    usg_id = request.form['usg_id']
    usg_foetus=request.form['usg_foetus']
    usg_presentation=request.form['usg_presentation']
    usg_placenta=request.form['usg_placenta']
    usg_liquor=request.form['usg_liquor']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "anc_usg_report"
    try:
        if request.method == 'POST':

            #Name of database Attribute
            dbcolumn.append('usg_date')
            dbcolumn.append('usg_testdone')
            dbcolumn.append('usg_gravida')
            dbcolumn.append('usg_lmp')
            dbcolumn.append('usg_edd')
            dbcolumn.append('usg_foetus')
            dbcolumn.append('usg_presentation')
            dbcolumn.append('usg_placenta')
            dbcolumn.append('usg_liquor')
            dbcolumn.append('usg_crl')
            dbcolumn.append('usg_fa1')
            dbcolumn.append('usg_edd1')
            dbcolumn.append('usg_bpd')
            dbcolumn.append('usg_fa2')
            dbcolumn.append('usg_edd2')
            dbcolumn.append('usg_hc')
            dbcolumn.append('usg_fa3')
            dbcolumn.append('usg_edd3')
            dbcolumn.append('usg_ac')
            dbcolumn.append('usg_fa4')
            dbcolumn.append('usg_edd4')
            dbcolumn.append('usg_fl')
            dbcolumn.append('usg_fa5')
            dbcolumn.append('usg_edd5')
            dbcolumn.append('usg_fa6')
            dbcolumn.append('usg_edd6')
            dbcolumn.append('usg_fhr')
            dbcolumn.append('usg_fwt')
            dbcolumn.append('usg_hc_ae')
            dbcolumn.append('usg_fl_he')
            dbcolumn.append('usg_fl_ae')
            dbcolumn.append('usg_others')
            dbcolumn.append('usg_id') # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"


            htmlcolumn.append(request.form['usg_date'])
            htmlcolumn.append(request.form['usg_testdone'])
            htmlcolumn.append(request.form['usg_gravida'])
            htmlcolumn.append(request.form['usg_lmp'])
            htmlcolumn.append(request.form['usg_edd'])

            if usg_foetus=='Others':
                htmlcolumn.append(str(request.form['otherFoetus']))
            else:
                htmlcolumn.append(str(request.form['usg_foetus']))

            if usg_presentation=='Others':
                htmlcolumn.append(str(request.form['otherPresentation']))
            else:
                htmlcolumn.append(str(request.form['usg_presentation']))

            if usg_placenta=='Others':
                htmlcolumn.append(str(request.form['otherPlacenta']))
            else:
                htmlcolumn.append(str(request.form['usg_placenta']))

            if usg_liquor=='Others':
                htmlcolumn.append(str(request.form['otherLiquor']))
            else:
                htmlcolumn.append(str(request.form['usg_liquor']))

            htmlcolumn.append(request.form['usg_crl'])
            htmlcolumn.append(request.form['usg_fa1'])
            htmlcolumn.append(request.form['usg_edd1'])
            htmlcolumn.append(request.form['usg_bpd'])
            htmlcolumn.append(request.form['usg_fa2'])
            htmlcolumn.append(request.form['usg_edd2'])
            htmlcolumn.append(request.form['usg_hc'])
            htmlcolumn.append(request.form['usg_fa3'])
            htmlcolumn.append(request.form['usg_edd3'])
            htmlcolumn.append(request.form['usg_ac'])
            htmlcolumn.append(request.form['usg_fa4'])
            htmlcolumn.append(request.form['usg_edd4'])
            htmlcolumn.append(request.form['usg_fl'])
            htmlcolumn.append(request.form['usg_fa5'])
            htmlcolumn.append(request.form['usg_edd5'])
            htmlcolumn.append(request.form['usg_fa6'])
            htmlcolumn.append(request.form['usg_edd6'])
            htmlcolumn.append(request.form['usg_fhr'])
            htmlcolumn.append(request.form['usg_fwt'])
            htmlcolumn.append(request.form['usg_hc_ae'])
            htmlcolumn.append(request.form['usg_fl_he'])
            htmlcolumn.append(request.form['usg_fl_ae'])
            htmlcolumn.append(request.form['usg_others'])
            htmlcolumn.append(usg_id) # The column name on the basis of which we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

################################################################################

###===================== ANC Search =========================================###

#This function will search ANC patient by Registration No.
def ANCSearchReg(regno):
    #regno=request.form['regno']
    try:
        sql="select r.regno,pfname,pmname,psname,age,agetype,DATE_FORMAT(regdate,'%d/%m/%Y'),DATE_FORMAT(anc_date,'%d/%m/%Y'),anc_id,anc_status from patient_registration r,anc_main a where r.regno=a.regno and anc_status=1 and r.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#This function will search ANC patient by Date.
def ANCSearchDate(frmdate,todate,ancgen):
    ancgen=ancgen+"ancgen.xlsx"
    frmdate=request.form['frmdate']
    todate=request.form['todate']
    try:
        sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),a.follow_visit from patient_registration r,anc_main a where r.regno=a.regno and anc_status=1 and r.regdate between '{}' and '{}'".format(frmdate,todate)
        cursor.execute(sql)
        q=cursor.fetchall()

        workbook = Workbook(ancgen)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'green'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"SURNAME",cell_format)
        sheet.write(0,4,"AGE",cell_format)
        sheet.write(0,5,"AGETYPE",cell_format)
        sheet.write(0,6,"SEX",cell_format)
        sheet.write(0,7,"RELATION",cell_format)
        sheet.write(0,8,"RELATIVE'S NAME",cell_format)
        sheet.write(0,9,"RELATIVE'S MIDDLE NAME",cell_format)
        sheet.write(0,10,"RELATIVE'S SURNAME",cell_format)
        sheet.write(0,11,"EDUCATION",cell_format)
        sheet.write(0,12,"REG.DATE",cell_format)
        sheet.write(0,13,"ADDRESS",cell_format)
        sheet.write(0,14,"ANC VISIT DATE",cell_format)
        sheet.write(0,15,"NO. OF VISITS",cell_format)

        for r, row in enumerate(q):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return q
    except Exception as e:
        return str(e)

#This function will search ANC patient by Immunization Status.
def ANCSearchImmu(ancimm):
    try:
        frmdate=request.form['frmdate']
        todate=request.form['todate']
        immustatus=request.form['immustatus']
        ancimm=ancimm+"ancimm.xlsx"

        if(immustatus == 'All'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),FoV_bodytemp,FoV_utsize,FoV_oedema,FoV_variveins,FoV_immstatus from patient_registration r,anc_main a,anc_followup_visit fv where r.regno=a.regno and a.anc_id=fv.anc_id and anc_status=1 and r.regdate between '{}' and '{}'".format(frmdate,todate)

        else:
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),FoV_bodytemp,FoV_utsize,FoV_oedema,FoV_variveins,FoV_immstatus from patient_registration r,anc_main a,anc_followup_visit fv where r.regno=a.regno and a.anc_id=fv.anc_id and anc_status=1 and r.regdate between '{}' and '{}' and fv.FoV_immstatus='{}'".format(frmdate,todate,immustatus)

        cursor.execute(sql)
        p=cursor.fetchall()

        workbook = Workbook(ancimm)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'magenta'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"SURNAME",cell_format)
        sheet.write(0,4,"AGE",cell_format)
        sheet.write(0,5,"AGETYPE",cell_format)
        sheet.write(0,6,"SEX",cell_format)
        sheet.write(0,7,"RELATION",cell_format)
        sheet.write(0,8,"RELATIVE'S NAME",cell_format)
        sheet.write(0,9,"RELATIVE'S MIDDLE NAME",cell_format)
        sheet.write(0,10,"RELATIVE'S SURNAME",cell_format)
        sheet.write(0,11,"EDUCATION",cell_format)
        sheet.write(0,12,"REG.DATE",cell_format)
        sheet.write(0,13,"ADDRESS",cell_format)
        sheet.write(0,14,"ANC VISIT DATE",cell_format)
        sheet.write(0,15,"BODY TEMPERATURE",cell_format)
        sheet.write(0,16,"UTERUS SIZE",cell_format)
        sheet.write(0,17,"OEDEMA",cell_format)
        sheet.write(0,18,"VARICOSE VEINS",cell_format)
        sheet.write(0,19,"IMMUNIZATION STATUS",cell_format)

        for r, row in enumerate(p):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return p
    except Exception as e:
        return str(e)


#This function will search ANC patient by Haemoglobin.
def ANCSearchHb(anchb):
    try:
        frmdate=request.form['frmdate']
        todate=request.form['todate']
        hb=float(request.form['hb'])
        blood=request.form['blood']
        anchb=anchb+"anchb.xlsx"


        if(frmdate != '' and todate != '' and hb != '' and blood =='Exact'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),lc_hb,lc_bldgrp,lc_sickling,lc_tsh from patient_registration r,anc_main a,anc_lab_checkup lc where r.regno=a.regno and a.anc_id=lc.anc_id and a.anc_status=1 and regdate between '{}' and '{}'and CAST(lc.lc_hb AS DECIMAL(10,2))='{}'".format(frmdate,todate,hb)

        elif(frmdate != '' and todate != '' and hb != '' and blood =='Above'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),lc_hb,lc_bldgrp,lc_sickling,lc_tsh from patient_registration r,anc_main a,anc_lab_checkup lc where r.regno=a.regno and a.anc_id=lc.anc_id and a.anc_status=1 and regdate between '{}' and '{}'and CAST(lc.lc_hb AS DECIMAL(10,2)) > '{}'".format(frmdate,todate,hb)

        elif(frmdate != '' and todate != '' and hb != '' and blood =='Below'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),lc_hb,lc_bldgrp,lc_sickling,lc_tsh from patient_registration r,anc_main a,anc_lab_checkup lc where r.regno=a.regno and a.anc_id=lc.anc_id and a.anc_status=1 and regdate between '{}' and '{}'and CAST(lc.lc_hb AS DECIMAL(10,2)) < '{}'".format(frmdate,todate,hb)

        else:
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),lc_hb,lc_bldgrp,lc_sickling,lc_tsh from patient_registration r,anc_main a,anc_lab_checkup lc where r.regno=a.regno and a.anc_id=lc.anc_id and a.anc_status=1 and regdate between '{}' and '{}'".format(frmdate,todate,hb)

        cursor.execute(sql)
        w=cursor.fetchall()

        workbook = Workbook(anchb)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'blue'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"SURNAME",cell_format)
        sheet.write(0,4,"AGE",cell_format)
        sheet.write(0,5,"AGETYPE",cell_format)
        sheet.write(0,6,"SEX",cell_format)
        sheet.write(0,7,"RELATION",cell_format)
        sheet.write(0,8,"RELATIVE'S NAME",cell_format)
        sheet.write(0,9,"RELATIVE'S MIDDLE NAME",cell_format)
        sheet.write(0,10,"RELATIVE'S SURNAME",cell_format)
        sheet.write(0,11,"EDUCATION",cell_format)
    	sheet.write(0,12,"REG.DATE",cell_format)
    	sheet.write(0,13,"ADDRESS",cell_format)
    	sheet.write(0,14,"ANC VISIT DATE",cell_format)
    	sheet.write(0,15,"HAEMOGLOBIN",cell_format)
    	sheet.write(0,16,"BLOOD GROUP",cell_format)
    	sheet.write(0,17,"SICKLING",cell_format)
    	sheet.write(0,18,"THYROID",cell_format)

        for r, row in enumerate(w):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
    	workbook.close()
        return w
    except Exception as e:
        return str(e)

#This function will search ANC patient by Blood Pressure.
def ANCSearchBp(ancbp):
    try:
        frmdate=request.form['frmdate']
        todate=request.form['todate']
        sys=int(request.form['sys'])
        dia=int(request.form['dia'])
        pressure=request.form['pressure']
        ancbp=ancbp+"ancbp.xlsx"

        if(frmdate != '' and todate != '' and sys != '' and dia != '' and pressure =='Exact'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),FoV_systolic,FoV_diastolic,FoV_oedema,FoV_variveins,FoV_immstatus from patient_registration r,anc_main a,anc_followup_visit fv where r.regno=a.regno and a.anc_id=fv.anc_id and a.anc_status=1 and regdate between '{}' and '{}'and CAST(FoV_systolic AS INT)='{}' and CAST(FoV_diastolic AS INT)='{}'".format(frmdate,todate,sys,dia)

        elif(frmdate != '' and todate != '' and sys != '' and dia != '' and pressure =='Above'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),FoV_systolic,FoV_diastolic,FoV_oedema,FoV_variveins,FoV_immstatus from patient_registration r,anc_main a,anc_followup_visit fv where r.regno=a.regno and a.anc_id=fv.anc_id and a.anc_status=1 and regdate between '{}' and '{}'and CAST(FoV_systolic AS INT)>'{}' and CAST(FoV_diastolic AS INT)>'{}'".format(frmdate,todate,sys,dia)

        elif(frmdate != '' and todate != '' and sys != '' and dia != '' and pressure =='Below'):
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),FoV_systolic,FoV_diastolic,FoV_oedema,FoV_variveins,FoV_immstatus from patient_registration r,anc_main a,anc_followup_visit fv where r.regno=a.regno and a.anc_id=fv.anc_id and a.anc_status=1 and regdate between '{}' and '{}'and CAST(FoV_systolic AS INT)<'{}' and CAST(FoV_diastolic AS INT)<'{}'".format(frmdate,todate,sys,dia)

        else:
            sql="select r.regno,pfname,pmname,psname,age,agetype,sex,rtype,rfname,rmname,rsname,education,DATE_FORMAT(regdate,'%d/%m/%Y'),address,DATE_FORMAT(anc_date,'%d/%m/%Y'),FoV_systolic,FoV_diastolic,FoV_oedema,FoV_variveins,FoV_immstatus from patient_registration r,anc_main a,anc_followup_visit fv where r.regno=a.regno and a.anc_id=fv.anc_id and a.anc_status=1 and regdate between '{}' and '{}'".format(frmdate,todate,sys,dia)

        cursor.execute(sql)
        d=cursor.fetchall()

        workbook = Workbook(ancbp)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"REG.NO.",cell_format)
        sheet.write(0,1,"NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"SURNAME",cell_format)
        sheet.write(0,4,"AGE",cell_format)
        sheet.write(0,5,"AGETYPE",cell_format)
        sheet.write(0,6,"SEX",cell_format)
        sheet.write(0,7,"RELATION",cell_format)
        sheet.write(0,8,"RELATIVE'S NAME",cell_format)
        sheet.write(0,9,"RELATIVE'S MIDDLE NAME",cell_format)
        sheet.write(0,10,"RELATIVE'S SURNAME",cell_format)
        sheet.write(0,11,"EDUCATION",cell_format)
        sheet.write(0,12,"REG.DATE",cell_format)
        sheet.write(0,13,"ADDRESS",cell_format)
        sheet.write(0,14,"ANC VISIT DATE",cell_format)
        sheet.write(0,15,"SYSTOLIC",cell_format)
        sheet.write(0,16,"DIASTOLIC",cell_format)
        sheet.write(0,17,"OEDEMA",cell_format)
        sheet.write(0,18,"VARICOSE VEINS",cell_format)
        sheet.write(0,19,"IMMUNIZATION STATUS",cell_format)

        for r, row in enumerate(d):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return d
    except Exception as e:
        return str(e)
################################################################################

###========================= ANC Report =====================================###

#This function will fetch the required regno and check its status in anc for a patient.
def getANCReport(anc_id):
    try:
        sql="select p.regno,pfname,pmname,psname,DATE_FORMAT(regdate,'%d/%m/%Y'),age,agetype,sex,education,anc_id,patient_history,gravida_history,first_visit,follow_visit,lab_checkup,usg_report,p.address,p.contactno from patient_registration p,anc_main a where a.regno=p.regno and anc_status=1 and anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getANCPhReport(anc_id):
    try:
        sql="select ph_id,anc_id,DATE_FORMAT(ph_date, '%d-%m-%Y'),ph_age,duration,cycle,DATE_FORMAT(lmp, '%d-%m-%Y'),edd,occupation,martial_status,past_history,family_history,contraceptive_history,ph_others from anc_patient_history where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getANCGhReport(anc_id):
    try:
        sql="select gh_id,anc_id,DATE_FORMAT(gh_date,'%d-%m-%Y'),gravida,parity_live,DATE_FORMAT(dopa,'%d-%m-%Y'),dop,aop,lsch,delivery_type,no_babies,puerperium,childsex,baby_wt,brstfed_btlefed,gh_others,baby_status from anc_gravida_history where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getANCFiVReport(anc_id):
    try:
        sql="select FiV_id,anc_id,FiV_seen_doctor,FiV_seen_sister,DATE_FORMAT(FiV_date,'%d-%m-%Y'),FiV_wt,FiV_ht,FiV_bmi,FiV_systolic,FiV_diastolic,Fiv_pulse,FiV_heart,FiV_lungs,FiV_breast,FiV_anaemia,FiV_jaundice,Fiv_tongue,FiV_thyroid,FiV_neckglds,FiV_teeth,FiV_gum,FiV_throat,FiV_kidneys,FiV_oedema,FiV_spleen,FiV_liver,FiV_variveins,FiV_pallor,FiV_icterus,FiV_others from anc_first_visit where anc_id='{}'".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getANCFoVReport(anc_id):
    try:
        sql="select FoV_id,anc_id,FoV_seen_doctor,FoV_seen_sister,DATE_FORMAT(FoV_date,'%d-%m-%Y'),FoV_wt,FoV_ht,FoV_bmi,FoV_systolic,FoV_diastolic,FoV_pulse,FoV_bodytemp,FoV_resprate,FoV_utsize,FoV_oedema,FoV_no_foetus,FoV_fhs,FoV_pallor,FoV_cyanosis,FoV_icterus,FoV_variveins,FoV_immstatus,FoV_others from anc_followup_visit where anc_id='{}' order by FoV_date desc".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getANCLcReport(anc_id):
    try:
        sql="select lc_id,anc_id,DATE_FORMAT(lc_date,'%d-%m-%Y'),lc_testdone,lc_sugar,lc_albumin,lc_microscopy,lc_hb,lc_bldgrp,lc_sickling,lc_vdrl,lc_hbsag,lc_hiv,lc_rbs,lc_tsh,lc_others from anc_lab_checkup where anc_id='{}' order by lc_date desc".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getANCUsgReport(anc_id):
    try:
        sql="select usg_id,anc_id,DATE_FORMAT(usg_date, '%d-%m-%Y'),usg_testdone,usg_gravida,DATE_FORMAT(usg_lmp, '%d-%m-%Y'),usg_edd,usg_foetus,usg_presentation,usg_placenta,usg_liquor,usg_crl,usg_fa1,DATE_FORMAT(usg_edd1, '%d-%m-%Y'),usg_bpd,usg_fa2,DATE_FORMAT(usg_edd2,'%d-%m-%Y'),usg_hc,usg_fa3,DATE_FORMAT(usg_edd3,'%d-%m-%Y'),usg_ac,usg_fa4,DATE_FORMAT(usg_edd4,'%d-%m-%Y'),usg_fl,usg_fa5,DATE_FORMAT(usg_edd5,'%d-%m-%Y'),usg_fa6,DATE_FORMAT(usg_edd6,'%d-%m-%Y'),usg_fhr,usg_fwt,usg_hc_ae,usg_fl_he,usg_fl_ae,usg_others from anc_usg_report where anc_id='{}' order by usg_date desc".format(anc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)



#This function will fetch the current data of Lab for Print
def ANCLabPrint():
    lc_id=request.form['lc_id']
    try:
        sql="select p.regno,pfname,pmname,psname,sex,age,agetype,regdate,address,contactno,o.regno,complaint,a.regno,a.anc_id,DATE_FORMAT(anc_date,'%d/%m/%Y'),lc_id,lc.anc_id,DATE_FORMAT(lc_date,'%d/%m/%Y'),lc_testdone,lc_sugar,lc_albumin,lc_microscopy,lc_hb,lc_bldgrp,lc_sickling,lc_vdrl,lc_hbsag,lc_hiv,lc_rbs,lc_tsh,lc_others from patient_registration p,opdvisit o,anc_main a,anc_lab_checkup lc where p.regno=o.regno and p.regno=a.regno and a.anc_id=lc.anc_id and lc_id='{}'".format(lc_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

##########################Update for Lab Report##########Sanjay############################################

def ANCSearchForLabData(regno):
    #regno=request.form['regno']
    try:
        sql="select r.regno,pfname,pmname,psname,age,agetype,DATE_FORMAT(lc_date,'%d/%m/%Y'),DATE_FORMAT(anc_date,'%d/%m/%Y'),a.anc_id,anc_status,lc.lc_id from patient_registration r,anc_main a,anc_lab_checkup lc where r.regno=a.regno and anc_status=1 and a.anc_id=lc.anc_id and r.regno='{}' order by lc_date desc".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

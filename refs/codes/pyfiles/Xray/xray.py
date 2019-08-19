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
import adminstuff as adm
from werkzeug import secure_filename
import datetime
from xlsxwriter.workbook import Workbook


#DB object for hospital databse
db = con.db
cursor=db.cursor()



#This function will return entire row of patient_registration with respect to RegNo.(OPD)
def getOpdPatientXray(regno):

	try:
		sql="select p.regno,pfname,pmname,psname,sex,age,'OPD',o.opdid,agetype from patient_registration p,opdvisit o where o.regno=p.regno and o.regno='{}' order by vdate desc limit 1".format(regno)
		cursor.execute(sql)

		return cursor.fetchall()
	except Exception as e:

         return str(e)



#This function will return entire row of patient_registration with respect to RegNo.(ward/ipd)


def getWardPatientXray(regno):

	try:
		sql="select p.regno,pfname,pmname,psname,sex,age,awb.bname,w.wrd_id,i.wardid from patient_registration p,ward_main w,ipdvisit i,admin_ward_bdname awb where w.regno=p.regno and w.wardstatus=1 and w.ipdid=i.ipdid and w.bedno=awb.bid and i.regno='{}' order by ipddate desc limit 1".format(regno)
		cursor.execute(sql)

		return cursor.fetchall()
	except Exception as e:

         return str(e)


#This function will insert a record in xray table


def insertXrayDetail(uploadloc):
    result=''
    tablename = "xray"
    regno = request.form['regno']
    row=len(request.form.getlist('xtype'))

    xdate = request.form.getlist('xdate') #Has Multiple Value
    xt = request.form.getlist('xtype') #Has Multiple Value
    st = request.form.getlist('stype')  #Has Multiple Value
    amt = request.form.getlist('amount') #Has Multiple Value
    upld= request.files.getlist('upload') #Has Multiple Value
    print(upld)

    try:
        if request.method == 'POST':

            for i in range(row):

                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('regno')
                dbcolumn.append('xdate')
                dbcolumn.append('pid')
                dbcolumn.append('xtype')
                dbcolumn.append('stype')
                dbcolumn.append('amount')
                dbcolumn.append('upload')
                dbcolumn.append('location')


                htmlcolumn.append(regno)
                htmlcolumn.append(xdate[i])
                htmlcolumn.append(request.form['pid'])
                htmlcolumn.append(xt[i])
                htmlcolumn.append(st[i])
                htmlcolumn.append(amt[i])
                fname,fileext = os.path.splitext(upld[i].filename)
                filename=secure_filename(regno+'_'+'{0:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'_'+fname+fileext)
                dst_path=os.path.join(uploadloc, filename)
                upld[i].save(dst_path)

                htmlcolumn.append(filename)
                htmlcolumn.append(request.form['location'])





                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                print(result)
            return result

    except Exception as e:
        return str(e)



#+++=========================ADMIN X-Ray=============================++++#

def newXrayPart():
    xrayname = request.form['xrayname']

    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_xname"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('xrayname')
            htmlcolumn.append(request.form['xrayname'])
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def newSubXray():
    xid=request.form['xid']
    subxray = request.form['subxray']

    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_subname"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('xid')
            dbcolumn.append('subxray')
            dbcolumn.append('amount')

            htmlcolumn.append(request.form['xid'])
            htmlcolumn.append(request.form['subxray'])
            htmlcolumn.append(request.form['amount'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def updatepartname():
    xid = request.form['xid']
    xrayname = request.form['xrayname']

    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_xname"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('xrayname')
            dbcolumn.append('xid') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            htmlcolumn.append(xrayname)
            htmlcolumn.append(xid) # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def getAllSubXrayList():
    try:
        sql="select ab.*,xrayname from admin_xname ax,admin_subname ab where ab.xid=ax.xid and ax.deletestatus=0 order by subxray desc"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)




def updateSubPartName():
    subid = request.form['subid']
    subxray = request.form['subxray']

    dbcolumn = []
    htmlcolumn = []
    tablename = "admin_subname"
    result=''
    try:
        if request.method == 'POST':
			dbcolumn.append('xid')
			dbcolumn.append('subxray')
			dbcolumn.append('amount')
			dbcolumn.append('subid') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

			htmlcolumn.append(request.form['xid'])
			htmlcolumn.append(subxray)
			htmlcolumn.append(request.form['amount'])
			htmlcolumn.append(subid) # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

			result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
			return result
    except Exception as e:
		return str(e)



#####################################*Getting Patient Details For Update*#######################################

def getPatientDetail(regno):

	try:
		sql= "select p.regno,pfname,pmname,psname,sex,age,x.location,agetype from patient_registration p,opdvisit o,xray x where p.regno=o.regno and o.regno=x.regno and x.regno='{}' and x.location='OPD' order by xdate desc limit 1".format(regno)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)

def getWardPatientDetail(regno):

	try:
		sql= "select p.regno,pfname,pmname,psname,sex,age,awb.bname,w.wrd_id,i.wardid,x.pid from xray x, patient_registration p,ward_main w,ipdvisit i,admin_ward_bdname awb where w.regno=p.regno and w.regno=x.regno and w.wardstatus=1 and w.bedno=awb.bid and w.ipdid=i.ipdid and w.wrd_id=x.pid and x.regno='{}' and x.location!='OPD' order by xdate desc limit 1".format(regno)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)

############################################################################################################


#====================================++X-Ray Update++===========================================#

def getOpdUpdateXray(regno):

	try:
		sql="select o.opdid,x.id,x.xdate,ax.xid,ax.xrayname,s.subid,s.subxray,x.amount,x.upload from patient_registration p,opdvisit o,xray x,admin_xname ax,admin_subname s where p.regno=o.regno and o.opdid=x.pid and ax.xid=x.xtype and x.location='OPD' and s.subid=x.stype and x.regno='{}' order by xdate desc".format(regno)
		cursor.execute(sql)
		print(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)

def getWardUpdateXray(regno):

	try:
		sql="select w.wrd_id,x.id,x.xdate,ax.xid,ax.xrayname,s.subid,s.subxray,x.amount,x.upload,x.pid from patient_registration p,ipdvisit i,xray x,admin_xname ax,admin_subname s,ward_main w where p.regno=w.regno and w.wrd_id=x.pid and ax.xid=x.xtype and x.location!='OPD' and s.subid=x.stype and wardstatus=1 and w.ipdid=i.ipdid and x.regno='{}' order by xdate desc;".format(regno)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)

def updateXrayDetail(uploadloc):
    result=''
    tablename = "xray"
    regno = request.form['regno']
    print("i am regno",regno)


    id = request.form['id']
    xdate = request.form['xdate']
    xtype = request.form['xrayname']
    stype = request.form['subxray']
    amount = request.form['amount']
    oldupload = request.form['oldupload']

    checkbox = request.form.get('chkbox')

    try:
        if request.method == 'POST':
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('xdate')
                dbcolumn.append('xtype')
                dbcolumn.append('stype')
                dbcolumn.append('amount')

                if checkbox == 'on':
                        xupload = request.files['uploadxray']
                        dbcolumn.append('upload')

                dbcolumn.append('id')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

                htmlcolumn.append(xdate)
                htmlcolumn.append(xtype)
                htmlcolumn.append(stype)
                htmlcolumn.append(amount)

                if checkbox == 'on':
                        fname,fileext = os.path.splitext(xupload.filename)
                        filename=secure_filename(regno+'_'+'{0:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'_'+fname+fileext)
                        dst_path=os.path.join(uploadloc, filename)
                        xupload.save(dst_path)
                        print("i m file",filename)

                        htmlcolumn.append(filename)

                htmlcolumn.append(id) # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

                # Here we are calling UpdateData that have a  common  code for update record.

                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                print("i am resultup",result)
                if result ==1:
                        os.remove(os.path.join(uploadloc,oldupload))
                return result
    except Exception as e:
        print("ERORORORO",str(e))
        return str(e)

def getAllXray(xraytype):

        try:
                sql="select subid,subxray from admin_xname ax,admin_subname s where s.xid=ax.xid and s.xid='{}'".format(xraytype)
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
                return str(e)

def getAllSubXray(subxray) :

        try:
                sql="select amount from admin_subname where subid='{}'".format(subxray)
                dr=cursor.execute(sql)
                print("i am dr",dr)
                return cursor.fetchall()
        except Exception as e:
                return str(e)
#####################################################################################################################
					#=======================+Acknowledgement By Regno+============================#

def getPatientNameDetails(regno):

	try:
		sql="select p.regno,p.pfname,p.pmname,p.psname,p.sex,p.age,p.agetype from patient_registration p,xray x where p.regno=x.regno and x.regno='{}' order by xdate desc limit 1".format(regno)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)

def getPatientXrayDetailXray(regno):

	try:
		sql=" select x.xdate,ax.xid,ax.xrayname,s.subid,s.subxray,x.amount,x.upload,x.location from patient_registration p,xray x,admin_xname ax,admin_subname s where p.regno=x.regno and ax.xid=x.xtype and s.subid=x.stype and x.regno='{}' order by xdate desc".format(regno)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)


def getPatientXrayByDate(filldate):

        try:
                sql="select p.regno,pfname,pmname,psname,p.sex,p.age,p.agetype,x.location,x.xdate,ax.xid,ax.xrayname,s.subid,s.subxray,x.amount from patient_registration p,xray x,admin_xname ax,admin_subname s where p.regno=x.regno and ax.xid=x.xtype and s.subid=x.stype and x.xdate='{}' order by xdate desc".format(filldate)
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:

         return str(e)


def getTotalPatientByDate(filldate):

	try:
		sql="select count(*),sum(amount) from xray where xdate='{}'".format(filldate)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:

         return str(e)



def monthlyXrayReport(exray):
	allxray = adm.getAllXray()
	fdate = request.form['fdate']
	tdate = request.form['tdate']
	exray=exray+"monthlyxray.xlsx"


	startpart = 'select monthname(xm.xdate),'
	tempstr=''
	xtotal = ''
	for i in range(0,len(allxray)):
		xraynames = "count(case when xtype="+str(allxray[i][0])+" then xtype end) as "+str(allxray[i][1])
		if i == 0:
			xtotal = xtotal +"count(case when xtype="+str(allxray[i][0])+" then xtype end)"
		else:
			xtotal = xtotal +"+count(case when xtype="+str(allxray[i][0])+" then xtype end)"
		tempstr =tempstr+xraynames+","

	endpart = xtotal+" from xray xm,admin_xname xa where  xm.xtype = xa.xid and xm.xdate between '{}' and '{}' group by month(xm.xdate)"
	tempstr = startpart+tempstr+endpart
	print(tempstr)
	sql = tempstr.format(fdate,tdate)
	print(sql)
	cursor.execute(sql)
	a=cursor.fetchall()
	print(a)

	workbook = Workbook(exray)
	sheet = workbook.add_worksheet()
	cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
	sheet.write(0,0,"Month",cell_format)
	for i in range(0,len(allxray)):
		sheet.write(0,i+1,allxray[i][1],cell_format)
	sheet.write(0,i+2,"Total",cell_format)

	for r, row in enumerate(a):
		for c, col in enumerate(row):
			sheet.write(r+1, c, col)
	workbook.close()
	return a


#To fetch all Patient in between  dates


def getAllXrayData(Fdate,Tdate):
    try:
        sql=" select p.regno,pfname,pmname,psname,sex,age,agetype,x.location,x.xdate,ax.xid,ax.xrayname,s.subid,s.subxray,x.amount from patient_registration p,xray x,admin_xname ax,admin_subname s where p.regno=x.regno and ax.xid=x.xtype and s.subid=x.stype and x.xdate between '{}' and '{}'".format(Fdate,Tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

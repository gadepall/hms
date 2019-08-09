from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys
import db_conf as con
newpath = os.getcwd()+"/dbpy"
sys.path.insert(0, newpath)
import insertdata as ins
import updatedata as up
from xlsxwriter.workbook import Workbook

db = con.db
cursor=db.cursor()

def getAdmitPatientData(ipdid):
    try:
        sql = "select i.*,TIME_FORMAT(i.ipdtime,'%H:%i'),w.wid,w.wname,gs.gsname from ipdvisit i,admin_wardname w,admin_govsch gs where i.wardid=w.wid AND i.govscheme=gs.gsid AND ipdid='{}'".format(ipdid)
        cursor.execute(sql)
        return(cursor.fetchall())
    except Exception as e:
        return str(e)


def getAllAdmitPatientData(regno):
    try:
        sql = "select i.*,w.wid,w.wname,gs.gsname from ipdvisit i,admin_wardname w,admin_govsch gs where i.wardid=w.wid AND i.govscheme=gs.gsid AND regno='{}' order by ipddate DESC".format(regno)
        cursor.execute(sql)
        return(cursor.fetchall())
    except Exception as e:
        return str(e)

def getLatestAdmitPatientData(regno):
    try:
        sql = "select p.*,o.complaint,o.ptype,ad.disname,c.cname from patient_registration p, opdvisit o,admin_district ad,admin_company c where p.regno = o.regno AND p.district=ad.did AND p.pclass=c.cid AND o.regno= '{}' order by o.vdate DESC limit 1".format(regno)
        cursor.execute(sql)
        return(cursor.fetchall())
    except Exception as e:
        return str(e)

# THIS FUNCTION WILL INSERT A NEW ROW IN IPDVISIT TABLE.

def visitIpd():
    gscheme=request.form['gscheme']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ipdvisit"
    try:
        if request.method == 'POST':
            dbcolumn.append('regno')
            dbcolumn.append('complaint')
            dbcolumn.append('patientfrom')
            dbcolumn.append('ipddate')
            dbcolumn.append('ipdtime')
            dbcolumn.append('ptype')
            dbcolumn.append('govscheme')
            dbcolumn.append('urnno')
            dbcolumn.append('advmoney')
            dbcolumn.append('moneyreceivedby')
            dbcolumn.append('wardid')


            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['complaint'])
            htmlcolumn.append(request.form['patientfrom'])
            htmlcolumn.append(request.form['ipddate'])
            htmlcolumn.append(request.form['ipdtime'])
            htmlcolumn.append(request.form['ptype'])

            if gscheme == 'eligible':
                htmlcolumn.append(request.form['govscheme'])
            else:
                htmlcolumn.append(str(request.form['gscheme']))

            htmlcolumn.append(request.form['urnno'])
            htmlcolumn.append(request.form['advmoney'])
            htmlcolumn.append(request.form['moneyreceivedby'])
            htmlcolumn.append(request.form['wardid'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

# THIS FUNCTION WILL UPDATE THE OLD INFORMATION IN IPDVISIT TABLE.

def visitIpdUpdate():
    gscheme=request.form['gscheme']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ipdvisit"
    try:
        if request.method == 'POST':
            dbcolumn.append('complaint')
            dbcolumn.append('patientfrom')
            dbcolumn.append('ipddate')
            dbcolumn.append('ipdtime')
            dbcolumn.append('govscheme')
            dbcolumn.append('urnno')
            dbcolumn.append('advmoney')
            dbcolumn.append('moneyreceivedby')
            dbcolumn.append('wardid')
            dbcolumn.append('ipdid')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            htmlcolumn.append(request.form['complaint'])
            htmlcolumn.append(request.form['patientfrom'])
            htmlcolumn.append(request.form['ipddate'])
            htmlcolumn.append(request.form['ipdtime'])

            if gscheme == 'eligible':
                htmlcolumn.append(request.form['govscheme'])
            else:
                htmlcolumn.append(str(request.form['gscheme']))

            htmlcolumn.append(request.form['urnno'])
            htmlcolumn.append(request.form['advmoney'])
            htmlcolumn.append(request.form['moneyreceivedby'])
            htmlcolumn.append(request.form['wardid'])
            htmlcolumn.append(request.form['ipdid'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def getAdmitPatientDataForPrint(regno,ipddate):
    try:
        sql="select p.*,i.*,aw.wname,ac.cname,ag.gsname from patient_registration p,ipdvisit i,admin_company ac,admin_govsch ag,admin_wardname aw where p.regno=i.regno and p.pclass=ac.cid and i.govscheme = ag.gsid and i.wardid = aw.wid and i.regno='{}' and i.ipddate='{}' order by i.ipddate desc limit 1".format(regno,ipddate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getOldAdmitPatientDataForPrint(ipdid):
    try:
        sql="select p.*,i.*,aw.wname,ac.cname,ag.gsname from patient_registration p,ipdvisit i,admin_company ac,admin_govsch ag,admin_wardname aw where p.regno=i.regno and p.pclass=ac.cid and i.govscheme = ag.gsid and i.wardid = aw.wid and i.ipdid='{}' order by i.ipddate desc limit 1".format(ipdid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#=========================ACKNOWLEDGEMENT================================
def getPtypeTodayAckIpd(fildate):
    try:
        sql="select count(case when i.ptype='NEW' then i.ptype end) as New,count(case when i.ptype='OLD' then i.ptype end) as Old from ipdvisit i where i.ipddate='{}'".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getGeneralPtypeIpd(fildate):
    try:
        sql="select count(case when i.ptype='NEW' then i.ptype end) as New,count(case when i.ptype='OLD' then i.ptype end) as Old,count(case when i.ptype='NEW' then i.ptype end)*20 + count(case when i.ptype='OLD' then i.ptype end)*10 as totalamount from patient_registration p,ipdvisit i where p.regno=i.regno AND p.pclass='-1' AND i.ipddate='{}'".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPcatTodayAckIpd(fildate):
    try:
        sql="select count(case when p.pclass='-1' then p.pclass end) as General,count(case when p.pclass='-2' then p.pclass end) as staff,count(case when p.pclass='-3' then p.pclass end) as CMSS,count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as Company,count(case when i.govscheme <>'-1' then i.govscheme end) as gsch  from patient_registration p,ipdvisit i where p.regno=i.regno AND  i.ipddate='{}'".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getCompanyDetailIpd(fildate):
    try:
        sql="select c.cname,count(*) from patient_registration p,ipdvisit i,admin_company c where p.regno=i.regno AND p.pclass=c.cid  AND pclass<>'-1' AND pclass<>'-2' AND pclass<>'-3' AND i.ipddate='{}'  group by pclass".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getGovSchemeDetailIpd(fildate):
    try:
        sql="select gsname,count(*) from patient_registration p,ipdvisit i,admin_govsch g where p.regno=i.regno and i.govscheme=g.gsid and i.govscheme<>'-1' AND i.ipddate='{}'  group by govscheme".format(fildate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getPtypeRangeAckIpd(fdate,tdate):
    try:
        sql="select i.ipddate,count(case when i.ptype='NEW' then i.ptype end) as New,count(case when i.ptype='OLD' then i.ptype end) as Old,count(case when i.ptype='NEW' then i.ptype end)+count(case when i.ptype='OLD' then i.ptype end) as total from ipdvisit i where i.ipddate BETWEEN '{}' AND '{}' group by i.ipddate".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getTotalPtypeRangeAckIpd(fdate,tdate):
    try:
        sql="select count(case when i.ptype='NEW' then i.ptype end) as New,count(case when i.ptype='OLD' then i.ptype end) as Old,count(case when i.ptype='NEW' then i.ptype end)+count(case when i.ptype='OLD' then i.ptype end) as total from ipdvisit i where i.ipddate BETWEEN '{}' AND '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPcatRangeAckIpd(fdate,tdate):
    try:
        sql="select i.ipddate,count(case when p.pclass='-1' then p.pclass end) as General,count(case when p.pclass='-2' then p.pclass end) as staff,count(case when p.pclass='-3' then p.pclass end) as CMSS,count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as Company,count(case when i.govscheme <> '-1' then i.govscheme end) as govsh,count(case when p.pclass='-1' then p.pclass end)+count(case when p.pclass='-2' then p.pclass end)+count(case when p.pclass='-3' then p.pclass end)+count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as total from patient_registration p,ipdvisit i where p.regno=i.regno AND  i.ipddate BETWEEN '{}' AND '{}' group by i.ipddate".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTotalPcatRangeAckIpd(fdate,tdate):
    try:
        sql="select count(case when p.pclass='-1' then p.pclass end) as General,count(case when p.pclass='-2' then p.pclass end) as staff,count(case when p.pclass='-3' then p.pclass end) as CMSS,count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as Company,count(case when i.govscheme <> '-1' then i.govscheme end) as govsh,count(case when p.pclass='-1' then p.pclass end)+count(case when p.pclass='-2' then p.pclass end)+count(case when p.pclass='-3' then p.pclass end)+count(case when p.pclass<>'-1' AND p.pclass<>'-2' AND p.pclass<>'-3' then p.pclass end) as total from patient_registration p,ipdvisit i where p.regno=i.regno AND  i.ipddate BETWEEN '{}' AND '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)



#====================IPDSEARCH================
def getipdoldpatientviewToday():
    try:
        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,i.ipddate,i.ipdtime from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.govscheme = ag.gsid and i.ipddate=curdate()"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getipdoldpatientviewdate(ipd):
    ipd=ipd+"ipd.xlsx"
    fdate=request.form['fdate']
    tdate=request.form['tdate']
    try:

        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,DATEDIFF(dischargedate,ipddate) as days,w.history,w.diagnosis,w.advice,w.death_refer_reason,w.patientstatus,w.othernotes,dischargeby from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag,ward_main w where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.ipdid=w.ipdid and i.govscheme = ag.gsid and wardstatus=0 and dischargestatus=3 and w.regno=i.regno and i.dischargedate BETWEEN '{}' and '{}'".format(fdate,tdate)
        print("i am ipdsql",sql)
        cursor.execute(sql)
        q=cursor.fetchall()

        workbook = Workbook(ipd)
        print("i am workbook=",workbook)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'green'})
        sheet.write(0,0,"Regno.",cell_format)
        sheet.write(0,1,"FIRST NAME",cell_format)
        sheet.write(0,2,"MIDDLE NAME",cell_format)
        sheet.write(0,3,"LAST NAME",cell_format)
        sheet.write(0,4,"RelativeName",cell_format)
        sheet.write(0,5,"RFirst Name",cell_format)
        sheet.write(0,6,"RMiddle Name",cell_format)
        sheet.write(0,7,"RLast Name",cell_format)
        sheet.write(0,8,"IPD Date",cell_format)
        sheet.write(0,9,"IPD Time",cell_format)
        sheet.write(0,10,"Age",cell_format)
        sheet.write(0,11,"AgeType",cell_format)
        sheet.write(0,12,"Gender",cell_format)
        sheet.write(0,13,"Education",cell_format)
        sheet.write(0,14,"Occupation",cell_format)
        sheet.write(0,15,"Phone Number",cell_format)
        sheet.write(0,16,"Post Office",cell_format)
        sheet.write(0,17,"Tahsil",cell_format)
        sheet.write(0,18,"District",cell_format)
        sheet.write(0,19,"Address",cell_format)
        sheet.write(0,20,"Cast",cell_format)
        sheet.write(0,21,"Aadhar No.",cell_format)
        sheet.write(0,22,"Ration Card",cell_format)
        sheet.write(0,23,"Ward Name",cell_format)
        sheet.write(0,24,"Patient Category",cell_format)
        sheet.write(0,25,"Ipdid",cell_format)
        sheet.write(0,26,"Government Scheme",cell_format)
        sheet.write(0,27,"Complaint",cell_format)
        sheet.write(0,28,"Patient From",cell_format)
        sheet.write(0,29,"Discharge Date",cell_format)
        sheet.write(0,30,"Discharge Time",cell_format)
        sheet.write(0,31,"Patient Type",cell_format)
        sheet.write(0,32,"Total Days(Patient Admitted)",cell_format)
        sheet.write(0,33,"History",cell_format)
        sheet.write(0,34,"Diagnosis",cell_format)
        sheet.write(0,35,"Advice",cell_format)
        sheet.write(0,36,"Death Refer Reason",cell_format)
        sheet.write(0,37,"Patient Status",cell_format)
        sheet.write(0,38,"Other Notes",cell_format)
        sheet.write(0,39,"Discharge Written By",cell_format)



        for r, row in enumerate(q):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return q
    except Exception as e:
        return str(e)




def getipdoldpatientviewnamedate():
    try:
        pfname=request.form['pfname']
        fdate=request.form['fdate']
        tdate=request.form['tdate']
        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,i.ipddate,i.ipdtime from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.govscheme = ag.gsid and p.pfname LIKE '%{}%' and i.ipddate BETWEEN '{}' and '{}'".format(pfname,fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getipdoldpatientviewregno():
    try:
        regno=request.form['regno']
        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,i.ipddate,i.ipdtime from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.govscheme = ag.gsid and i.regno='{}' ".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getipdoldpatientviewfname():
    try:
        pfname=request.form['pfname']
        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,i.ipddate,i.ipdtime from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.govscheme = ag.gsid and p.pfname LIKE '%{}%' ".format(pfname)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getipdoldpatientviewcontact():
    try:
        contactno=request.form['contactno']
        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,i.ipddate,i.ipdtime from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.govscheme = ag.gsid and p.contactno='{}'".format(contactno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getipdoldpatientviewAddress():
    try:
        address=request.form['address']
        sql="select i.regno,p.pfname,p.pmname,p.psname,p.rtype,p.rfname,rmname,p.rsname,DATE_FORMAT(i.ipddate,'%d/%m/%Y'),TIME_FORMAT(i.ipdtime,'%H:%i'),p.age,p.agetype,p.sex,p.education,p.occupation,p.contactno,p.post,p.tahsil,ad.disname,p.address,p.cast,p.aadharNo,p.rationcard,aw.wname,ac.cname,i.ipdid,ad.disname,ag.gsname,i.complaint,patientfrom,DATE_FORMAT(i.dischargedate,'%d/%m/%Y'),TIME_FORMAT(dischargetime,'%H:%i'),i.ptype,i.ipddate,i.ipdtime from patient_registration p,ipdvisit i,admin_wardname aw,admin_company ac,admin_district ad,admin_govsch ag where p.regno=i.regno and p.pclass=ac.cid and p.district=ad.did and i.wardid=aw.wid and i.govscheme = ag.gsid and p.address LIKE '%{}%' ".format(address)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

##DISCHARGE REQUEST
def dischargeMeRequest(wmid):
    try:
        tablename="ward_main"
        dbcolumn=[]
        htmlcolumn=[]
        dbcolumn.append('dischargestatus')
        dbcolumn.append('wrd_id')

        htmlcolumn.append("1")
        htmlcolumn.append(str(wmid))
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        print("RESULT",result)
        return result
    except Exception as e:
        print("ERROR",str(e))
        return str(e)

def cancelDischargeMeRequest(wmid):
    try:
        tablename="ward_main"
        dbcolumn=[]
        htmlcolumn=[]
        dbcolumn.append('dischargestatus')
        dbcolumn.append('wrd_id')

        htmlcolumn.append("0")
        htmlcolumn.append(str(wmid))
        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        print("RESULT",result)
        return result
    except Exception as e:
        print("ERROR",str(e))
        return str(e)


def getDischargeRequestedPatientData():
    try:
        sql="select w.regno,p.pfname,p.pmname,p.psname,i.ipddate,i.ipdtime,i.complaint,i.patientfrom,ac.cname,ag.gsname,aw.wname,ab.bname,w.dischargestatus,w.wrd_id,w.ipdid,w.wid from patient_registration p,ipdvisit i,admin_wardname aw,admin_ward_bdname ab,ward_main w,admin_company ac,admin_govsch ag where p.regno=w.regno and i.ipdid=w.ipdid and aw.wid=w.wid and ab.bid=w.bedno and p.pclass = ac.cid and i.govscheme = ag.gsid and w.wardstatus=1 and w.dischargestatus<>0 and w.dischargestatus<>3 order by w.dischargestatus asc"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getPatientDataForAdvice(wmid):
    try:
        sql="select w.regno,p.pfname,p.pmname,p.psname,i.ipddate,i.ipdtime,i.complaint,i.patientfrom,ac.cname,ag.gsname,aw.wname,ab.bname,w.dischargestatus,w.wrd_id,w.history,w.diagnosis,w.advice,w.patientstatus,w.death_refer_reason,w.othernotes from patient_registration p,ipdvisit i,admin_wardname aw,admin_ward_bdname ab,ward_main w,admin_company ac,admin_govsch ag where p.regno=w.regno and i.ipdid=w.ipdid and aw.wid=w.wid and ab.bid=w.bedno and p.pclass = ac.cid and i.govscheme = ag.gsid and w.wardstatus=1 and w.dischargestatus<>0 and w.dischargestatus<>3 and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)



def updatePatientAdvice():
    try:
        tablename="ward_main"
        dbcolumn=[]
        htmlcolumn=[]
        dbcolumn.append('dischargestatus')
        dbcolumn.append('history')
        dbcolumn.append('diagnosis')
        dbcolumn.append('advice')
        dbcolumn.append('patientstatus')
        dbcolumn.append('death_refer_reason')
        dbcolumn.append('othernotes')
        dbcolumn.append('dischargeby')
        dbcolumn.append('wrd_id')


        htmlcolumn.append("2")
        htmlcolumn.append(request.form['history'])
        htmlcolumn.append(request.form['diagnosis'])
        htmlcolumn.append(request.form['advice'])
        htmlcolumn.append(request.form['patientstatus'])

        if request.form['patientstatus'] == "Cured":
            reason="Cured"
        elif request.form['patientstatus'] == "Refer":
            reason=request.form['refernote']
        elif request.form['patientstatus'] == "Dead":
            reason=request.form['dreason']

        htmlcolumn.append(reason)
        htmlcolumn.append(request.form['othernotes'])
        htmlcolumn.append(request.form['dischargeby'])
        htmlcolumn.append(request.form['wmid'])

        result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
        print("RESULT",result)
        return result
    except Exception as e:
        print("ERROR",str(e))
        return str(e)


def getAdmitPatientDataForBill(ipdid):
    try:
        sql="select p.*,i.ipddate,aw.wname,ab.bname,ac.cname,ad.disname,ag.gsname,i.advmoney,w.wrd_id,w.ipdid,ab.bid from patient_registration p,ipdvisit i,admin_wardname aw,admin_ward_bdname ab,admin_company ac,admin_district ad,ward_main w,admin_govsch ag where w.ipdid=i.ipdid and w.wid = aw.wid and w.bedno=ab.bid and w.regno=p.regno and p.pclass=ac.cid and p.district=ad.did and i.govscheme=ag.gsid  and w.ipdid='{}'".format(ipdid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientMedicineDataForBill(wmid):
    try:
        sql="select m.drugname,m.medicine_type,sum(wm.quantity),wm.unit,i.unitprice,sum(wm.amount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_medicine_chart wm where wm.meddet_id = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and wm.wrd_id='{}' group by(wm.meddet_id)".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)



def getAdmitPatientMedicineTotalAmount(wmid):
    try:
        sql="select sum(wm.amount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_medicine_chart wm where wm.meddet_id = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and wm.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientIntakeDataForBill(wmid):
    try:
        sql="select m.drugname,m.medicine_type,sum(wi.idose),wi.iunit,i.unitprice,sum(wi.iamount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_intake_chart wi where wi.meddet_id = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and wi.wrd_id='{}' group by(wi.meddet_id)".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientIntakeTotalAmount(wmid):
    try:
        sql="select sum(wi.iamount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_intake_chart wi where wi.meddet_id = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and wi.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientInsulineDataForBill(wmid):
    try:
        sql="select m.drugname,m.medicine_type,sum(ws.sdose),ws.sunit,i.unitprice,sum(ws.samount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_sugar_chart ws where ws.sinsuline = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and ws.wrd_id='{}' group by(ws.sinsuline)".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientInsulineTotalAmount(wmid):
    try:
        sql="select sum(ws.samount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_sugar_chart ws where ws.sinsuline = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and ws.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientPoisonDataForBill(wmid):
    try:
        sql="select m.drugname,m.medicine_type,sum(wp.pdose),wp.punit,i.unitprice,sum(wp.pamount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_poision_chart wp where wp.pinjection = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and wp.wrd_id='{}' group by(wp.pinjection)".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientPoisonTotalAmount(wmid):
    try:
        sql="select sum(wp.pamount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_poision_chart wp where wp.pinjection = md.meddet_id and  md.inv_id = i.inv_id and m.med_id=i.med_id and wp.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientConsumeDataForBill(wmid):
    try:
        sql="select m.drugname,m.medicine_type,sum(wc.cqty),i.unitprice,sum(wc.camount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_consume_chart wc where wc.conname = md.meddet_id and md.inv_id = i.inv_id and m.med_id=i.med_id and wc.wrd_id='{}' group by(wc.conname)".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientConsumeTotalAmount(wmid):
    try:
        sql="select sum(wc.camount) from main_medicine m,inventory_detail i,medicine_outward_detail md,ward_consume_chart wc where wc.conname = md.meddet_id and md.inv_id = i.inv_id and m.med_id=i.med_id and wc.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientSurgeryDataForBill(wmid):
    try:
        sql="select ap.sprocedure,s.ksurgerytype,ap.spamount from ward_main w,surgery_details s,admin_surgery_procedure ap where w.wrd_id=s.wrd_id and s.psurgery = ap.sid and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientSurgeryTotalAmount(wmid):
    try:
        sql="select sum(ap.spamount) from ward_main w,surgery_details s,admin_surgery_procedure ap where w.wrd_id=s.wrd_id and s.psurgery = ap.sid and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#================================================



def getAdmitPatientLabDataForBill(regno,ipdid):
    try:
        sql="select s.sample_name,t.test_name,t.amount,lt.test_value,t.Unit from admin_addsample s,admin_addtest t,lab_sample_collect ls,lab_test_data lt,ward_main w where ls.accession_no=lt.accession_no and lt.tid=t.id and t.sid = s.id and w.regno=ls.regno and ls.source <> 'OPD' and wardstatus=1  and  w.regno='{}' and  ls.source_id='{}' order by t.sid ASC".format(regno,ipdid)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientLabToatalAmount(regno,ipdid):
    try:
        sql="select sum(t.amount) from admin_addsample s,admin_addtest t,lab_sample_collect ls,lab_test_data lt,ward_main w where ls.accession_no=lt.accession_no and lt.tid=t.id and t.sid = s.id and w.regno=ls.regno and ls.source <> 'OPD' and  w.regno='{}' and  ls.source_id='{}'".format(regno,ipdid)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getLabPatientForDischarge(regno,ipdid):
    try:
        sql = "select ls.accession_no,ls.regno,p.sex,ls.date from patient_registration p, lab_sample_collect ls,ward_main w where ls.regno=p.regno and w.regno=ls.regno and w.ipdid=ls.source_id and ls.test_validation=1 and  ls.regno='{}' and  ls.source_id='{}'".format(regno,ipdid)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getTestForDischarge(regno,ipdid):
    try:
        sql = "select ls.accession_no,s.sample_name,t.test_name,lt.test_value,t.Unit,cast(t.Male_Range_min AS DECIMAL(10,2)),cast(t.Male_Range_max AS DECIMAL(10,2)),cast(t.Female_Range_min AS DECIMAL(10,2)),cast(t.Female_Range_max AS DECIMAL(10,2)),lt.test_value REGEXP '^-?[0.0-9.0]+$' from lab_sample_collect ls,lab_test_data lt,admin_addtest t,admin_addsample s where ls.accession_no = lt.accession_no and lt.tid=t.id and s.id=t.sid and ls.regno='{}' and  ls.source_id='{}' order by s.sample_name ASC".format(regno,ipdid)
        cursor.execute(sql)
        valu = cursor.fetchall()
        return valu
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientXrayDataForBill(regno,wmid):
    try:
        sql="select ax.xrayname,asx.subxray,x.amount from admin_xname ax,admin_subname asx,xray x,ward_main w where ax.xid=x.xtype and asx.subid = x.stype and ax.xid=asx.xid and x.regno=w.regno and x.pid=w.wrd_id and x.location <> 'OPD'  and x.regno='{}' and x.pid='{}'".format(regno,wmid)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def getAdmitPatientXrayTotalAmount(regno,wmid):
    try:
        sql="select sum(x.amount) from admin_xname ax,admin_subname asx,xray x,ward_main w where ax.xid=x.xtype and asx.subid = x.stype and ax.xid=asx.xid and x.regno=w.regno and x.pid=w.wrd_id and x.location <> 'OPD'  and x.regno='{}' and x.pid='{}'".format(regno,wmid)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#================================================

def getAdmitPatientDressingDataForBill(wmid):
    try:
        sql="select ad.drsname,d.dressing_amount from ward_dressing d,admin_dressing ad,ward_main w where d.dressing_name=ad.drsid and w.wrd_id=d.wrd_id and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientDressingTotalAmount(wmid):
    try:
        sql="select sum(d.dressing_amount) from ward_dressing d,admin_dressing ad,ward_main w where d.dressing_name=ad.drsid and w.wrd_id=d.wrd_id and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
#================================================

def getAdmitPatientPhyDataForBill(wmid):
    try:
        sql="select ap.phyname,p.physiotherapy_amount from ward_physiotherapy p,admin_physiotherapy ap,ward_main w where p.physiotherapy_name=ap.phyid and w.wrd_id=p.wrd_id and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getAdmitPatientPhyTotalAmount(wmid):
    try:
        sql="select sum(p.physiotherapy_amount) from ward_physiotherapy p,admin_physiotherapy ap,ward_main w where p.physiotherapy_name=ap.phyid and w.wrd_id=p.wrd_id and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
#================================================

def keepIpdBillingData():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ward_billing"
    try:
        if request.method == 'POST':
            dbcolumn.append('wrd_id')
            dbcolumn.append('bedcharge')
            dbcolumn.append('servicecharge')
            dbcolumn.append('othercharge')
            dbcolumn.append('rebateamount')
            dbcolumn.append('medamount')
            dbcolumn.append('insalamount')
            dbcolumn.append('insulineamount')
            dbcolumn.append('pinjamount')
            dbcolumn.append('conamount')
            dbcolumn.append('suramount')
            dbcolumn.append('labamount')
            dbcolumn.append('xamount')
            dbcolumn.append('ecgamount')
            dbcolumn.append('dreamount')
            dbcolumn.append('phyamount')
            dbcolumn.append('therapyamount')
            dbcolumn.append('paymentdate')
            dbcolumn.append('paymentstatus')
            dbcolumn.append('receivedby')
            dbcolumn.append('totalamount')
            dbcolumn.append('netamount')

            htmlcolumn.append(request.form['wrd_id'])
            htmlcolumn.append(str(request.form['bed']))
            htmlcolumn.append(request.form['service'])
            htmlcolumn.append(request.form['others'])
            htmlcolumn.append(request.form['rebate'])
            htmlcolumn.append(request.form['medicinetotal'])
            htmlcolumn.append(request.form['intaketotal'])
            htmlcolumn.append(request.form['isutotal'])
            htmlcolumn.append(request.form['poisontotal'])
            htmlcolumn.append(request.form['constotal'])
            htmlcolumn.append(request.form['surgerytotal'])
            htmlcolumn.append(request.form['labtotal'])
            htmlcolumn.append(request.form['xraytotal'])
            htmlcolumn.append("0")
            htmlcolumn.append(request.form['drestotal'])
            htmlcolumn.append(request.form['phystotal'])
            htmlcolumn.append("0")
            htmlcolumn.append(request.form['dischargedate'])
            htmlcolumn.append(request.form['paymentstatus'])
            htmlcolumn.append(request.form['received'])
            htmlcolumn.append(request.form['totalamounttxt'])
            htmlcolumn.append(request.form['netamounttxt'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)

            if result==1:
                dbcolumn = []
                htmlcolumn = []
                tablename = "ipdvisit"
                dbcolumn.append('dischargedate')
                dbcolumn.append('dischargetime')
                dbcolumn.append('ipdid')

                htmlcolumn.append(request.form['dischargedate'])
                htmlcolumn.append(request.form['dischargetime'])
                htmlcolumn.append(request.form['ipdid'])
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)

            if result == 1:
                dbcolumn = []
                htmlcolumn = []
                tablename = "ward_main"
                dbcolumn.append('dischargestatus')
                dbcolumn.append('wardstatus')
                dbcolumn.append('dischargestatus')
                dbcolumn.append('wrd_id')

                htmlcolumn.append(request.form['dischargedate'])
                htmlcolumn.append("0")
                htmlcolumn.append("3")
                htmlcolumn.append(request.form['wrd_id'])
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)

            if result == 1:
                dbcolumn = []
                htmlcolumn = []
                tablename = "admin_ward_bdname"
                dbcolumn.append('bstatus')
                dbcolumn.append('bid')

                htmlcolumn.append("1")
                htmlcolumn.append(request.form['bid'])
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        print("ERROR: "+str(e))
        return str(e)

#=====================================================
def getPatientDetailForDischarge(wmid):
    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,p.sex,aw.wname,w.patientstatus,i.ipddate,i.dischargedate,w.wid from patient_registration p,ipdvisit i,admin_wardname aw,ward_main w where w.ipdid=i.ipdid and w.wid = aw.wid and  w.regno=p.regno and w.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getWardDetailForDischarge(wmid):
    try:
        sql="select history,diagnosis,advice,death_refer_reason,othernotes from ward_main where wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


#========================================
def getPatientDetailForIpdBill(wmid):
    try:
        sql="select p.regno,p.pfname,p.pmname,p.psname,p.age,p.agetype,p.sex,wb.*,i.advmoney from patient_registration p,ward_main w,ward_billing wb,ipdvisit i where wb.wrd_id=w.wrd_id and w.regno=p.regno and w.ipdid=i.ipdid and wb.wrd_id='{}'".format(wmid)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
#=============================BILLING SEARCH
def getipdBillingSearchByTodayData():
    try:
        sql="select wb.wrd_id,w.ipdid,w.regno,p.pfname,pmname,psname,p.sex,p.age,p.agetype,i.ipddate,i.dischargedate,wb.paymentdate,wb.netamount,wb.paymentstatus,wb.receivedby from patient_registration p,ipdvisit i,ward_main w,ward_billing wb where wb.wrd_id=w.wrd_id and w.ipdid=i.ipdid and w.regno=p.regno and wb.paymentdate=curdate()"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getipdBillingSearchByDateData():
    try:
        fdate=request.form['fdate']
        tdate=request.form['tdate']
        sql="select wb.wrd_id,w.ipdid,w.regno,p.pfname,pmname,psname,p.sex,p.age,p.agetype,i.ipddate,i.dischargedate,wb.paymentdate,wb.netamount,wb.paymentstatus,wb.receivedby from patient_registration p,ipdvisit i,ward_main w,ward_billing wb where wb.wrd_id=w.wrd_id and w.ipdid=i.ipdid and w.regno=p.regno and wb.paymentdate BETWEEN '{}' and '{}'".format(fdate,tdate)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

def getipdBillingSearchByRegnoData():
    try:
        regno=request.form['regno']
        sql="select wb.wrd_id,w.ipdid,w.regno,p.pfname,pmname,psname,p.sex,p.age,p.agetype,i.ipddate,i.dischargedate,wb.paymentdate,wb.netamount,wb.paymentstatus,wb.receivedby from patient_registration p,ipdvisit i,ward_main w,ward_billing wb where wb.wrd_id=w.wrd_id and w.ipdid=i.ipdid and w.regno=p.regno and w.regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

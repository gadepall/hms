from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys
import datetime
import db_conf as con
import datetime as dt,time as tm
import insertdata as ins
import updatedata as up
import wardstuff as wrd
from xlsxwriter.workbook import Workbook

db = con.db
cursor=db.cursor()


##---here we are inserting new medicine
def AddNewMedicne():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "main_medicine"
    try:
        if request.method == 'POST':
            #Name of database Attribute

            dbcolumn.append('drugname')
            dbcolumn.append('medicine_type')
            dbcolumn.append('min_value')
            dbcolumn.append('max_value')


            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['drugname'])
            htmlcolumn.append(request.form['drugtype'])
            htmlcolumn.append(request.form['min_value'])
            htmlcolumn.append(request.form['max_value'])



            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#----getting all drugdepttype from inventory_detail
def GetDrugDeptType():
    try:
        sql="select distinct(drugdept_type) from inventory_detail"
        cursor.execute(sql)
        print("hii");
        return cursor.fetchall()
    except Exception as e:
        return str(e)


##----retrieving data from main medicine table--
def GetMedType():
	try:
		sql="select distinct(medicine_type) from main_medicine order by medicine_type asc"
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

##---view the list of available medicines---
def ShowAllDrugName(ViewAvailDrug):
    try:
        drugtype1=request.form['drugtype1']
        print("hello there",drugtype1)
        ViewAvailDrug=ViewAvailDrug+"ViewAvailableDrugList.xlsx"

        sql="select drugname,medicine_type,min_value,max_value from main_medicine where medicine_type='{}'".format(drugtype1)
        print(sql)

        cursor.execute(sql)
        a=cursor.fetchall()
        print("here is ur result ",a)

        workbook = Workbook(ViewAvailDrug)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Drug Name",cell_format)
        sheet.write(0,1,"Drug Type",cell_format)
        sheet.write(0,2,"MinimumValue",cell_format)
        sheet.write(0,3,"MaximumValue",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)

#----getting data according to medicinename and medicine type
def UpdateMinMaxValue():
    try:
        dname=request.form['drugname']
        dtype=request.form['drugtype']
        sql="Select min_value,max_value from main_medicine where drugname='{}' and medicine_type='{}'".format(dname,dtype)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#----retreiving data from main medicine  in one text box(drugname)
def GetAlldata():
    drugname=request.form['drugname']
    arr_rows=[]
    try:
        if len(drugname)>=1:
            sql="select drugname,medicine_type,min_value,max_value,med_id from main_medicine where drugname like '{}%'".format(drugname)
            cursor.execute(sql)
            outdata=cursor.fetchall()
            for i in range(0,len(outdata)):
                med = outdata[i][0] + " >  " +outdata[i][1] + "  > MinValue: "  + outdata[i][2] + " > MaxValue: " + outdata[i][3] +"  > medid: "+ str(outdata[i][4])
                arr_rows.append(med)
            print("MYDATA",arr_rows)
            return arr_rows
        else:
            return arr_rows
    except Exception as e:
        return str(e)




##----updating  medicine name(admin update)
def UpdateDrugNameDrugType():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "main_medicine"
    try:
        if request.method == 'POST':
            print("dsdsd",request.form['medicineid'])

            ##Name of database Attribute
            dbcolumn.append('drugname')
            dbcolumn.append('medicine_type')
            dbcolumn.append('min_value')
            dbcolumn.append('max_value')
            dbcolumn.append('med_id')
            print("i am dbcolumn",dbcolumn)

            htmlcolumn.append(request.form['drugname'])
            htmlcolumn.append(request.form['drugtype'])
            htmlcolumn.append(request.form['min_value'])
            htmlcolumn.append(request.form['max_value'])
            htmlcolumn.append(request.form['medicineid'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolum

            print("i am htmlcolumn",htmlcolumn)
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)




##------Inserting inventory details-----
def New_Inventory():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "inventory_detail"
    entrydate=request.form['entrydate']
	#print("DATE",entrydate)
    dis_id=request.form['dist_type_name']
    print("DISID",dis_id);
    row=len(request.form.getlist('batch_no'))
    print(row);
    drug = request.form.getlist('drug_id') #Has Multiple Value
    print(drug);
    hsn = request.form.getlist('hsn_code') #Has Multiple Value
    print(hsn);
    tstrip = request.form.getlist('tstrip') #Has Multiple Value
    print(tstrip);
    Rate = request.form.getlist('rate') #Has Multiple Value
    print(Rate);
    batch_no = request.form.getlist('batch_no') #Has Multiple Value
    print(batch_no);
    expiry = request.form.getlist('expiry_date') #Has Multiple Value
    print(expiry);
    mfg_d = request.form.getlist('manufacturing_date') #Has Multiple Value
    print(mfg_d);
    dis = request.form.getlist('discount') #Has Multiple Value
    print(dis);
    free = request.form.getlist('free_med') #Has Multiple Value
    print(free);
    Mrp = request.form.getlist('mrp') #Has Multiple Value
    print(Mrp);
    pak = request.form.getlist('pack') #Has Multiple Value
    print(pak);
    tax = request.form.getlist('taxable_amount') #Has Multiple Value
    print(tax);
    cgt= request.form.getlist('cgst') #Has Multiple Value
    print(cgt);
    sgt = request.form.getlist('sgst') #Has Multiple Value
    print(sgt);
    amount = request.form.getlist('amt') #Has Multiple Value
    print(amount);
    rack = request.form.getlist('rack_no') #Has Multiple Value
    print(rack);
    uprice= request.form.getlist('unitprice') #Has Multiple Value
    print(uprice);
    drugdept_type = request.form.getlist('drugdept') #Has Multiple Valu
    rmk = request.form.getlist('remark') #Has Multiple Value
    totalqty= request.form.getlist('totalqty') #Has Multiple Value
    try:
        if request.method == 'POST':
            for i in range(row):
                dbcolumn = []
                htmlcolumn = []
                dbcolumn.append('distdet_id')
                dbcolumn.append('med_id')
                dbcolumn.append('date')
                dbcolumn.append('hsn_code')
                dbcolumn.append('quantity')
                dbcolumn.append('rate')
                dbcolumn.append('batch_no')
                dbcolumn.append('expiry_date')
                dbcolumn.append('manufacturing_date')
                dbcolumn.append('discount')
                dbcolumn.append('free_med')
                dbcolumn.append('mrp')
                dbcolumn.append('pack')
                dbcolumn.append('taxable_amt')
                dbcolumn.append('cgst')
                dbcolumn.append('sgst')
                dbcolumn.append('amount')
                dbcolumn.append('rack_no')
                dbcolumn.append('temp_quantity')
                dbcolumn.append('drugdept_type')
                dbcolumn.append('remark')
                dbcolumn.append('unitprice')
                dbcolumn.append('totalqty')

                #Name of html component e.g request.form['nameofcomponenet']
                htmlcolumn.append(dis_id)
                htmlcolumn.append(drug[i])
                htmlcolumn.append(entrydate)
                htmlcolumn.append(hsn[i])
                htmlcolumn.append(tstrip[i])
                #print("HTML",htmlcolumn)
                htmlcolumn.append(Rate[i])
                htmlcolumn.append(batch_no[i])
                htmlcolumn.append(expiry[i])
                htmlcolumn.append(mfg_d[i])
                htmlcolumn.append(dis[i])
                htmlcolumn.append(free[i])
                htmlcolumn.append(Mrp[i])
                htmlcolumn.append(pak[i])
                htmlcolumn.append(tax[i])
                htmlcolumn.append(cgt[i])
                htmlcolumn.append(sgt[i])
                htmlcolumn.append(amount[i])
                htmlcolumn.append(rack[i])
                htmlcolumn.append(totalqty[i])
                htmlcolumn.append(drugdept_type[i])
                htmlcolumn.append(rmk[i])
                htmlcolumn.append(uprice[i])
                htmlcolumn.append(totalqty[i])

                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                print(result);
            return result
    except Exception as e:
        return str(e)

#----fetching data from inventory_detail(table) for updating

def GetAllInventoryDetail():
    try:
        entrydate=request.form['entrydate']
        dist_type=request.form['dist_type_name']
        sql="select i.inv_id,dt.dist_type_name,d.distributor_name,m.drugname,m.medicine_type,i.hsn_code,i.quantity,i.rate,i.batch_no,i.expiry_date,i.manufacturing_date,i.discount,i.free_med,i.mrp,i.pack,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.drugdept_type,i.remark,i.date,i.unitprice,i.totalqty from inventory_detail i,main_medicine m ,distributor_detail d,distributor_type_detail dt where i.distdet_id=d.distdet_id and d.dist_type_id = dt.dist_type_id and m.med_id=i.med_id and i.date='{}' and i.distdet_id='{}'".format(entrydate,dist_type)
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)


def ShowInventoryUpadte():
	try:
		if request.method == 'POST':
			sql="select i.inv_id,dt.dist_type_id,dt.dist_type_name,d.distdet_id,d.distributor_name,m.med_id,m.drugname,m.medicine_type,i.hsn_code,i.quantity,i.rate,i.batch_no,i.expiry_date,i.manufacturing_date,i.discount,i.free_med,i.mrp,i.pack,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.drugdept_type,i.remark,i.date,i.unitprice,i.totalqty from inventory_detail i,main_medicine m ,distributor_detail d,distributor_type_detail dt where i.distdet_id=d.distdet_id and d.dist_type_id = dt.dist_type_id and m.med_id=i.med_id and inv_id='{}'".format(request.form['inventoryid'])
			cursor.execute(sql)
			result = cursor.fetchall()
			return result
	except Exception as e:
		return str(e)


#------updating inventory-----
def UpdateInventory():
    print("update here");
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "inventory_detail"
    try:
        if request.method == 'POST':
            ##Name of database Attribute
            dbcolumn.append('distdet_id')
            dbcolumn.append('med_id')
            dbcolumn.append('date')
            dbcolumn.append('hsn_code')
            dbcolumn.append('quantity')
            dbcolumn.append('rate')
            dbcolumn.append('unitprice')
            dbcolumn.append('batch_no')
            dbcolumn.append('expiry_date')
            dbcolumn.append('manufacturing_date')
            dbcolumn.append('discount')
            dbcolumn.append('free_med')
            dbcolumn.append('mrp')
            dbcolumn.append('pack')
            dbcolumn.append('taxable_amt')
            dbcolumn.append('cgst')
            dbcolumn.append('sgst')
            dbcolumn.append('amount')
            dbcolumn.append('rack_no')
            dbcolumn.append('drugdept_type')
            dbcolumn.append('remark')
            dbcolumn.append('totalqty')
            dbcolumn.append('inv_id')
            htmlcolumn.append(request.form['distdet_id'])
            htmlcolumn.append(request.form['drug_id'])
            htmlcolumn.append(request.form['entrydate'])
            htmlcolumn.append(request.form['hsncode'])
            htmlcolumn.append(request.form['qty'])
            htmlcolumn.append(request.form['rate'])
            htmlcolumn.append(request.form['unitprice'])
            htmlcolumn.append(request.form['batchno'])
            htmlcolumn.append(request.form['expirydate'])
            htmlcolumn.append(request.form['mfgdate'])
            htmlcolumn.append(request.form['discount'])
            htmlcolumn.append(request.form['freemed'])
            htmlcolumn.append(request.form['mrp'])
            htmlcolumn.append(request.form['pack'])
            htmlcolumn.append(request.form['tax_am'])
            htmlcolumn.append(request.form['cgst'])
            htmlcolumn.append(request.form['sgst'])
            htmlcolumn.append(request.form['amt'])
            htmlcolumn.append(request.form['rackno'])
            htmlcolumn.append(request.form['ddrugdept'])
            htmlcolumn.append(request.form['remark'])
            htmlcolumn.append(request.form['totalqty'])
            htmlcolumn.append(request.form['inventoryid'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolum
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)




##---Here we are inserting new distributor details----
def AddNewDistributor():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "distributor_detail"
    try:
        if request.method == 'POST':
            ##Name of database Attribute


            dbcolumn.append('distributor_name')
            dbcolumn.append('dist_type_id')
            dbcolumn.append('address')
            dbcolumn.append('emailid')
            dbcolumn.append('contact_no')
            dbcolumn.append('drug_license')
            dbcolumn.append('gst_no')
            dbcolumn.append('aadhar_no')
            dbcolumn.append('pancard_no')



            ##Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['distributor_name'])
            htmlcolumn.append(request.form['dist_type_id'])
            htmlcolumn.append(request.form['address'])
            htmlcolumn.append(request.form['emailid'])
            htmlcolumn.append(request.form['contact_no'])
            htmlcolumn.append(request.form['drug_license'])
            htmlcolumn.append(request.form['gst_no'])
            htmlcolumn.append(request.form['aadhar_no'])
            htmlcolumn.append(request.form['pancard_no'])


            ## Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


 ##----inserting values in outward_detail and MedicineOutwardDetail----

def Outward_detail_Insert():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "outward_detail"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('ward_id')
            dbcolumn.append('issued_date')
            dbcolumn.append('person_name')
            dbcolumn.append('time')
            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['issuedto'])
            htmlcolumn.append(request.form['issued_date'])
            htmlcolumn.append(request.form['person_name'])
            htmlcolumn.append(request.form['Entrytime'])
            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            #print("fgfg",result);
            if result == 1:
                sql = "SELECT LAST_INSERT_ID()";
                cursor.execute(sql)
                owtid = cursor.fetchall()[0][0]
                print("LASTID",owtid)
                dbcolumn = []
                htmlcolumn = []
                tablename = "medicine_outward_detail"
                row=len(request.form.getlist('inve_id')) #Has Multiple Value
                print("LENGHT",row)
                inv_id=request.form.getlist('inve_id') #Has Multiple Value
                Iqty = request.form.getlist('issuedqty') #Has Multiple Value
                row1=len(Iqty) #Has Multiple Value
                print("LENGHT",row1)
                for i in range(row):
                    dbcolumn = []
                    htmlcolumn = []
                    dbcolumn.append('outw_id')
                    dbcolumn.append('inv_id')
                    dbcolumn.append('issued_qty')
                    dbcolumn.append('fix_issued_qty')
                    htmlcolumn.append(str(owtid))
                    htmlcolumn.append(str(inv_id[i]))
                    htmlcolumn.append(str(Iqty[i]))
                    htmlcolumn.append(str(Iqty[i]))
                    result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                #print("tis is resylt",result)
                return result
    except Exception as e:
        print('I AM ERROR',str(e))
        return str(e)

##------updating  outward detail---

def Outward_detail_Update():
	dbcolumn = []
	htmlcolumn = []
	result=''
	tablename = "outward_detail"
	try:
		if request.method == 'POST':
            #Name of database Attribute
			dbcolumn.append('ward_id')
			dbcolumn.append('person_name')
			dbcolumn.append('time')
			dbcolumn.append('issued_date')

            #Name of html component e.g request.form['nameofcomponenet']
			htmlcolumn.append(request.form['issuedto'])
			htmlcolumn.append(request.form['person_name'])
			htmlcolumn.append(request.form['time'])
			htmlcolumn.append(request.form['issued_date'])
			result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
			return result
	except Exception as e:
		return str(e)

 ###-----retreiving data from outward_detail
def ViewUpdateOutwardDate():
	idateto=request.form['issued_dateto']
	idatefr=request.form['issued_datefrom']
	try:
		fields="select od.outw_id,od.issued_date,od.time,m.drugname,m.medicine_type,i.batch_no,i.expiry_date,i.manufacturing_date,w.wname,md.fix_issued_qty,od.person_name,md.meddet_id"
		joins= "from inventory_detail i,main_medicine m,admin_wardname w,outward_detail od,medicine_outward_detail md where m.med_id=i.med_id and i.inv_id=md.inv_id and md.outw_id = od.outw_id and od.ward_id=w.wid"
		filters= "and od.issued_date between '{}' and '{}'".format(idateto,idatefr)
		sql=fields+" "+joins+" "+filters
		print("date",sql)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

def ViewUpdateOutwardWard():
	idateto=request.form['issued_dateto']
	idatefr=request.form['issued_datefrom']
	wname=request.form['Wardname']
	try:
		fields="select od.outw_id,od.issued_date,od.time,m.drugname,m.medicine_type,i.batch_no,i.expiry_date,i.manufacturing_date,w.wname,md.fix_issued_qty,od.person_name,md.meddet_id"
		joins= "from inventory_detail i,main_medicine m,admin_wardname w,outward_detail od,medicine_outward_detail md where m.med_id=i.med_id and i.inv_id=md.inv_id and md.outw_id = od.outw_id and od.ward_id=w.wid"
		filters= " and od.issued_date between '{}' and '{}' and w.wid='{}'".format(idateto,idatefr,wname)
		sql=fields+" "+joins+" "+filters
		print("ward",sql)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

def ViewUpdateOutwardDrugname():
	dname=request.form['drugname']
	drugname,drugtype=dname.split('>')
	drugtype = drugtype[2:-1]
	print("HELLO ",drugname,drugtype)
	try:
		fields="select od.outw_id,od.issued_date,od.time,m.drugname,m.medicine_type,i.batch_no,i.expiry_date,i.manufacturing_date,w.wname,md.fix_issued_qty,od.person_name,md.meddet_id"
		joins= "from inventory_detail i,main_medicine m,admin_wardname w,outward_detail od,medicine_outward_detail md where m.med_id=i.med_id and i.inv_id=md.inv_id and md.outw_id = od.outw_id and od.ward_id=w.wid"
		filters= "and m.drugname='{}' and m.medicine_type='{}'".format(drugname,drugtype)
		sql=fields+" "+joins+" "+filters
		print("drugnam",sql)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

def getViewUpdateOutward():
    try:
        outw_id=request.form['outwardid']
        meddet_id=request.form['meddet_id']
        fields="select od.outw_id,od.issued_date, TIME_FORMAT(od.time,'%H:%i'),m.drugname,m.medicine_type,i.batch_no,i.expiry_date,i.manufacturing_date,w.wid,w.wname,md.fix_issued_qty,od.person_name,md.meddet_id,i.inv_id"
        joins= "from inventory_detail i,main_medicine m,admin_wardname w,outward_detail od,medicine_outward_detail md where m.med_id=i.med_id and i.inv_id=md.inv_id and md.outw_id = od.outw_id and od.ward_id=w.wid"
        filters= "and od.outw_id='{}' and md.meddet_id='{}'".format(outw_id,meddet_id)
        sql=fields+" "+joins+" "+filters
        print("ddete",sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#-----General search for medicine outward-----
def ShowByIssuedDate(issueddate):
    try :
        issuedfrom=request.form['issuedfrom']
        issuedto=request.form['issuedto']
        issueddate=issueddate+"OutwardIssuedDateList.xlsx"
        sql="Select od.outw_id, m.drugname,m.medicine_type,i.drugdept_type,a.wname,i.batch_no,i.pack,i.totalqty,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date,'%d-%m-%y'),i.amount,i.rack_no,md.issued_qty from inventory_detail i,main_medicine m ,admin_wardname a,outward_detail od,medicine_outward_detail md  where od.outw_id=md.outw_id and od.ward_id=a.wid and md.inv_id=i.inv_id and i.med_id=m.med_id and od.issued_date between '{}' and '{}'".format(issuedfrom,issuedto)
        print(sql)
        cursor.execute(sql)
        a=cursor.fetchall()
        #print("here is ur resulttttttyyyy ",a)

        workbook = Workbook(issueddate)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Ward Name",cell_format)
        sheet.write(0,5,"Batch Number",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalQuantity",cell_format)
        sheet.write(0,13,"IssuedQuantity",cell_format)
        sheet.write(0,8,"PerMRP",cell_format)
        sheet.write(0,9,"Unitprice",cell_format)
        sheet.write(0,10,"ExpiryDate",cell_format)
        sheet.write(0,11,"Amount",cell_format)
        sheet.write(0,12,"RackNumber",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)


def ShowByDrugName(viewdrugname):
    try :
        dname=request.form['drugname']
        issuedfrom=request.form['issuedfrom']
        issuedto=request.form['issuedto']
        viewdrugname=viewdrugname+"OutwardViewDrugnameList.xlsx"

        print("hhhh",dname);
        drugname,drugtype=dname.split(' >')
        drugtype = drugtype[2:-1]
        print("HELLO",drugname,drugtype)
        sql= "Select od.outw_id, m.drugname, m.medicine_type, i.drugdept_type, a.wname, i.batch_no, i.pack, i.totalqty, i.mrp,i.unitprice, DATE_FORMAT(i.expiry_date,'%d-%m-%y'), i.amount, i.rack_no,md.issued_qty from inventory_detail i, main_medicine m , admin_wardname a, outward_detail od, medicine_outward_detail md  where od.outw_id=md.outw_id and od.ward_id=a.wid and md.inv_id=i.inv_id and i.med_id=m.med_id and m.drugname like '%{}%' and m.medicine_type='{}' and od.issued_date between '{}' and'{}'".format(drugname,drugtype,issuedfrom,issuedto)
        print(sql)
        cursor.execute(sql)
        a=cursor.fetchall()

        workbook = Workbook(viewdrugname)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Ward Name",cell_format)
        sheet.write(0,5,"Batch Number",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalQuantity",cell_format)
        sheet.write(0,13,"IssuedQuantity",cell_format)
        sheet.write(0,8,"PerMRP",cell_format)
        sheet.write(0,9,"Unitprice",cell_format)
        sheet.write(0,10,"ExpiryDate",cell_format)
        sheet.write(0,11,"Amount",cell_format)
        sheet.write(0,12,"RackNumber",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)


def ShowByDrugType(viewdrugtype):
    try :
        drugtype=request.form['drugtype']
        issuedfrom=request.form['issuedfrom']
        issuedto=request.form['issuedto']

        viewdrugtype=viewdrugtype+"OutwardViewDrugTypeList.xlsx"

        sql="select od.outw_id  m.drugname, m.medicine_type, i.drugdept_type, a.wname,i.batch_no, i.pack, i.totalqty, i.mrp, i.unitprice, DATE_FORMAT(i.expiry_date,'%d-%m-%y'), i.amount, i.rack_no,md.issued_qty from inventory_detail i,main_medicine m ,admin_wardname a,outward_detail od,medicine_outward_detail md  where od.outw_id=md.outw_id and od.ward_id=a.wid and md.inv_id=i.inv_id and i.med_id=m.med_id and m.medicine_type='{}' and od.issued_date between '{}' and'{}'".format(drugtype,issuedfrom,issuedto)
        cursor.execute(sql)
        a=cursor.fetchall()
        workbook = Workbook(viewdrugtype)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Ward Name",cell_format)
        sheet.write(0,5,"Batch Number",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalQuantity",cell_format)
        sheet.write(0,13,"IssuedQuantity",cell_format)
        sheet.write(0,8,"PerMRP",cell_format)
        sheet.write(0,9,"Unitprice",cell_format)
        sheet.write(0,10,"ExpiryDate",cell_format)
        sheet.write(0,11,"Amount",cell_format)
        sheet.write(0,12,"RackNumber",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)


def ShowWardIssuedDate(viewbywardissueddate):
    try :
        issueddatefrom=request.form['issueddatefrom']
        issueddateto=request.form['issueddateto']
        issuedto=request.form['issuedto']
        viewbywardissueddate=viewbywardissueddate+"OutwardViewWardByissuedDateList.xlsx"

    	sql="select od.outw_id, m.drugname,m.medicine_type,i.drugdept_type,a.wname,i.batch_no,i.pack,i.totalqty,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date,'%d-%m-%y'),i.amount,i.rack_no,md.issued_qty from inventory_detail i,main_medicine m ,admin_wardname a,outward_detail od,medicine_outward_detail md where od.outw_id=md.outw_id and od.ward_id=a.wid and md.inv_id=i.inv_id and i.med_id=m.med_id and od.issued_date between '{}' and '{}'and a.wid='{}'".format(issueddatefrom,issueddateto,issuedto)
        print(sql)
        cursor.execute(sql)
        a=cursor.fetchall()

        workbook = Workbook(viewbywardissueddate)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Ward Name",cell_format)
        sheet.write(0,5,"Batch Number",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalQuantity",cell_format)
        sheet.write(0,13,"IssuedQuantity",cell_format)
        sheet.write(0,8,"PerMRP",cell_format)
        sheet.write(0,9,"Unitprice",cell_format)
        sheet.write(0,10,"ExpiryDate",cell_format)
        sheet.write(0,11,"Amount",cell_format)
        sheet.write(0,12,"RackNumber",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)

def ShowDetailsByGeneralSearchMedcineOutward():
    try:
        outw_id=request.form['outw_id']
        sql="select od.outw_id, m.drugname,m.medicine_type,i.drugdept_type,a.wname,i.batch_no,i.pack,i.quantity,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date,'%d-%m-%y'),i.amount,i.rack_no ,md.issued_qty from inventory_detail i,main_medicine m ,admin_wardname a,outward_detail od,medicine_outward_detail md  where od.outw_id=md.outw_id and od.ward_id=a.wid and md.inv_id=i.inv_id and i.med_id=m.med_id and outw_id='{}' ".format(outw_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

#-------------------general seacrh for inventory-----------
def ShowFullDetails(inventorystock):
    try :
        inventorystock=inventorystock+"InventoryFullStockSearch.xlsx"
        sql="Select i.inv_id,m.drugname,m.medicine_type,i.drugdept_type,i.batch_no,i.hsn_code,i.pack,i.quantity,i.rate,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),DATE_FORMAT(manufacturing_date,'%d-%m-%Y'),i.discount,i.free_med,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.remark,i.temp_quantity from inventory_detail i,main_medicine m where m.med_id=i.med_id  order by(expiry_date)"
        cursor.execute(sql)
        b=cursor.fetchall()


        workbook = Workbook(inventorystock)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'font_color': 'purple'})
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Batch Number",cell_format)
        sheet.write(0,5,"HSN Code",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalStrip",cell_format)
        sheet.write(0,21,"TotalQuantity",cell_format)
        sheet.write(0,8,"Rate",cell_format)
        sheet.write(0,9,"MRP",cell_format)
        sheet.write(0,10,"Unitprice",cell_format)
        sheet.write(0,11,"ExpiryDate",cell_format)
        sheet.write(0,12,"Manufacturing Date",cell_format)
        sheet.write(0,13,"Discount",cell_format)
        sheet.write(0,14,"FreeMedicine",cell_format)
        sheet.write(0,15,"TaxableAmount",cell_format)
        sheet.write(0,16,"CGST%",cell_format)
        sheet.write(0,17,"SGST%",cell_format)
        sheet.write(0,18,"Amount",cell_format)
        sheet.write(0,19,"RackNumber",cell_format)
        sheet.write(0,20,"Remark",cell_format)

        for r, row in enumerate(b):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return b
    except Exception as e:
        return str(e)


def ShowByEntryDate(entrydatesearch):
    try :
        entrydatefrom=request.form['entrydatefrom']
        entrydateto=request.form['entrydateto']
        entrydatesearch=entrydatesearch+"InventoryEntryDateSearch.xlsx"
        print("i am path=",entrydatesearch)
        sql="Select i.inv_id,m.drugname,m.medicine_type,i.drugdept_type,i.batch_no,i.hsn_code,i.pack,i.quantity,i.rate,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),DATE_FORMAT(manufacturing_date,'%d-%m-%Y'),i.discount,i.free_med,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.remark,i.temp_quantity,d.distributor_name from inventory_detail i,main_medicine m,distributor_detail d where d.distdet_id=i.distdet_id and m.med_id=i.med_id and i.date between '{}' and '{}' order by(i.expiry_date)".format(entrydatefrom,entrydateto)
        print("i am sql=",sql)
        cursor.execute(sql)
        a=cursor.fetchall()

        workbook = Workbook(entrydatesearch)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Batch Number",cell_format)
        sheet.write(0,5,"HSN Code",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalStrip",cell_format)
        sheet.write(0,21,"TotalQuantity",cell_format)
        sheet.write(0,8,"Rate",cell_format)
        sheet.write(0,9,"MRP",cell_format)
        sheet.write(0,10,"Unitprice",cell_format)
        sheet.write(0,11,"ExpiryDate",cell_format)
        sheet.write(0,12,"Manufacturing Date",cell_format)
        sheet.write(0,13,"Discount",cell_format)
        sheet.write(0,14,"FreeMedicine",cell_format)
        sheet.write(0,15,"TaxableAmount",cell_format)
        sheet.write(0,16,"CGST%",cell_format)
        sheet.write(0,17,"SGST%",cell_format)
        sheet.write(0,18,"Amount",cell_format)
        sheet.write(0,19,"RackNumber",cell_format)
        sheet.write(0,20,"Remark",cell_format)
        sheet.write(0,22,"DistributorName",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)


def ShowByExpiry(expiry):
    try :
        expiryfrom=request.form['expiryfrom']
        expiryto=request.form['expiryto']
        expiry=expiry+"InventoryExpirySearch.xlsx"
        sql="Select i.inv_id,m.drugname,m.medicine_type,i.drugdept_type,i.batch_no,i.hsn_code,i.pack,i.quantity,i.rate,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),DATE_FORMAT(manufacturing_date,'%d-%m-%Y'),i.discount,i.free_med,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.remark,i.temp_quantity from inventory_detail i,main_medicine m where m.med_id=i.med_id and i.expiry_date between '{}' and '{}' order by(expiry_date)".format(expiryfrom,expiryto)
        cursor.execute(sql)
        b=cursor.fetchall()


        workbook = Workbook(expiry)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'font_color': 'purple'})
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Batch Number",cell_format)
        sheet.write(0,5,"HSN Code",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalStrip",cell_format)
        sheet.write(0,21,"TotalQuantity",cell_format)
        sheet.write(0,8,"Rate",cell_format)
        sheet.write(0,9,"MRP",cell_format)
        sheet.write(0,10,"Unitprice",cell_format)
        sheet.write(0,11,"ExpiryDate",cell_format)
        sheet.write(0,12,"Manufacturing Date",cell_format)
        sheet.write(0,13,"Discount",cell_format)
        sheet.write(0,14,"FreeMedicine",cell_format)
        sheet.write(0,15,"TaxableAmount",cell_format)
        sheet.write(0,16,"CGST%",cell_format)
        sheet.write(0,17,"SGST%",cell_format)
        sheet.write(0,18,"Amount",cell_format)
        sheet.write(0,19,"RackNumber",cell_format)
        sheet.write(0,20,"Remark",cell_format)

        for r, row in enumerate(b):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return b
    except Exception as e:
        return str(e)

def ShowByDeptNameExpiry(Deptname_xpiry):
    try :
        expiryFrom=request.form['expiryFrom']
        expiryTo=request.form['expiryTo']
        deptname=request.form['ddrugdept']
        Deptname_xpiry=Deptname_xpiry+"InventoryDeptnamExpirySearch.xlsx"
    	sql="Select i.inv_id,m.drugname,m.medicine_type,i.drugdept_type,i.batch_no,i.hsn_code,i.pack,i.quantity,i.rate,i.mrp,i.unitprice,DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),DATE_FORMAT(manufacturing_date,'%d-%m-%Y'),i.discount,i.free_med,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.remark,i.temp_quantity from inventory_detail i,main_medicine m where m.med_id=i.med_id and i.expiry_date between '{}' and '{}' and i.drugdept_type='{}'order by(expiry_date)".format(expiryFrom,expiryTo,deptname)
        print("i am sqllllll=",sql)
        cursor.execute(sql)
        a=cursor.fetchall()
        print(a)

        workbook = Workbook(Deptname_xpiry)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Drug Issued To Department",cell_format)
        sheet.write(0,4,"Batch Number",cell_format)
        sheet.write(0,5,"HSN Code",cell_format)
        sheet.write(0,6,"PackQuantity",cell_format)
        sheet.write(0,7,"TotalStrip",cell_format)
        sheet.write(0,21,"TotalQuantity",cell_format)
        sheet.write(0,8,"Rate",cell_format)
        sheet.write(0,9,"MRP",cell_format)
        sheet.write(0,10,"Unitprice",cell_format)
        sheet.write(0,11,"ExpiryDate",cell_format)
        sheet.write(0,12,"Manufacturing Date",cell_format)
        sheet.write(0,13,"Discount",cell_format)
        sheet.write(0,14,"FreeMedicine",cell_format)
        sheet.write(0,15,"TaxableAmount",cell_format)
        sheet.write(0,16,"CGST%",cell_format)
        sheet.write(0,17,"SGST%",cell_format)
        sheet.write(0,18,"Amount",cell_format)
        sheet.write(0,19,"RackNumber",cell_format)
        sheet.write(0,20,"Remark",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)



def ShowDetailsByGeneralSearchInventory():
    try :
        inv_id=request.form['inventoryid']
        sql="Select  i.inv_id,m.drugname,m.medicine_type,i.drugdept_type,i.batch_no,i.hsn_code,i.pack,i.quantity,i.rate,i.mrp,i.unitprice,i.expiry_date,i.manufacturing_date,i.discount,i.free_med,i.taxable_amt,i.cgst,i.sgst,i.amount,i.rack_no,i.remark,i.temp_quantity from inventory_detail i,main_medicine m where m.med_id=i.med_id and i.inv_id='{}' ".format(inv_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return str(e)



##----updating medicine_outward_detail,outward_detail  for updating records while issuing medicines to Outward_detail_Insert
def UpdateOutwardMedicineDetail():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "outward_detail"
    try:
        if request.method == 'POST':
            dbcolumn.append('time')
            dbcolumn.append('issued_date')
            dbcolumn.append('ward_id')
            dbcolumn.append('person_name')
            dbcolumn.append('outw_id')
            htmlcolumn.append(request.form['time'])
            htmlcolumn.append(request.form['issueddate'])
            htmlcolumn.append(request.form['wardid'])
            htmlcolumn.append(request.form['personname'])
            htmlcolumn.append(request.form['outwardid'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolum
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            print("inside outward",result)
            if result==1:
                dbcolumn = []
                htmlcolumn = []
                result=''
                tablename = "medicine_outward_detail"
                dbcolumn.append('issued_qty')
                dbcolumn.append('fix_issued_qty')
                dbcolumn.append('inv_id')
                dbcolumn.append('meddet_id')
                htmlcolumn.append(request.form['fix_issued_qty'])
                htmlcolumn.append(request.form['fix_issued_qty'])
                htmlcolumn.append(request.form['inv_id'])
                htmlcolumn.append(request.form['meddet_id'])
                result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                return result
                print("medicne outward",result)
    except Exception as e:
		return str(e)


###-----updating  inventory table in context to outward table
def MedicineOutwardInventoryUpdate():
	dbcolumn = []
	htmlcolumn = []
	result=''
	tablename = "inventory_detail"
	row=len(request.form.getlist('remainingqty'))
	inv_id = request.form.getlist('inve_id')#Has Multiple Value
	print(inv_id);
	remqty= request.form.getlist('remainingqty') #Has Multiple Value
	print(remqty);

	try:
		if request.method == 'POST':
			for i in range(row):
					dbcolumn = []
					htmlcolumn = []
					dbcolumn.append('temp_quantity')
					dbcolumn.append('inv_id')

					htmlcolumn.append(remqty[i])
					htmlcolumn.append(inv_id[i])

					result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
					print(result);
			return result
	except Exception as e:
		return str(e)

###-----------getting drug detail from inventory in outward---

def GetDrugDetailList():
	try:
		medname=request.form['medname']
		medtype=request.form['medtype']
		sql="Select i.inv_id,m.drugname,m.medicine_type,i.batch_no,DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),DATE_FORMAT(i.manufacturing_date, '%d-%m-%Y'),i.rate,i.temp_quantity,i.temp_quantity  from inventory_detail i,main_medicine m where m.med_id =i.med_id and i.temp_quantity>0 and m.medicine_type='{}' and m.drugname like '{}%'".format(medtype,medname)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

##---get all ward names
def GetAllWardName():
	try:
		sql="Select * from admin_wardname where deletestatus=0 Order by wname ASC"
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)


##---here we are fetching all distributor type
def GetAllDistributorType():
	try:
		sql="Select  * from distributor_type_detail"
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

##---here we are fetching all distributor name
def GetAll_DistributorName(dist_type_id):
	try:
		sql="select distdet_id,distributor_name from distributor_detail where dist_type_id='{}'".format(dist_type_id)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

def getDistributorAllData(distributor_id):
	try:
		sql="select dn.*,dt.dist_type_name from distributor_detail dn,distributor_type_detail dt where dn.dist_type_id = dt.dist_type_id AND deletestatus='0' AND dn.distdet_id='{}'".format(distributor_id)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)



#----here we are getting all drugname--
def getDrugname():

    hint = str(request.form['drugname'])
    arr_rows=[]
    if len(hint)>=1:
        sql = "select drugname,UPPER(medicine_type) from main_medicine where drugname LIKE '{}%'".format(hint)
        print(sql)
        cursor.execute(sql)
        dt = cursor.fetchall()
        for i in range(0,len(dt)):
            med = dt[i][0] + " > [" + dt[i][1] + "]"
            arr_rows.append(med)
            print("hello s",arr_rows);
        return arr_rows
    else:
        return arr_rows


#----here we are separating drug name and drug type

def getDrugTypeName(drugtype):
	arr_data=[]
	print('HELLO',drugtype)
	drugname,drugtype=drugtype.split('>')
	drugtype = drugtype[2:-1]
	try:
		sql = "select med_id,drugname,UPPER(medicine_type) from main_medicine where drugname='{}' AND medicine_type='{}' ".format(drugname,drugtype)
		cursor.execute(sql)
		drugdata =cursor.fetchall()
		arr_data.append(str(drugdata[0][0]))
		arr_data.append(drugdata[0][1])
		arr_data.append(drugdata[0][2])

		return arr_data

	except Exception as e:
		return str(e)




#----here we update distributor details
def UpdateDistributor():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "distributor_detail"
    try:
        if request.method == 'POST':
            ##Name of database Attribute


            dbcolumn.append('distributor_name')
            dbcolumn.append('dist_type_id')
            dbcolumn.append('address')
            dbcolumn.append('emailid')
            dbcolumn.append('contact_no')
            dbcolumn.append('drug_license')
            dbcolumn.append('gst_no')
            dbcolumn.append('aadhar_no')
            dbcolumn.append('pancard_no')
            dbcolumn.append('distdet_id')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            ##Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['distributor_name'])
            htmlcolumn.append(request.form['dis_type_name'])
            htmlcolumn.append(request.form['address'])
            htmlcolumn.append(request.form['emailid'])
            htmlcolumn.append(request.form['contact_no'])
            htmlcolumn.append(request.form['drug_license'])
            htmlcolumn.append(request.form['gst_no'])
            htmlcolumn.append(request.form['aadhar_no'])
            htmlcolumn.append(request.form['pancard_no'])
            htmlcolumn.append(request.form['distributor_id'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"



            # Here we are calling UpdateData that have a  common  code for insert record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            print(result)
            return result
    except Exception as e:
        return str(e)


#-----adding new distributor type(admin panel)
def AddDistributorType():
	dbcolumn = []
	htmlcolumn = []
	result=''
	tablename = "distributor_type_detail"
	try:
		if request.method == 'POST':
			##Name of database Attribute
			dbcolumn.append('dist_type_name')

			##Name of html component e.g request.form['nameofcomponenet']
			htmlcolumn.append(request.form['dist_type_name'])
			result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
			return result
	except Exception as e:
		return str(e)


#----------- SELECTING ALL MEDICINE WITH ASSOCIATED INVENTORY DATA WITHOUT FILTER---
def getAllMedicineNoFilter():
    drugname=request.form['drugname']
    arr_rows=[]

    try:
        if len(drugname)>=1:
            sql="Select i.inv_id,m.drugname,m.medicine_type,i.batch_no,DATE_FORMAT(i.expiry_date, '%d/%m/%Y'),DATE_FORMAT(i.manufacturing_date, '%d/%m/%Y'),i.temp_quantity from inventory_detail i,main_medicine m where i.med_id=m.med_id and m.drugname  like '{}%'".format(drugname)
            print(sql)
            cursor.execute(sql)
            outdata=cursor.fetchall()
            for i in range(0,len(outdata)):
                med = str(outdata[i][0]) + " >  " +outdata[i][1] + " > [" + outdata[i][2] + "] >  Batch No: "+ outdata[i][3]+ " > Expiry Date: "+ outdata[i][4]+ " > MFG Date: "+ outdata[i][5]
                arr_rows.append(med)
            print("MYDATA   ",arr_rows)
            return arr_rows
        else:
            return arr_rows
    except Exception as e:
        print("I AM ERROR ", str(e))
        return str(e)

##----medicine return by wards (here we first insert into medicine_return table then we update inventory(temp_quantity) and medicine_outward_detail (issuedqty))---
def MedicineReturnByWard():
     dbcolumn = []
     htmlcolumn = []
     result=''
     tablename = "medicine_return"
     try:
         if request.method == 'POST':
             dbcolumn.append('wardname')
             dbcolumn.append('date')
             dbcolumn.append('person_name')
             dbcolumn.append('return_qty')
             dbcolumn.append('inv_id')

             htmlcolumn.append(request.form['issuedto'])
             htmlcolumn.append(request.form['returndate'])
             htmlcolumn.append(request.form['personname'])
             htmlcolumn.append(request.form['returnquantity'])
             htmlcolumn.append(request.form['inventoryid'])

             result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
             print("insert query",result)
             if result==1:
                 dbcolumn = []
                 htmlcolumn = []
                 result=''
                 tablename = "medicine_outward_detail"
                 dbcolumn.append('issued_qty')
                 dbcolumn.append('inv_id')
                 dbcolumn.append('meddet_id')

                 htmlcolumn.append(request.form['issuedquantity'])
                 htmlcolumn.append(request.form['inventoryid'])
                 htmlcolumn.append(request.form['meddet_id'])
                 print("HTML",htmlcolumn)
                 result1 = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                 print("first update",result1)
                 if result1==1:
                      dbcolumn = []
                      htmlcolumn = []
                      result=''
                      tablename = "inventory_detail"
                      dbcolumn.append('temp_quantity')
                      dbcolumn.append('inv_id')

                      htmlcolumn.append(request.form['tempqty'])
                      htmlcolumn.append(request.form['inventoryid'])
                      result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
                      return result1
     except Exception as e:
         return str(e)

#-----select query to retreive data when medicine is returned----
def RetrieveData():
    drugname=request.form['drugname1']
    wname=request.form['issuedto']
    arr_rows=[]
    #print("wc")
    try:
        if len(drugname)>=1:
            sql="select m.drugname,m.medicine_type,md.issued_qty ,i.batch_no,i.inv_id,i.temp_quantity,md.meddet_id from medicine_outward_detail md,outward_detail od,inventory_detail i,admin_wardname a,main_medicine m where md.outw_id=od.outw_id and md.inv_id=i.inv_id and i.med_id=m.med_id and md.issued_qty >0 and  od.ward_id=a.wid and od.ward_id='{}' and m.drugname like '{}%'".format(wname,drugname)
            print("AAA",sql)
            cursor.execute(sql)
            outdata=cursor.fetchall()

            for i in range(0,len(outdata)):
                med = outdata[i][0] + " > [" +outdata[i][1] + "] >Issuedqty: " + outdata[i][2] + " > Batchno: " + outdata[i][3]+ ">invid:"+ str(outdata[i][4])+">tempqty:"+str(outdata[i][5])+">meddetid:"+str(outdata[i][6])
                #print("hi there",med)
                arr_rows.append(med)
                #print(arr_rows)
            return arr_rows
        else:
            return arr_rows
    except Exception as e:
        return str(e)

##----Medicine return search for date ---
def MedicineReturnByDateSearch(returndate):
    returndatefrom=request.form['returndatefrom']
    returndateto=request.form['returndateto']
    returndate=returndate+"MedicineReturnDateList.xlsx"

    try:
        sql="select mr.medret_id,m.drugname,m.medicine_type,i.batch_no,mr.person_name,a.wname,mr.return_qty from inventory_detail i,main_medicine m,medicine_return mr,admin_wardname a where mr.inv_id=i.inv_id and mr.wardname=a.wid and i.med_id=m.med_id and  mr.date between '{}' and '{}'".format(returndatefrom,returndateto)
        cursor.execute(sql)
        a=cursor.fetchall()
        workbook = Workbook(returndate)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Batch Number",cell_format)
        sheet.write(0,4,"PersonName",cell_format)
        sheet.write(0,5,"Ward Name",cell_format)
        sheet.write(0,6,"ReturnQuantity",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)

def MedicineReturnByWardDateSearch(returnward):
    wardname=request.form['wardname']
    print(wardname)
    returndatefrom=request.form['returndatefrom']
    print(returndatefrom)
    returndateto=request.form['returndateto']
    print(returndateto)
    returnward=returnward+"MedicineReturnDateWardList.xlsx"

    try:
        sql="select mr.medret_id,m.drugname,m.medicine_type,i.batch_no,mr.person_name,a.wname,mr.return_qty from inventory_detail i,main_medicine m,medicine_return mr,admin_wardname a where mr.inv_id=i.inv_id and mr.wardname=a.wid and i.med_id=m.med_id and mr.wardname ='{}' and mr.date between '{}' and '{}'".format(wardname,returndatefrom,returndateto)
        print(sql)
        cursor.execute(sql)
        a=cursor.fetchall()
        workbook = Workbook(returnward)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'font_color': 'purple'})
        sheet.write(0,0,"Id",cell_format)
        sheet.write(0,1,"Drug Name",cell_format)
        sheet.write(0,2,"Drug Type",cell_format)
        sheet.write(0,3,"Batch Number",cell_format)
        sheet.write(0,4,"PersonName",cell_format)
        sheet.write(0,5,"Ward Name",cell_format)
        sheet.write(0,6,"ReturnQuantity",cell_format)

        for r, row in enumerate(a):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return a
    except Exception as e:
        return str(e)

def showDetailsByGeneralSearchMedicineReturn():
    medret_id=request.form['medret_id']
    try:
        sql="select mr.medret_id,m.drugname,m.medicine_type,i.batch_no,mr.person_name,a.wname,mr.return_qty from inventory_detail i,main_medicine m,medicine_return mr,admin_wardname a where mr.inv_id=i.inv_id and mr.wardname=a.wid and i.med_id=m.med_id and  mr.medret_id='{}'".format(medret_id)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
       return str(e)






##----geting data for notification (expiry alert and stock alert(minimum and maximum))
def checkForExpiry():
    result=''
    tablename = "notification"
    try:
        sql="select * from notification where filter_type='Expiry' and flag=0"
        cursor.execute(sql)
        noti=cursor.fetchall()
        print("NOTI",len(noti))
        sql="Select i.inv_id from inventory_detail i,main_medicine m where i.med_id=m.med_id and DATEDIFF(expiry_date,CURRENT_TIMESTAMP) between 0 and 90"
        cursor.execute(sql)
        expdata=cursor.fetchall()
        a=0
        if len(noti) == 0:
            for i in range(len(expdata)):
                print("inside if")
                htmlcolumn = []
                dbcolumn = []
                dbcolumn.append('inv_id')
                dbcolumn.append('filter_type')
                htmlcolumn.append(str(expdata[i][0]))
                htmlcolumn.append("Expiry")
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                a=a+1
        else:
            for i in range(len(expdata)):
                print("inside else")
                if i <= len(noti):
                    if expdata[i][0]!=noti[i][1]:
                        htmlcolumn = []
                        dbcolumn = []
                        dbcolumn.append('inv_id')
                        dbcolumn.append('filter_type')
                        htmlcolumn.append(str(expdata[i][0]))
                        htmlcolumn.append("Expiry")
                        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                        a=a+1
                else:
                        htmlcolumn = []
                        dbcolumn = []
                        dbcolumn.append('inv_id')
                        dbcolumn.append('filter_type')
                        htmlcolumn.append(str(expdata[i][0]))
                        htmlcolumn.append("Expiry")
                        result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
                        a=a+1
        return a
    except Exception as e:
        return str(e)

def getDataNotificationPageExpiry(NotPageExpiry):
    try:
        NotPageExpiry=NotPageExpiry+"NotExpirySearchList.xlsx"

        print("DSDDSDDSDSSDSDSDD")
    	startpart = "Select drugname,medicine_type,i.batch_no,DATE_FORMAT(i.manufacturing_date,'%d-%m-%Y'),DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),i.temp_quantity,i.rack_no,"
    	tempstr=''
    	xtotal = ''
        allwardname = wrd.getAllWardData()
    	for i in range(0,len(allwardname)):
    		print(str(allwardname[i][0]))
    		wardnames = "case when wid="+str(allwardname[i][0])+" then md.issued_qty else '0' end "
    		if i == 0:
    			xtotal = xtotal +"case when wid="+str(allwardname[i][0])+" then md.issued_qty else '0' end"
    		else:
    			xtotal = xtotal +"+case when wid="+str(allwardname[i][0])+" then md.issued_qty else '0' end"
    		tempstr =tempstr+wardnames+","

    	endpart = xtotal+"+i.temp_quantity from inventory_detail i,main_medicine m,admin_wardname a ,outward_detail od,medicine_outward_detail md where i.med_id=m.med_id and i.inv_id=md.inv_id and md.outw_id=od.outw_id and od.ward_id=a.wid and DATEDIFF(i.expiry_date,CURRENT_TIMESTAMP) between 0 and 90 order by i.expiry_date desc"
    	sql = startpart+tempstr+endpart
    	print("I AM SQL",sql)

    	cursor.execute(sql)
        b=cursor.fetchall()


        workbook = Workbook(NotPageExpiry)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'font_color': 'purple'})
        sheet.write(0,0,"Drug Name",cell_format)
        sheet.write(0,1,"Drug Type",cell_format)
        sheet.write(0,2,"Batch Number",cell_format)
        sheet.write(0,3,"Manufacturing Date",cell_format)
        sheet.write(0,4,"ExpiryDate",cell_format)
        sheet.write(0,5,"Current Quantity In store",cell_format)
        sheet.write(0,6,"RackNumber",cell_format)
        for i in range(0,len(allwardname)):
            sheet.write(0,i+7,allwardname[i][1],cell_format)
        sheet.write(0,i+8,"TotalQuantity",cell_format)

        for r, row in enumerate(b):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return b
    except Exception as e:
        return str(e)

def getMedicineExpiryCount(NotPageMedicineCount):
    try:
        NotPageMedicineCount=NotPageMedicineCount+"MedicneStoreExpirySearchList.xlsx"
        sql="Select drugname,medicine_type,i.batch_no,DATE_FORMAT(i.manufacturing_date,'%d-%m-%Y'),DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),i.temp_quantity,i.rack_no   from inventory_detail i,main_medicine m where i.med_id=m.med_id  and DATEDIFF(expiry_date,CURRENT_TIMESTAMP) between 0 and 90 order by expiry_date desc"
        print(sql)
        cursor.execute(sql)
        b=cursor.fetchall()


        workbook = Workbook(NotPageMedicineCount)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'font_color': 'purple'})
        sheet.write(0,0,"Drug Name",cell_format)
        sheet.write(0,1,"Drug Type",cell_format)
        sheet.write(0,2,"Batch Number",cell_format)
        sheet.write(0,3,"Manufacturing Date",cell_format)
        sheet.write(0,4,"ExpiryDate",cell_format)
        sheet.write(0,5,"Current Quantity In store",cell_format)
        sheet.write(0,6,"RackNumber",cell_format)


        for r, row in enumerate(b):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        print("ggggggggggggggghkjkl",b)
        return b
    except Exception as e:
        return str(e)



def getDataNotificationPageMinValue(NotPageMinVal):
    try:
        NotPageMinVal=NotPageMinVal+"NotMinValueSearchList.xlsx"
        sql="select drugname,medicine_type,i.batch_no,DATE_FORMAT(manufacturing_date,'%d-%m-%Y'),DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),i.rack_no,sum(i.temp_quantity), m.min_value  from main_medicine m, inventory_detail i where i.med_id =m.med_id group by(i.med_id) having sum(i.temp_quantity) < m.min_value order by expiry_date"

        cursor.execute(sql)
        b=cursor.fetchall()


        workbook = Workbook(NotPageMinVal)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'font_color': 'purple'})
        sheet.write(0,0,"Drug Name",cell_format)
        sheet.write(0,1,"Drug Type",cell_format)
        sheet.write(0,2,"Batch Number",cell_format)
        sheet.write(0,3,"Manufacturing Date",cell_format)
        sheet.write(0,4,"ExpiryDate",cell_format)
        sheet.write(0,5,"RackNumber",cell_format)
        sheet.write(0,6,"Current Quantity In store",cell_format)
        sheet.write(0,7,"Minimum Value",cell_format)


        for r, row in enumerate(b):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return b
    except Exception as e:
        return str(e)

def getDataNotificationPageMaxValue(NotPageMaxVal):
    try:
        NotPageMaxVal=NotPageMaxVal+"NotMaxValueSearchList.xlsx"
        sql="select drugname,medicine_type,i.batch_no,DATE_FORMAT(manufacturing_date,'%d-%m-%Y'),DATE_FORMAT(i.expiry_date, '%d-%m-%Y'),i.rack_no,sum(i.temp_quantity), m.max_value  from main_medicine m, inventory_detail i where i.med_id =m.med_id group by(i.med_id) having sum(i.temp_quantity) > m.max_value order by expiry_date"
        cursor.execute(sql)
        b=cursor.fetchall()


        workbook = Workbook(NotPageMaxVal)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'font_color': 'purple'})
        sheet.write(0,0,"Drug Name",cell_format)
        sheet.write(0,1,"Drug Type",cell_format)
        sheet.write(0,2,"Batch Number",cell_format)
        sheet.write(0,3,"Manufacturing Date",cell_format)
        sheet.write(0,4,"ExpiryDate",cell_format)
        sheet.write(0,5,"RackNumber",cell_format)
        sheet.write(0,6,"Current Quantity In store",cell_format)
        sheet.write(0,7,"Maximum Value",cell_format)

        for r, row in enumerate(b):
            for c, col in enumerate(row):
                sheet.write(r+1, c, col)
        workbook.close()
        return b
    except Exception as e:
        return str(e)

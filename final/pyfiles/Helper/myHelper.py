from werkzeug.security import generate_password_hash,check_password_hash
from mysql.connector import Error

#This method returns the homepage of a given usertype
#If the user is clerk then this method also returns the no. of pending reimbersement requests
def getUserHomePage(session):
	print("SESSION= ",session)
	if session['usertype']==str('staff').upper():
		return '/mainpage/mainpage.html'
	else:
		return '/login/login.html'

def fetch_results(cursor,sql):
	results={}
	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		print(results)
		if(cursor.rowcount<=0):
			print("msg=0")
			msg=0	#this means that there are no completed requests
		else:
			print("msg=1")
			msg=1	#means we have results
	except Error as e:
		print(e)
		msg=-1	# this impleies there is an error in database
	return results,msg

from imaplib import IMAP4_SSL 
from datetime import date,timedelta,datetime 
from time import mktime 
from email.utils import parsedate 
from pylab import plot_date,show,xticks,date2num 
from pylab import figure,hist,num2date 
from matplotlib.dates import DateFormatter
import pygal

def getHeaders(address,password,folder,d):
	"""Retrive headers of Email from d-days from now   """
	
# Let's make an iMap connection 

	mail = IMAP4_SSL('imap.gmail.com') 
	mail.login(address,password)
	mail.select(folder)
	
	#uid - Unique ID
	
	interval = (date.today()-timedelta(d)).strftime("%d-%b-%y") #first we got today's date(date.today() is inbuilt time function) then timedelta(d) 
	
#	interval = date.today()-timedelt.strftime("%d-%b-%y")

#to get data one week later we will put date.today()-timedeldta(d) where d= 7
	
	result, data = mail.uid('search', None, 
                      '(SENTSINCE {date})'.format(date=interval))
	
	#retriving the headers
	
	result, data = mail.uid('fetch', data[0].replace(' ',','), 
	                         '(BODY[HEADER.FIELDS (DATE)])')


	mail.close()
	mail.logout()
	print data[0]
	
def diurnalPlot(headers):

	"""diurnal plot of emails, with years running along x axis and times of day on the Y axis """

	xday = []
	ytime= []

	for h in headers:

		if len(h) > 1: 
		
		#	timestamp = mktime(parsedate(h[1][5:].replace('.',':')))
		
# mktime is an inbuilt function, "from time import mktime"

		
			timestamp = mktime(parsedate(h[1][5:].replace('.',':'))) 
		        mailstamp = datetime.fromtimestamp(timestamp)
			
                        xday.append(mailstamp)
		
		#Time the Email is arrived
		
			y = datetime(2010,10,14,mailstamp.hour,mailstamp.minute,mailstamp.second)
			ytime.append(y)
		
	plot_date(xday,ytime,'.',alpha=.7)
	xticks(rotation=30)
	return xday,ytime


def dailyDistributioPlot(ytime):
 """ draw the histogram of the daily distribution """
 # converting dates to numbers
 numtime = [date2num(t) for t in ytime] 
 # plotting the histogram
 ax = figure().gca()
 _, _, patches = hist(numtime, bins=24,alpha=.5)
 # adding the labels for the x axis
 tks = [num2date(p.get_x()) for p in patches] 
 xticks(tks,rotation=75)
 # formatting the dates on the x axis
 ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
 
# ytime = []
# timestamp = mktime(parsedate(h[1][5:].replace('.',':')))
# mailstamp = datetime.fromtimestamp(timestamp)
# xday.append(mailstamp)
# y = datetime(2010,10,14,mailstamp.hour,mailstamp.minute,mailstamp.second)
# ytime.append(y)
		
		 

	
print 'Fetching emails'


headers = getHeaders('arsh840@gmail.com','Mypassword','inbox',5)

#print headers

#print len(data)

xday = []
ytime= []


for h in headers:
    if len(h)>1:
         
        timestamp = mktime(parsedate(h[1][5:].replace('.',':'))) 
        mailstamp = datetime.fromtimestamp(timestamp)    
         
        print timestamp
        print mailstamp



#         xday.append(mailstamp)
#	  y = datetime(2010,10,14,mailstamp.hour,mailstamp.minute,mailstamp.second)
 #         ytime.append(y)
  #        numtime = [date2num(t) for t in ytime]
#          print numtime
          
#          print ytime				


#print 'plotting some Statictics'

#xday,ytime = diurnalPlot(headers)

#dailyDistributioPlot(ytime)

#print len(xday), 'Emails Analysed'

#print ytime
#print 

#print xday

#show()


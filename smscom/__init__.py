
import httplib2
import urllib
import getopt
import sys

class SMSClient():
    def __init__(self,acc,apikey): 
        self.acc = acc
        self.apikey = apikey

    def send(self,msg,sender,to,prio=2):
        h = httplib2.Http()
        query = urllib.urlencode({'msg': msg,'acc': self.acc,'pass': self.apikey,'from':sender,'prio':prio,'to':to})
        r,c = h.request("https://web.smscom.se/sendsms.aspx?%s" % query)
        print r 

def main():
    try:
        opts,args = getopt.getopt(sys.argv[1:],'a:k:m:f:t:P')
    except getopt.error,msg:
        print msg
	print __doc__
	sys.exit(2)

    acc = None
    apikey = None
    sender = None
    to = None
    prio = 2
    msg = None
    try:
	for o,a in opts:
	    if o in '-a':
	        acc = a
            elif o in '-k':
                apikey = a
            elif o in '-m':
                msg = a
            elif o in '-P':
                prio = a
            elif o in '-t':
                to = a
	    elif o in '-f':
                sender = a
            else:
		raise ValueError("what about %s?" % o)
    except Exception,ex:
        print ex
        print __doc__
        sys.exit(3)

    sms = SMSClient(acc=acc,apikey=apikey)
    sms.send(msg=msg,to=to,sender=sender,prio=prio) 

if __name__ == "__main__":
    main()


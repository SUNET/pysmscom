"""
Module that implements SMS using ip1 SMS service.
"""

import httplib2
import urllib
import getopt
import sys


class SMSClient(object):
    """
    Class that implements SMS using ip1 SMS service.
    """
    status_codes = {
        '0': 'Delivered to gateway',
        '1': 'Gateway login failed',
        '2': 'Invalid message content',
        '3': 'Invalid phone number format',
        '4': 'Insufficient funds',
        '10': 'Received by the gateway',
        '11': 'Delayed delivery',
        '12': 'Delayed delivery cancelled',
        '21': 'Delivered to the GSM network',
        '22': 'Delivered to the phone',
        '30': 'Insufficient funds',
        '41': 'Invalid message content',
        '42': 'Internal error',
        '43': 'Delivery failed',
        '50': 'General delivery error',
        '51': 'Delivery to GSM network failed',
        '52': 'Delivery to phone failed',
        '100': 'Insufficient credits',
        '101': 'Wrong account credentials',
        '110': 'Parameter error'
    }

    def __init__(self, acc, apikey):
        """
        @param acc: ip1 service account name
        @type acc: str
        @param apikey: ip1 service password
        @type apikey: str
        """
        self.acc = acc
        self.apikey = apikey

    def send(self, msg, sender, to, prio=2):
        """
        Send SMS message to sender.

        @param msg: The message. If the message is over 160 characters the message will be split into multipe SMS
        messages, if the message is 161 characters you will be charged for two messages.
        @type msg: str
        @param sender: Phone number or a text string of max 11 characters.
        @type sender: str
        @param to: Mobile phone number in E.164 format ie (+46xxxxxxxx)
        @type to: str
        @param prio: (optional) SMS urgency priority, possible values 1 (Group messages), 2 (Normal), 3 (Urgent).
        default is 2
        @return Return True if delivery was successful, if an error occurred with the SMS service a status message
        is returned. If an httplib error occur the httplib response object is returned.
        """
        http = httplib2.Http()
        query = urllib.urlencode({'msg': msg, 'acc': self.acc, 'pass': self.apikey, 'from': sender,
                                  'prio': prio, 'to': to})
        resp, content = http.request("https://web.smscom.se/sendsms.aspx?%s" % query)
        if resp.status == 200:
            if content not in self.status_codes:
                return True
            else:
                return self.status_codes[content]
        else:
            return resp


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'a:k:m:f:t:P')
    except getopt.error, msg:
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
        for opt, arg in opts:
            if opt in '-a':
                acc = arg
            elif opt in '-k':
                apikey = arg
            elif opt in '-m':
                msg = arg
            elif opt in '-P':
                prio = arg
            elif opt in '-t':
                to = arg
            elif opt in '-f':
                sender = arg
            else:
                raise ValueError("what about %s?" % opt)
    except Exception, ex:
        print ex
        print __doc__
        sys.exit(3)

    sms = SMSClient(acc=acc, apikey=apikey)
    sms.send(msg=msg, to=to, sender=sender, prio=prio)

if __name__ == "__main__":
    main()

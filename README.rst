
ip1.se SMS Gateway client
=========================


API:

  from smscom import SMSClient

  c = SMSClient(acc=$your_account_code,apikey=$your_api_key)
  c.send(msg=$message,sender=$from_string,to=$mobile,prio=$prio)

prio defaults to 2 (normal priority) and can be either 1 (low) or 3 (high)

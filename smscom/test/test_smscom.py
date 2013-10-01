from smscom import SMSClient
from unittest import TestCase
from httplib2 import Response
from mock import patch


class TestSmscom(TestCase):
    def setUp(self):
        self.sms = SMSClient('bogus', 'bogus')

    @patch('httplib2.Http.request')
    def test_send_sms_ok(self, mock_request):
        mock_request.return_value = request_return_value(200, "66666")
        status = self.sms.send("Test", "Test sender", "+461111111")
        self.assertEqual(status, True)

    @patch('httplib2.Http.request')
    def test_send_sms_wrong_credentials(self, mock_request):
        mock_request.return_value = request_return_value(200, "101")
        status = self.sms.send("Test", "Test sender", "+461111111")
        self.assertEqual(status, SMSClient.status_codes['101'])

    @patch('httplib2.Http.request')
    def test_send_sms_404(self, mock_request):
        mock_request.return_value = request_return_value(404, "101")
        status = self.sms.send("Test", "Test sender", "+461111111")
        self.assertEqual(status['status'], 404)


def request_return_value(response_code, content):
    data = {'status': response_code, 'content-length': '3', 'content-location': 'https://example.com/', 'x-powered-by': 'ASP.NET', 'set-cookie': 'ASP.NET_SessionId=wf1bkl0d5vykfpihwv0hlnhc; path=/; HttpOnly', 'x-aspnet-version': '4.0.30319', 'server': 'Microsoft-IIS/7.0', 'cache-control': 'private', 'date': 'Tue, 01 Oct 2013 06:29:28 GMT', 'content-type': 'text/html; charset=utf-8'}
    resp = Response(data)
    return (resp, content)

import africastalkingwrapper
import unittest
from test import USERNAME, API_KEY

africastalkingwrapper.initialize(USERNAME, API_KEY)
token_service = africastalkingwrapper.Authentication
service = africastalkingwrapper.SMS


class TestSmsService(unittest.TestCase):

    def test_send(self):
        res = service.send('test_send()', ['+254722212132', '+254738161159'])
        recipients = res['SMSMessageData']['Recipients']
        assert len(recipients) == 2
        assert recipients[0]['status'] == 'Success'
  
    # def test_send_premium(self):
    #     res = service.send_premium('test_send_premium()', 'AT2FA', ['+254722212132', '+254718769881'], 'JOHN',
    #                                'ERNST', retry_duration_in_hours=10)
    #     recipients = res['SMSMessageData']['Recipients']
    #     assert len(recipients) == 2
    #     assert recipients[0]['status'] == 'Success'

if __name__ == '__main__':
    unittest.main()

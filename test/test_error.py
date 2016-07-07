import chargehound
import requests_mock
import unittest2
import requests
from mock import patch
from chargehound.error import (
    ChargehoundBadRequestError, ChargehoundError,
    ChargehoundTimeoutError
)


class ErrorTest(unittest2.TestCase):

    def setUp(self):
        super(ErrorTest, self).setUp()
        chargehound.api_key = 'API_KEY'

    @requests_mock.mock()
    def test_bad_request(self, mock):
        mock.post('https://api.chargehound.com/v1/disputes/dp_123/submit',
                  status_code=400,
                  json={
                    'error': {'status': 400, 'message': 'Bad request.'}
                  })

        try:
            chargehound.Disputes.submit('dp_123')
        except ChargehoundBadRequestError as bad:
            assert bad.status == 400
            assert bad.message == 'Bad request.'

    @patch('requests.get', side_effect=requests.exceptions.ReadTimeout())
    def test_timeout(self, mock):
        try:
            chargehound.Disputes.list()
        except ChargehoundTimeoutError as time:
            assert time.message == 'Connection timed out'

    def test_propagate_errors(self):
        orig_host = chargehound.host
        chargehound.host = 'test'

        try:
            chargehound.Disputes.retrieve('dp_123')
        except Exception as e:
            assert not isinstance(e, ChargehoundError)
            chargehound.host = orig_host

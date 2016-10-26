from __future__ import unicode_literals

import chargehound
import requests
from chargehound.error import create_chargehound_error
from chargehound.version import VERSION


class APIRequestor(object):

    def parse_response(self, response):
        payload = response.json()
        if response.status_code < 400:
            payload['response'] = dict(
              status=response.status_code
            )
            return payload
        else:
            raise create_chargehound_error(payload)

    def get_url(self, path):
        return 'https://' + chargehound.host + chargehound.base_path + path

    def make_request(self, method, path, params=None, data=None,
                     callback=None):
        headers = {
            'accept': 'application/json',
            'user-agent': 'Chargehound/v1 PythonBindings/%s' % VERSION
        }

        auth = (chargehound.api_key, '')

        if method == 'get':
            return self.parse_response(requests.get(self.get_url(path),
                                       auth=auth,
                                       params=params,
                                       headers=headers,
                                       timeout=chargehound.timeout))
        elif method == 'post':
            return self.parse_response(requests.post(self.get_url(path),
                                       auth=auth,
                                       json=data,
                                       headers=headers,
                                       timeout=chargehound.timeout))

    def request(self, method, path, params=None, data=None, callback=None):
        if callback is None:
            return self.make_request(method, path, params, data)
        else:
            return self.make_request(method, path, params, data, callback)

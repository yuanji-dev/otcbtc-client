# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class User(OTCBTCAPIBase):

    def fetch(self):
        uri = '/api/v2/users/me'
        params = {
            'access_key': self.access_key,
        }
        payload = self.build_payload('GET', uri, params=params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)
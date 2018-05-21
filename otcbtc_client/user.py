# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase


class User(OTCBTCAPIBase):

    URI = '/api/v2/users/me'

    def fetch(self):
        uri = self.URI
        params = {
            'access_key': self.access_key,
        }
        payload = self.build_payload('GET', uri, params=params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)
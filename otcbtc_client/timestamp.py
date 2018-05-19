# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Timestamp(OTCBTCAPIBase):

    def fetch(self):
        return self.get('/api/v2/timestamp')

    def __call__(self):
        return self.fetch()
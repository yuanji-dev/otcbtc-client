# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Timestamp(OTCBTCAPIBase):

    URI = '/api/v2/timestamp'

    def fetch(self):
        return self.get(self.URI)

    def __call__(self):
        return self.fetch()
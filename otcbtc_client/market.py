# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Market(OTCBTCAPIBase):

    URI = '/api/v2/markets'

    def all(self):
        return self.get(self.URI)
# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Market(OTCBTCAPIBase):

    def all(self):
        return self.get('/api/v2/markets')
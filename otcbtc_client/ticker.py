# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Ticker(OTCBTCAPIBase):

    def all(self):
        return self.get('/api/v2/tickers')

    def fetch(self, market_id):
        return self.get('/api/v2/tickers/{market_id}'.format(market_id=market_id))
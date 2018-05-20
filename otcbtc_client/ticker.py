# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase


class Ticker(OTCBTCAPIBase):

    URI = '/api/v2/tickers'

    def all(self):
        return self.get(self.URI)

    def fetch(self, market_id):
        return self.get('{uri}/{market_id}'.format(
            uri=self.URI, market_id=market_id))

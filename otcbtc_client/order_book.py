# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class OrderBook(OTCBTCAPIBase):

    def fetch(self, market, asks_limit=20, bids_limit=20):
        return self.get('/api/v2/order_book', params={'market': market, 'asks_limit': asks_limit, 'bids_limit': bids_limit})
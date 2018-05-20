# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase


class OrderBook(OTCBTCAPIBase):

    URI = '/api/v2/order_book'

    def fetch(self, market, asks_limit=20, bids_limit=20):
        return self.get(
            self.URI,
            params={
                'market': market,
                'asks_limit': asks_limit,
                'bids_limit': bids_limit
            })

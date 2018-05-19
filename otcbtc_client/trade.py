# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Trade(OTCBTCAPIBase):

    def fetch(self, market, limit=50, timestamp=None, from_=None, to=None, order_by='desc'):
        params = {k: v for k, v in {
            'market': market,
            'limit': limit,
            'timestamp': timestamp,
            'from': from_,
            'to': to,
            'order_by': order_by
        }.items() if v}
        return self.get('/api/v2/trades', params=params)
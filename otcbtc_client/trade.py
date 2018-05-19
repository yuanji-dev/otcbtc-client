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

    def my_trades(self, market, limit=50, timestamp=None, from_=None, to=None, order_by='desc'):
        uri = '/api/v2/trades/my'
        params = {k: v for k, v in {
            'access_key': self.access_key,
            'market': market,
            'limit': limit,
            'timestamp': timestamp,
            'from': from_,
            'to': to,
            'order_by': order_by
        }.items() if v}
        payload = self.build_payload('GET', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)
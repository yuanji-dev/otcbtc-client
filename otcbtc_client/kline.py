# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Kline(OTCBTCAPIBase):

    def fetch(self, market, limit=30, period=1, timestamp=None):
        params =  {
            'market': market,
            'limit': limit,
            'period': period
        }
        if timestamp:
            params.update(timestamp=timestamp)
        return self.get('/api/v2/klines', params=params)

    def with_pending_trades(self, market, trade_id, limit=30, period=1, timestamp=None):
        params =  {
            'market': market,
            'trade_id': trade_id,
            'limit': limit,
            'period': period
        }
        if timestamp:
            params.update(timestamp=timestamp)
        return self.get('/api/v2/klines_with_pending_trades', params=params)
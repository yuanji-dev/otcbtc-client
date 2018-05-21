# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase


class Kline(OTCBTCAPIBase):

    KLINES_URI = '/api/v2/klines'
    KLINES_WITH_PENDING_TRADES_URI = '/api/v2/klines_with_pending_trades'

    def fetch(self, market, limit=30, period=1, timestamp=None):
        params = {'market': market, 'limit': limit, 'period': period}
        if timestamp:
            params.update(timestamp=timestamp)
        return self.get(self.KLINES_URI, params=params)

    def with_pending_trades(self,
                            market,
                            trade_id,
                            limit=None,
                            period=None,
                            timestamp=None):
        params = {
            k: v
            for k, v in {
                'market': market,
                'trade_id': trade_id,
                'limit': limit,
                'period': period
            }.items() if v
        }
        if timestamp:
            params.update(timestamp=timestamp)
        return self.get(self.KLINES_WITH_PENDING_TRADES_URI, params=params)
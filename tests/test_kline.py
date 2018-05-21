# coding: utf-8

import responses

from otcbtc_client.client import OTCBTCClient
from tests.helper import concat_url_and_params


class TestKline(object):
    @property
    def kline(self):
        return OTCBTCClient().kline

    @responses.activate
    def test_fetch(self):
        kline = self.kline
        market = 'otbeth'
        params = {
            'market': market,
            'limit': 2,
            'period': 1,
        }
        responses.add(
            responses.GET,
            concat_url_and_params(kline.build_url(kline.KLINES_URI), params),
            json=[
                [
                    1517833860,  # An integer represents the seconds elapsed since Unix epoch.
                    0.001159,  # K line open price
                    0.001162,  # K line highest price
                    0.001157,  # K line lowest price
                    0.001158,  # K line close price
                    1000  # K line volume
                ],
                [1517833920, 0.001142, 0.001160, 0.001142, 0.001159, 500]
            ],
            match_querystring=True)
        resp = kline.fetch(market=market, limit=2, period=1)
        assert len(resp) == 2

    @responses.activate
    def test_with_pending_trades(self):
        kline = self.kline
        market = 'otbeth'
        params = {
            'market': market,
            'trade_id': 1,
            'period': 1,
        }
        responses.add(
            responses.GET,
            concat_url_and_params(
                kline.build_url(kline.KLINES_WITH_PENDING_TRADES_URI), params),
            json={
                'k': [[
                    1517833860,
                    0.001159,  # K line open price
                    0.001162,  # K line highest price
                    0.001157,  # K line lowest price
                    0.001158,  # K line close price
                    1000  # K line volume
                ]],
                'trades': [{
                    'id': 25073,  # Unique trade id
                    'price': '0.00116',  # Trade's price
                    'volume': '473.3586',  # Trade's volume
                    'funds':
                    '0.549095976',  # Trade's funds, calculated by price * volume
                    'market':
                    'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                    'created_at':
                    '2018-02-05T20:45:22+08:00',  # Order create time in iso8601 format.
                    'at':
                    1517834722,  # An integer represents the seconds elapsed since Unix epoch till the trade create time.
                    'side':
                    'up'  # Trade's side, 'up' means the price is higher than the previous one, 'down' is lower than the previous one
                }]
            },
            match_querystring=True)
        resp = kline.with_pending_trades(market=market, trade_id=1, period=1)
        assert len(resp) == 2
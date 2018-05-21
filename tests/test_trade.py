# coding: utf-8

import pytest
import responses
from requests.exceptions import ConnectionError

from otcbtc_client.client import OTCBTCClient
from tests.helper import concat_url_and_params


class TestTrade(object):
    @property
    def trade(self):
        return OTCBTCClient().trade

    @property
    def trade_with_auth(self):
        return OTCBTCClient(api_key='xxx', api_secret='yyy').trade

    @responses.activate
    def test_fetch(self):
        trade = self.trade
        market = 'otbeth'
        params = {'market': market, 'limit': '1', 'order_by': 'desc'}
        responses.add(
            responses.GET,
            concat_url_and_params(trade.build_url(trade.TRADES_URI), params),
            json=[{
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
                1517834722,  # An integer represents the seconds elapsed since Unix epoch.
                'side':
                'up'  # Trade's side, 'up' means the price is higher than the previous one, 'down' is lower than the previous one
            }],
            match_querystring=True)
        resp = trade.fetch(market=market, limit=1, order_by='desc')
        assert len(resp) == 1
        assert resp[0]['market'] == market

    @responses.activate
    def test_my_trades(self):
        trade = self.trade
        market = 'otbeth'
        params = {
            'access_key':
            'xxx',
            'market':
            market,
            'signature':
            '9dbe0ecdcd3db5030486764dd8b8a4f15a6ee3eae47856f864d11f34c9eba478'
        }
        responses.add(
            responses.GET,
            concat_url_and_params(
                trade.build_url(trade.MY_TRADES_URI), params),
            json=[
                {
                    'id': 2,  # Unique trade id. 
                    'price':
                    '0.0015',  # Price for each unit. e.g. If you sell/buy 2 OTB at 0.0015 ETH, the price is '0.0015'.
                    'volume':
                    '2.0',  # The amount of base unit. e.g. If you sell/buy 2 OTB at 0.0015 ETH, the volume is '2.0'.
                    'funds':
                    '0.003',  # The amouut of quote unit. e.g. If you sell/buy 2 OTB at 0.0015 ETH, the funds is '0.003' ETH.
                    'market':
                    'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                    'created_at':
                    '2017-01-31T00:00:00+08:00',  # Trade create time in iso8601 format.
                    'at':
                    1485792000,  # An integer represents the seconds elapsed since Unix epoch.
                    'side': 'bid',  # Either 'bid' or 'ask'.
                    'order_id': 3  # Unique order id. 
                },
                {
                    'id': 1,
                    'price': '0.0018',
                    'volume': '1.0',
                    'funds': '0.0018',
                    'market': 'otbeth',
                    'created_at': '2017-01-30T00:00:00+08:00',
                    'at': 1485705600,
                    'side': 'ask',
                    'order_id': 1
                }
            ],
            match_querystring=True)
        with pytest.raises(ConnectionError):
            trade.my_trades(market=market)
        self.trade_with_auth.my_trades(market=market)

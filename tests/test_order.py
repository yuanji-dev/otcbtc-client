# coding: utf-8

import responses

from otcbtc_client.client import OTCBTCClient
from tests.helper import concat_url_and_params, body_str_to_dict


class TestOrder(object):
    @property
    def order(self):
        return OTCBTCClient(api_key='xxx', api_secret='yyy').order

    @responses.activate
    def test_list_order(self):
        order = self.order
        market = 'otbeth'
        params = {
            'market':
            market,
            'id':
            1,
            'access_key':
            'xxx',
            'signature':
            'c242b60f1830337f7618afab08d378b7cb2e9501fe226e76e0cab0ee93ac1933'
        }
        responses.add(
            responses.GET,
            concat_url_and_params(order.build_url(order.ORDER_URI), params),
            json={
                'id': 1,  # Unique order id.
                'side': 'buy',  # Either 'sell' or 'buy'.
                'ord_type': 'limit',  # Type of order, now only 'limit'.
                'price':
                '0.002',  # Price for each unit. e.g. If you sell/buy 1 OTB at 0.002 ETH, the price is '0.002'
                'avg_price':
                '0.0',  # Average execution price, average of price in trades.
                'state':
                'wait',  # One of 'wait', 'done', or 'cancel'. An order in 'wait' is an active order, waiting fullfillment; a 'done' order is an order fullfilled; 'cancel' means the order has been cancelled.
                'market':
                'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                'created_at':
                '2017-02-01T00:00:00+08:00',  # Order create time in iso8601 format.
                'volume':
                '100.0',  # The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 100 otb can be matched with a buy 60 otb order, left 40 otb to be sold; in this case the order's volume would be '100.0', its remaining_volume would be '40.0', its executed volume is '60.0'.
                'remaining_volume': '100.0',  # The remaining volume
                'executed_volume': '0.0',  # The executed volume
                'trades_count': 1  # Number of trades under this order
            })
        resp = order.list_order(id=1)
        print(resp)
        assert resp['id'] == 1

    @responses.activate
    def test_list_orders(self):
        order = self.order
        market = 'otbeth'
        params = {
            'market':
            market,
            'access_key':
            'xxx',
            'signature':
            'be0694b7c33e92da3ec6ee534f7391fb7d0332fc1d867681c5085c5194ed69c8'
        }
        responses.add(
            responses.GET,
            concat_url_and_params(order.build_url(order.ORDERS_URI), params),
            json=[
                {
                    'id': 1,  # Unique order id.
                    'side': 'buy',  # Either 'sell' or 'buy'.
                    'ord_type': 'limit',  # Type of order, now only 'limit'.
                    'price':
                    '0.002',  # Price for each unit. e.g. If you sell/buy 1 OTB at 0.002 ETH, the price is '0.002'
                    'avg_price':
                    '0.0',  # Average execution price, average of price in trades.
                    'state':
                    'wait',  # One of 'wait', 'done', or 'cancel'. An order in 'wait' is an active order, waiting fullfillment; a 'done' order is an order fullfilled; 'cancel' means the order has been cancelled.
                    'market':
                    'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                    'created_at':
                    '2017-02-01T00:00:00+08:00',  # Order create time in iso8601 format.
                    'volume':
                    '100.0',  # The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 100 otb can be matched with a buy 60 otb order, left 40 otb to be sold; in this case the order's volume would be '100.0', its remaining_volume would be '40.0', its executed volume is '60.0'.
                    'remaining_volume': '100.0',  # The remaining volume
                    'executed_volume': '0.0',  # The executed volume
                    'trades_count': 1  # Counts of trades under this order
                },
                {
                    'id': 3,
                    'side': 'sell',
                    'ord_type': 'limit',
                    'price': '0.003',
                    'avg_price': '0.0',
                    'state': 'wait',
                    'market': 'otbeth',
                    'created_at': '2017-02-01T00:00:00+08:00',
                    'volume': '100.0',
                    'remaining_volume': '100.0',
                    'executed_volume': '0.0',
                    'trades_count': 0
                }
            ],
            match_querystring=True)
        resp = order.list_orders(market=market)
        assert isinstance(resp, list)

    @responses.activate
    def test_create_order(self):
        order = self.order
        market = 'otbeth'
        data = {
            'market':
            market,
            'price':
            '0.002',
            'side':
            'sell',
            'volume':
            '100',
            'access_key':
            'xxx',
            'signature':
            'efcc83119fe25b18f0a02302aaee7765b62d7bf64dc6c5d4f2266f5a5fda4327'
        }
        responses.add(
            responses.POST,
            order.build_url(order.ORDERS_URI),
            json={
                'id': 1,  # Unique order id. 
                'side': 'sell',  # Either 'sell' or 'buy'.
                'ord_type': 'limit',  # Type of order, now only 'limit'.
                'price':
                '0.002',  # Price for each unit. e.g. If you sell/buy 100 OTB at 0.002 ETH, the price is '0.002'.
                'avg_price':
                '0.0',  # Average execution price, average of price in trades.
                'state':
                'wait',  # One of 'wait', 'done', or 'cancel'. An order in 'wait' is an active order, waiting fullfillment; a 'done' order is an order fullfilled; 'cancel' means the order has been cancelled.
                'market':
                'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                'created_at':
                '2017-02-01T00:00:00+08:00',  # Trade create time in iso8601 format.
                'volume':
                '100.0',  # The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 100 otb can be matched with a buy 60 otb order, left 40 otb to be sold; in this case the order's volume would be '100.0', its remaining_volume would be '40.0', its executed volume is '60.0'.
                'remaining_volume': '100.0',  # The remaining volume
                'executed_volume': '0.0',  # The executed volume
                'trades_count': 0  # Number of trades under this order
            },
            match_querystring=True)
        order.create_order(
            market=market, side='sell', price='0.002', volume='100')
        # XXX(Gimo): due to responses library don't have a parameter like match_request_body.
        assert body_str_to_dict(responses.calls[0].request.body) == data

    @responses.activate
    def test_cancel_order(self):
        order = self.order
        data = {
            'id':
            '1',
            'access_key':
            'xxx',
            'signature':
            '47ba4a04e8f5471a05078f8dd13976b7caa80665c5f8152d654486de327c395c'
        }
        responses.add(
            responses.POST,
            order.build_url(order.DELETE_ORDER_URI),
            json={
                'id': 1,  # Unique order id. 
                'side': 'buy',  # Either 'sell' or 'buy'.
                'ord_type': 'limit',  # Type of order, now only 'limit'.
                'price':
                '0.002',  # Price for each unit. e.g. If you sell/buy 100 OTB at 0.002 ETH, the price is '0.002'.
                'avg_price':
                '0.0',  # Average execution price, average of price in trades.
                'state':
                'wait',  # One of 'wait', 'done', or 'cancel'. An order in 'wait' is an active order, waiting fullfillment; a 'done' order is an order fullfilled; 'cancel' means the order has been cancelled.
                'market':
                'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                'created_at':
                '2017-02-01T00:00:00+08:00',  # Trade create time in iso8601 format.
                'volume':
                '100.0',  # The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 100 otb can be matched with a buy 60 otb order, left 40 otb to be sold; in this case the order's volume would be '100.0', its remaining_volume would be '40.0', its executed volume is '60.0'.
                'remaining_volume': '100.0',  # The remaining volume
                'executed_volume': '0.0',  # The executed volume
                'trades_count': 0  # Number of trades under this order
            },
            match_querystring=True)
        order.cancel_order(id='1')
        # XXX(Gimo): due to responses library don't have a parameter like match_request_body.
        assert body_str_to_dict(responses.calls[0].request.body) == data

    @responses.activate
    def test_cancel_orders(self):
        order = self.order
        data = {
            'access_key':
            'xxx',
            'signature':
            'f2ab1d061ad07a2de9fe7658b7203ce28ed6b6511287502b2a7a869172039bcf'
        }
        responses.add(
            responses.POST,
            order.build_url(order.CLEAR_ORDERS_URI),
            json=[
                {
                    'id': 2,  # Unique order id. 
                    'side': 'buy',  # Either 'sell' or 'buy'.
                    'ord_type': 'limit',  # Type of order, now only 'limit'.
                    'price':
                    '0.0015',  # Price for each unit. e.g. If you sell/buy 100 OTB at 0.0015 ETH, the price is '0.0015'.         
                    'avg_price':
                    '0.0',  # Average execution price, average of price in trades.
                    'state':
                    'wait',  # One of 'wait', 'done', or 'cancel'. An order in 'wait' is an active order, waiting fullfillment; a 'done' order is an order fullfilled; 'cancel' means the order has been cancelled.
                    'market':
                    'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                    'created_at':
                    '2017-02-01T00:00:00+08:00',  # Trade create time in iso8601 format.
                    'volume':
                    '100.0',  # The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 100 otb can be matched with a buy 60 otb order, left 40 otb to be sold; in this case the order's volume would be '100.0', its remaining_volume would be '40.0', its executed volume is '60.0'.
                    'remaining_volume': '60.0',  # The remaining volume
                    'executed_volume': '40.0',  # The executed volume
                    'trades_count': 1  # Number of trades under this order
                },
                {
                    'id': 1,
                    'side': 'sell',
                    'ord_type': 'limit',
                    'price': '0.0012',
                    'avg_price': '0.0',
                    'state': 'wait',
                    'market': 'otbeth',
                    'created_at': '2017-02-01T00:00:00+08:00',
                    'volume': '100.0',
                    'remaining_volume': '100.0',
                    'executed_volume': '0.0',
                    'trades_count': 0
                }
            ],
            match_querystring=True)
        order.cancel_orders()
        # XXX(Gimo): due to responses library don't have a parameter like match_request_body.
        assert body_str_to_dict(responses.calls[0].request.body) == data
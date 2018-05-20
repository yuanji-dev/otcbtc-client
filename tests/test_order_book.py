# coding: utf-8

import responses

from otcbtc_client.order_book import OrderBook


class TestOrderBook(object):
    @property
    def order_book(self):
        return OrderBook()

    @responses.activate
    def test_fetch(self):
        order_book = self.order_book
        responses.add(
            responses.GET,
            order_book.build_url(order_book.URI),
            json={
                'asks': [{
                    'id': 71468,  # Unique order id
                    'side': 'sell',  # Either 'sell' or 'buy'.
                    'ord_type': 'limit',  # Type of order, now only 'limit'.
                    'price':
                    '0.00116',  # Price for each unit. e.g. If you sell/buy 1 OTB at 0.00116 ETH, the price is '0.00116'
                    'avg_price':
                    '0.00116',  # Average execution price, average of price in trades.
                    'state':
                    'wait',  # One of 'wait', 'done', or 'cancel'. An order in 'wait' is an active order, waiting fullfillment; a 'done' order is an order fullfilled; 'cancel' means the order has been cancelled.
                    'market':
                    'otbeth',  # The market in which the order is placed, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
                    'created_at':
                    '2018-02-04T20:13:01+08:00',  # Order create time in iso8601 format.
                    'volume':
                    '5000.0',  # The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 5000 otb can be matched with a buy 2146.6 otb order, left 2000 otb to be sold; in this case the order's volume would be '5000.0', its remaining_volume would be '2853.4', its executed volume is '2146.6'.
                    'remaining_volume': '2853.4',  # The remaining volume
                    'executed_volume': '2146.6',  # The executed volume
                    'trades_count': 3  # Counts of trades under this order
                }],
                'bids': [{
                    'id': 74866,
                    'side': 'buy',
                    'ord_type': 'limit',
                    'price': '0.00113212',
                    'avg_price': '0.00113212',
                    'state': 'wait',
                    'market': 'otbeth',
                    'created_at': '2018-02-05T20:32:35+08:00',
                    'volume': '849.15791612',
                    'remaining_volume': '845.15791612',
                    'executed_volume': '4.0',
                    'trades_count': 1
                }]
            })
        resp = order_book.fetch(market='otbeth', asks_limit=1, bids_limit=1)
        assert 'asks' in resp
        assert 'bids' in resp
        assert len(resp['asks']) == 1
        assert len(resp['bids']) == 1

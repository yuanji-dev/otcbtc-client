# coding: utf-8

from otcbtc_client.kline import Kline
from otcbtc_client.market import Market
from otcbtc_client.order_book import OrderBook
from otcbtc_client.ticker import Ticker
from otcbtc_client.timestamp import Timestamp
from otcbtc_client.trade import Trade
from otcbtc_client.user import User
from otcbtc_client.order import Order


class OTCBTCClient(object):
    def __init__(self, api_key='', api_secret=''):
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def market(self):
        return Market()

    @property
    def ticker(self):
        return Ticker()

    @property
    def order_book(self):
        return OrderBook()

    @property
    def trade(self):
        return Trade(self.api_key, self.api_secret)

    @property
    def timestamp(self):
        return Timestamp()

    @property
    def kline(self):
        return Kline()

    @property
    def user(self):
        return User(self.api_key, self.api_secret)

    @property
    def order(self):
        return Order(self.api_key, self.api_secret)
# coding: utf-8

from otcbtc_client.market import Market
from otcbtc_client.ticker import Ticker


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

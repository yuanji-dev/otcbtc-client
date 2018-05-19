# coding: utf-8

from otcbtc_client.market import Market

class OTCBTCClient(object):

    def __init__(self, api_key='', api_secret=''):
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def market(self):
        return Market()
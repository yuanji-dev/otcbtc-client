# coding: utf-8

import requests

class OTCBTCAPIBase(object):

    API_ENDPOINT = 'https://bb.otcbtc.com'

    def __init__(self, api_key='', api_secret=''):
        self.access_token = api_key
        self.api_secret = api_secret

    def build_url(self, uri):
        return self.API_ENDPOINT + uri

    def get(self, uri, params=None, **kwargs):
        r = requests.get(self.build_url(uri), params=params, **kwargs)
        return r.json()
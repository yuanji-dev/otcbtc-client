# coding: utf-8

import responses

from otcbtc_client.client import OTCBTCClient
from tests.helper import concat_url_and_params


class TestUser(object):
    @property
    def user(self):
        return OTCBTCClient(api_key='xxx', api_secret='yyy').user

    @responses.activate
    def test_fetch(self):
        user = self.user
        params = {
            'access_key':
            'xxx',
            'signature':
            'a71c1c5ee28fbd2196ee0bca9e334a18e6053526bd979020ef3839245136c763'
        }
        responses.add(
            responses.GET,
            concat_url_and_params(user.build_url(user.URI), params),
            json={
                'user_name':
                'u1513250056',  # your user name
                'email':
                'u1513250056@gmail.com',  # your email
                'accounts': [  # your account information
                    {
                        'currency': 'btc',  # your BTC account
                        'balance': '0.01',  # your current BTC balance amount
                        'locked': '0.001',  # your current BTC locked amount
                        'saving': '0.0'  # your current BTC saving amount
                    },
                    {
                        'currency': 'otb',
                        'balance': '1000.0',
                        'locked': '200.0',
                        'saving': '0.0'
                    },
                ]
            },
            match_querystring=True)
        resp = user.fetch()
        assert 'user_name' in resp
        assert 'email' in resp
        assert 'accounts' in resp

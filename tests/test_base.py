# coding: utf-8

from otcbtc_client.base import OTCBTCAPIBase

class TestBase(object):

    @property
    def base(self):
        return OTCBTCAPIBase(api_key='xxx', api_secret='yyy')

    def test_build_payload(self):
        base = self.base
        assert base.build_payload('GET', '/api/v2/users/me', dict(access_key='xxx')) == 'GET|/api/v2/users/me|access_key=xxx'
        assert base.build_payload('GET', '/api/v2/orders', dict(market='otbeth', access_key='xxx')) == 'GET|/api/v2/orders|access_key=xxx&market=otbeth'
        assert base.build_payload('GET', '/api/v2/order', dict(id='1', access_key='xxx')) == 'GET|/api/v2/order|access_key=xxx&id=1'
        assert base.build_payload('POST', '/api/v2/orders', dict(market='otbeth', access_key='xxx', price='0.002', side='sell', volume='100')) == 'POST|/api/v2/orders|access_key=xxx&market=otbeth&price=0.002&side=sell&volume=100'
        assert base.build_payload('POST', '/api/v2/order/delete', dict(id='1', access_key='xxx')) == 'POST|/api/v2/order/delete|access_key=xxx&id=1'
        assert base.build_payload('POST', '/api/v2/orders/clear', dict(access_key='xxx')) == 'POST|/api/v2/orders/clear|access_key=xxx'
        assert base.build_payload('GET', '/api/v2/trades/my', dict(market='otbeth', access_key='xxx')) == 'GET|/api/v2/trades/my|access_key=xxx&market=otbeth'

    def test_signature(self):
        base = self.base
        assert base.generate_signature('GET|/api/v2/users/me|access_key=xxx') == 'a71c1c5ee28fbd2196ee0bca9e334a18e6053526bd979020ef3839245136c763'
        assert base.generate_signature('GET|/api/v2/orders|access_key=xxx&market=otbeth') == 'be0694b7c33e92da3ec6ee534f7391fb7d0332fc1d867681c5085c5194ed69c8'
        assert base.generate_signature('GET|/api/v2/order|access_key=xxx&id=1') == 'c242b60f1830337f7618afab08d378b7cb2e9501fe226e76e0cab0ee93ac1933'
        assert base.generate_signature('POST|/api/v2/orders|access_key=xxx&market=otbeth&price=0.002&side=sell&volume=100') == 'efcc83119fe25b18f0a02302aaee7765b62d7bf64dc6c5d4f2266f5a5fda4327'
        assert base.generate_signature('POST|/api/v2/order/delete|access_key=xxx&id=1') == '47ba4a04e8f5471a05078f8dd13976b7caa80665c5f8152d654486de327c395c'
        assert base.generate_signature('POST|/api/v2/orders/clear|access_key=xxx') == 'f2ab1d061ad07a2de9fe7658b7203ce28ed6b6511287502b2a7a869172039bcf'
        assert base.generate_signature('GET|/api/v2/trades/my|access_key=xxx&market=otbeth') == '9dbe0ecdcd3db5030486764dd8b8a4f15a6ee3eae47856f864d11f34c9eba478'
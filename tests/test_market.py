# coding: utf-8

import responses

from otcbtc_client.client import OTCBTCClient


class TestMarket(object):
    @property
    def market(self):
        return OTCBTCClient().market

    @responses.activate
    def test_all(self):
        market = self.market
        responses.add(
            responses.GET,
            market.build_url(market.URI),
            json=[
                {
                    'id': 'otbeth',  # Unique marked id.
                    'ticker_id': 'btc_eth',  # Unique ticker id.
                    'name': 'BTC/ETH'  # market name
                },
                {
                    'id': 'otbeth',
                    'ticker_id': 'otb_eth',
                    'name': 'OTB/ETH'
                },
                {
                    'id': 'eoseth',
                    'ticker_id': 'eos_eth',
                    'name': 'EOS/ETH'
                },
                {
                    'id': 'bcheth',
                    'ticker_id': 'bch_eth',
                    'name': 'BCH/ETH'
                },
            ],
            match_querystring=True)
        resp = market.all()
        assert resp[0]
        assert resp[0]['id'] == 'otbeth'
        assert resp[0]['ticker_id'] == 'btc_eth'
        assert resp[0]['name'] == 'BTC/ETH'

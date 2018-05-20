# coding: utf-8

import responses

from otcbtc_client.ticker import Ticker


class TestTicker(object):
    @property
    def ticker(self):
        return Ticker()

    def test_all(self):
        ticker = self.ticker
        responses.add(
            responses.GET,
            ticker.build_url(ticker.URI),
            json={
                'btc_eth': {
                    'at':
                    1517833531,  # An integer represents the seconds elapsed since Unix epoch.
                    'ticker': {
                        'buy': '9.0000008',  # Latest bid price
                        'sell': '9.78949997',  # Latest ask price
                        'low':
                        '8.65100033',  # Lowest price within last 24 hours
                        'high':
                        '9.79999439',  # Highest Price within last 24 hours
                        'last': '9.0000008',  # Last trade's price
                        'vol':
                        '13.37148291'  # Trade volume within last 24 hours
                    }
                },
                'otb_eth': {
                    'at': 1517833531,
                    'ticker': {
                        'buy': '0.0011599',
                        'sell': '0.00116',
                        'low': '0.00109301',
                        'high': '0.00116',
                        'last': '0.00116',
                        'vol': '71236.11349855'
                    }
                },
            })
        resp = ticker.all()
        assert 'btc_eth' in resp
        assert 'otb_eth' in resp

    @responses.activate
    def test_fetch(self):
        ticker = self.ticker
        market_id = 'otbeth'
        responses.add(
            responses.GET,
            '{}/{}'.format(ticker.build_url(ticker.URI), market_id),
            json={
                'at':
                1517833531,  # An integer represents the seconds elapsed since Unix epoch.
                'ticker': {
                    'buy': '0.0011599',  # Latest bid price
                    'sell': '0.00116',  # Latest ask price
                    'low': '0.00109301',  # Lowest price within last 24 hours
                    'high': '0.00116',  # Highest Price within last 24 hours
                    'last': '0.00116',  # Last trade's price
                    'vol':
                    '71236.11349855'  # Trade volume within last 24 hours
                }
            })
        resp = ticker.fetch(market_id)
        assert 'ticker' in resp
        assert 'at' in resp
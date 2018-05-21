# coding: utf-8

import responses

from otcbtc_client.client import OTCBTCClient


class TestTimestamp(object):
    @property
    def timestamp(self):
        return OTCBTCClient().timestamp

    @responses.activate
    def test_timestamp(self):
        timestamp = self.timestamp
        responses.add(
            responses.GET,
            timestamp.build_url(timestamp.URI),
            json=1517740381,
            match_querystring=True)
        resp = timestamp()
        assert resp == 1517740381

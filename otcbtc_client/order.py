# coding:  utf-8

from otcbtc_client.base import OTCBTCAPIBase

class Order(OTCBTCAPIBase):

    def list_order(self, id):
        uri = '/api/v2/order'
        params = {
            'access_key': self.access_key,
            'id': id
        }
        payload = self.build_payload('GET', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)

    def list_orders(self, market=None, state='wait', limit=100, page=1, order_by='asc'):
        # state: Filter order by state, default to ‘wait’ (active orders). Other options:‘cancel’, ‘done’
        uri = '/api/v2/orders'
        params = {
            'access_key': self.access_key,
            'state': state,
            'limit': limit,
            'page': page,
            'order_by': order_by
        }
        if market:
            params.update(market=market)
        payload = self.build_payload('GET', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)

    def create_order(self, market, side, volume, price, ord_type='limit'):
        uri = '/api/v2/orders'
        params = {
            'access_key': self.access_key,
            'market': market,
            'side': side,
            'volume': volume,
            'price': price,
            'ord_type': ord_type
        }
        payload = self.build_payload('POST', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.post(uri, params=params)

    def cancel_order(self, id):
        uri = '/api/v2/order/delete'
        params = {
            'access_key': self.access_key,
            'id': id
        }
        payload = self.build_payload('POST', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.post(uri, params=params)

    def cancel_orders(self):
        uri = '/api/v2/orders/clear'
        params = {
            'access_key': self.access_key,
        }
        payload = self.build_payload('POST', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.post(uri, params=params)
# coding:  utf-8

from otcbtc_client.base import OTCBTCAPIBase


class Order(OTCBTCAPIBase):

    ORDER_URI = '/api/v2/order'
    ORDERS_URI = '/api/v2/orders'
    DELETE_ORDER_URI = '/api/v2/order/delete'
    CLEAR_ORDERS_URI = '/api/v2/orders/clear'

    def list_order(self, id):
        uri = self.ORDER_URI
        params = {'access_key': self.access_key, 'id': id}
        payload = self.build_payload('GET', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)

    def list_orders(self,
                    market=None,
                    state=None,
                    limit=None,
                    page=None,
                    order_by=None):
        # state: Filter order by state, default to ‘wait’ (active orders). Other options:‘cancel’, ‘done’
        uri = self.ORDERS_URI
        params = {
            k: v
            for k, v in {
                'access_key': self.access_key,
                'state': state,
                'limit': limit,
                'page': page,
                'order_by': order_by
            }.items() if v
        }
        if market:
            params.update(market=market)
        payload = self.build_payload('GET', uri, params)
        params.update(signature=self.generate_signature(payload))
        return self.get(uri, params=params)

    def create_order(self, market, side, volume, price, ord_type=None):
        uri = self.ORDERS_URI
        data = {
            k: v
            for k, v in {
                'access_key': self.access_key,
                'market': market,
                'side': side,
                'volume': volume,
                'price': price,
                'ord_type': ord_type
            }.items() if v
        }
        payload = self.build_payload('POST', uri, data)
        data.update(signature=self.generate_signature(payload))
        return self.post(uri, data=data)

    def cancel_order(self, id):
        uri = self.DELETE_ORDER_URI
        data = {'access_key': self.access_key, 'id': id}
        payload = self.build_payload('POST', uri, data)
        data.update(signature=self.generate_signature(payload))
        return self.post(uri, data=data)

    def cancel_orders(self, side=None):
        uri = self.CLEAR_ORDERS_URI
        data = {
            k: v
            for k, v in {
                'access_key': self.access_key,
                'side': side
            }.items() if v
        }
        payload = self.build_payload('POST', uri, data)
        data.update(signature=self.generate_signature(payload))
        return self.post(uri, data=data)
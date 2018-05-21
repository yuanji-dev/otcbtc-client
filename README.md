# otcbtc-client

A client for OTCBTC, which supports the OTCBTC public API and Auth API based on the [official API documentation](https://github.com/otcbtc/otcbtc-exchange-api-doc), for more information, please read the documentation.

[![PyPI](https://img.shields.io/pypi/v/otcbtc-client.svg)](https://pypi.org/project/otcbtc-client/)
[![PyPI - License](https://img.shields.io/pypi/l/otcbtc-client.svg)](https://pypi.org/project/otcbtc-client/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otcbtc-client.svg)](https://pypi.org/project/otcbtc-client/)
[![Build Status](https://travis-ci.org/masakichi/otcbtc-client.svg?branch=master)](https://travis-ci.org/masakichi/otcbtc-client)
[![codecov](https://codecov.io/gh/masakichi/otcbtc-client/branch/master/graph/badge.svg)](https://codecov.io/gh/masakichi/otcbtc-client)

## Overview

Whether you're building a custom app or integrating other service into OTCBTC, OTCBTC SDK for Python allows you to leverage the flexibility of Python to get your project up and running as quickly as possible.

## Installation

PyPI are recommended to install OTCBTC SDK for Python, use pip or pipenv.

```python
pip install otcbtc-client
```

## Usage

You need to instantiate an client from OTCBTCClient class first, with your own API_KEY and API_SECRET. 

```python
from otcbtc_client.client import OTCBTCClient

auth_client = OTCBTCClient(API_KEY, API_SECRET) # Need to access auth APIs
```

*For public APIs, API_KEY and API_SECRET are not necessary.*

```python
client = OTCBTCClient() # Use public APIs only.
```

### Market

#### Get all available markets(Public API)

```python
In [1]: client.market.all()
Out[1]:
[{'id': 'btceth', 'name': 'BTC/ETH', 'ticker_id': 'btc_eth'},
 {'id': 'eoseth', 'name': 'EOS/ETH', 'ticker_id': 'eos_eth'},
 {'id': 'bcheth', 'name': 'BCH/ETH', 'ticker_id': 'bch_eth'},
 {'id': 'gxseth', 'name': 'GXS/ETH', 'ticker_id': 'gxs_eth'},
 {'id': 'zeceth', 'name': 'ZEC/ETH', 'ticker_id': 'zec_eth'},...]
```

### Ticker

#### Get ticker of all markets(Public API)

```python
In [1]: client.ticker.all()
Out[1]:
{'ada_btc': {'at': 1526921081,
  'ticker': {'buy': '0.0000301',
   'high': '0.0000309',
   'last': '0.00003027',
   'low': '0.0000293',
   'open': 2.943e-05,
   'sell': '0.0000306',
   'vol': '60930.97947734'}},
 'ada_eth': {'at': 1526921081,
  'ticker': {'buy': '0.00034758',
   'high': '0.000372',
   'last': '0.00035391',
   'low': '0.00034335',
   'open': 0.0003498,
   'sell': '0.00036176',
   'vol': '70583.0778626'}},...}
```

#### Get ticker of specific market(Public API)

```python
In [1]: client.ticker.fetch('otbeth')
Out[1]:
{'at': 1526921191,
 'ticker': {'buy': '0.00062634',
  'high': '0.000655',
  'last': '0.00063229',
  'low': '0.00061501',
  'open': 0.0006402,
  'sell': '0.00064',
  'vol': '900260.78491758'}}
```

### Order Book

#### Get the order book of specified market(Public API)

```python
In [1]: client.order_book.fetch(market='otbeth', asks_limit=1, bids_limit=1)
Out[1]:
{'asks': [{'avg_price': '0.0',
   'created_at': '2018-05-22T00:43:18+08:00',
   'executed_volume': '0.0',
   'id': 37519992,
   'market': 'otbeth',
   'ord_type': 'limit',
   'price': '0.00064',
   'remaining_volume': '1107.93650478',
   'side': 'sell',
   'state': 'wait',
   'trades_count': 0,
   'volume': '1107.93650478'}],
 'bids': [{'avg_price': '0.0',
   'created_at': '2018-05-22T00:48:31+08:00',
   'executed_volume': '0.0',
   'id': 37521683,
   'market': 'otbeth',
   'ord_type': 'limit',
   'price': '0.00062636',
   'remaining_volume': '159.65259595',
   'side': 'buy',
   'state': 'wait',
   'trades_count': 0,
   'volume': '159.65259595'}]}
```

### Trade

#### Get recent trades on market(Public Api)

*Each trade is included only once. Trades are sorted in reverse creation order*

```python
In [1]: client.trade.fetch(market='otbeth', limit=1)
Out[1]:
[{'at': 1526921408,
  'created_at': '2018-05-22T00:50:08+08:00',
  'funds': '0.5631751916118198',
  'id': 1813244,
  'market': 'otbeth',
  'price': '0.00063297',
  'side': 'up',
  'volume': '889.73441334'}]
```

Other parameters:

- timestamp: An integer represents the seconds elapsed since Unix epoch. If set, only trades executed before the time will be returned.
- **from_**: Trade id. If set, only trades created after the trade will be returned.
- to: Trade id. If set, only trades created before the trade will be returned.
- order_by: If set, returned trades will be sorted in specific order, default to 'desc’.

### Timestammp

#### Get server current time, in seconds since Unix epoch(Public API)

```python
In [1]: client.timestamp.fetch() # or just call client.timestamp()
Out[1]: 1526921749
```

### Kline

#### Get OHLC(k line) of specific market(Public API)

```python
In [1]: client.kline.fetch(market='otbeth', limit=1)
Out[1]: [[1526921880, 0.00063846, 0.00063846, 0.00063846, 0.00063846, 823.5836]]
```

Other parameters:

- period: Time period of K line, default to 1. You can choose between 1, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080. Default value : 1
- timestamp: An integer represents the seconds elapsed since Unix epoch. If set, only k-line data after that time will be returned.

### Klines with pending trades

#### Get K data with pending trades(Public API)

Which are the trades not included in K data yet, because there’s delay between trade generated and processed by K data generator.

```python
In [1]: client.kline.with_pending_trades(market='otbeth', trade_id=1, limit=1)
Out[1]:
{'k': [[1526922180, 0.00063787, 0.00063787, 0.00063787, 0.00063787, 998.8065]],
 'trades': []}
```

### User

#### Get your profile and accounts info(Auth API)

```python
In [1]: auth_client.user.fetch()
Out[1]:
{'accounts': [{'balance': '0.0',
   'currency': 'eos',
   'locked': '0.0',
   'saving': '0.0'},
  {'balance': '0.0',
   'currency': 'btc',
   'locked': '0.0',
   'saving': '0.0'},...],
 'email': '***',
 'user_name': '***'}
```

### List Orders

#### Get your orders, results is paginated(Auth API)

```python
auth_client.order.list_orders(market=None, state=None, limit=None, page=None, order_by=None)
```

Paramters:

- market: Unique market id. It’s always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'otbeth'. All available markets can be found at /api/v2/markets. If left blank, the api will return your orders of all markets.
- state: Filter order by state, default to 'wait' (active orders). Other options:'cancel', 'done'
- limit: Limit the number of returned price levels. Default to 100.
- page: Specify the page of paginated results. Default value: 1
- order_by: If set, returned trades will be sorted in specific order, default to 'asc'.

### List Order

#### Get information of specified order(Auth API)

```python
auth_client.order.list_order(id) # Unique order id
```

### Create Order

#### Create a Sell/Buy order(Auth API)

```python
auth_client.order.create_order(market, side, volume, price, ord_type=None)
```

Parameters:

- market(required): Unique market id. It’s always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
- side(required): Either 'sell' or 'buy'.
- volume(required): The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 100 otb can be matched with a buy 60 otb order, left 40 otb to be sold; in this case the order’s volume would be '100.0', its remaining_volume would be '40.0', its executed volume is '60.0'.
- price: Price for each unit. e.g. If you want to sell/buy 1 otb at 0.002 ETH, the price is ‘0.002’.
- ord_type: Type of order, now only 'limit'.

### Cancel Order

#### Cancel an order(Auth API)

```python
auth_client.order.cancel_order(id)
```

### Cancel Orders

#### Cancel all your orders(Auth API)

```python
auth_client.order.cancel_orders(side=None) # If present, only sell orders (asks) or buy orders (bids) will be canncelled. Vaules: 'sell', 'buy'
```

### My Trades

#### Get your executed trades(Auth API) 

Trades are sorted in reverse creation order.

```python
auth_client.trade.my_trades(market, limit=None, timestamp=None, from_=None, to=None, order_by=None)
```

Parameters:

- market(required): Unique market id. It’s always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'otbeth'. All available markets can be found at /api/v2/markets.
- limit: Limit the number of returned trades. Default to 50. Range 1..1000
- timestamp: An integer represents the seconds elapsed since Unix epoch. If set, only trades executed before the time will be returned.
- from: Trade id. If set, only trades created after the trade will be returned.
- to: Trade id. If set, only trades created before the trade will be returned.
- order_by:If set, returned trades will be sorted in specific order, default to 'desc'. Values: 'asc', 'desc'

# python -m unittest -v test_stockdata_api3

import requests
import json

response = requests.get("https://api.iextrading.com/1.0/tops/last?symbols=AAPL,MSFT,AMZN")

txt = response.text
seclist = json.loads(txt)

print("The response includes the following headers:")
print(response.headers)

print(type(seclist))
print(seclist)
print(type(seclist[0]))
print(seclist[0])

for secrecord in seclist:

	print(secrecord['symbol'], secrecord['price'])

print(seclist[0]['price'])
print(type(seclist[0]['price']))

import unittest

class TestPrices(unittest.TestCase):
    def test_datatype(self):
        for secrecord in seclist:
            a = type(secrecord['price'])
            b = type(1.23)
            self.assertEqual(a, b)

    def test_price_positive(self):
        for secrecord in seclist:
            a = seclist[0]['price']
            b = 0
            self.assertGreater(a, b)

    def test_aymbol_count(self):
        seccount = len(seclist)
        self.assertEqual(seccount, 3)

# python -m unittest -v test_stockdata_api3
import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin

class TestConversion(TestCase):

    # patch the get_bitcoin_data function
    @patch('bitcoin.get_bitcoin_data')
    def test_get_bitcoin_data(self, mock_api):

        # mock API response
        mock_api.return_value = {"time":{"updated":"Oct 12, 2023 01:04:00 UTC","updatedISO":"2023-10-12T01:04:00+00:00","updateduk":"Oct 12, 2023 at 02:04 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"26,786.2329","description":"United States Dollar","rate_float":26786.2329},"GBP":{"code":"GBP","symbol":"&pound;","rate":"22,382.3619","description":"British Pound Sterling","rate_float":22382.3619},"EUR":{"code":"EUR","symbol":"&euro;","rate":"26,093.7016","description":"Euro","rate_float":26093.7016}}}

        # extract dollar value from mock data and convert it to dollars
        expected_float = float(mock_api.return_value['bpi']['USD']['rate_float']) * 100
        expected = round(expected_float, 2)
        dollars = bitcoin.convert_bitcoin_to_dollars(100)
        self.assertEqual(expected, dollars)

if __name__ == '__main__':
    unittest.main()

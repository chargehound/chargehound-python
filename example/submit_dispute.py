#!/usr/bin/python
# -*- coding: utf-8 -*-
# import Chargehound and set your API key

import os
import chargehound

chargehound.api_key = os.environ.get('CHARGEHOUND_API_KEY')

# List currently active disputes and then submit
# the most recent with the 'crowdfunding' template
# and update the `customer_ip` evidence field.

disputes = chargehound.Disputes.list()
first = disputes['data'][0]

products = [{'name': 'Saxophone',
             'description': 'Alto saxophone, with carrying case',
             'image': 'http://s3.amazonaws.com/chargehound/saxophone.png',
             'sku': '17283001272',
             'quantity': 1,
             'amount': 20000,
             'url': 'http://www.example.com', },
            {'name': 'Milk',
             'description': 'Semi-skimmed Organic',
             'image': 'http://s3.amazonaws.com/chargehound/milk.png',
             'sku': '26377382910',
             'quantity': '64oz',
             'amount': 400,
             'url': 'http://www.example.com'}]

submitted = chargehound.Disputes.submit(first['id'],
                                        template='crowdfunding',
                                        fields={'customer_ip': '0.0.0.0'},
                                        products=products)

print('Submitted with fields: {0}'.format(submitted['fields']))

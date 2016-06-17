# import Chargehound and set your API key
import os
import chargehound
chargehound.api_key = os.environ.get('CHARGEHOUND_API_KEY')

# List currently active disputes and then submit
# the most recent with the 'crowdfunding' template
# and update the `customer_ip` evidence field.
disputes = chargehound.Disputes.list()
first = disputes['data'][0]
submitted = chargehound.Disputes.submit(first['id'],
                                        template='crowdfunding',
                                        fields={
                                          'customer_ip': '0.0.0.0'
                                        },
                                        products=[{
                                            'name': 'Product Name 1',
                                            'description': 'Product Description (optional)',
                                            'image': 'Product Image URL (optional)',
                                            'sku': 'Stock Keeping Unit (optional)',
                                            'quantity': 1,
                                            'amount': 1000,
                                            'url': 'Product URL (optional)'
                                          }, {
                                            'name': 'Product Name 2',
                                            'description': 'Product Description (optional)',
                                            'image': 'Product Image URL (optional)',
                                            'sku': 'Stock Keeping Unit (optional)',
                                            'quantity': '10oz',
                                            'amount': 2000,
                                            'url': 'Product URL (optional)'
                                          }
                                        ])

print('Submitted with fields: {0}'.format(submitted['fields']))

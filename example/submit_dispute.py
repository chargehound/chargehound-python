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
                                          'customer_ip': '001'
                                        })

print 'Submitted with fields: {}'.format(submitted['fields'])

# your code goes here!

import re

def parse(self):
    addresses = re.split(r",|\s", self.email_addresses)

    parsed_addresses = []
    for address in addresses:
        address = address.strip()
        if address and not any(address in parsed for parsed in parsed_addresses):
            parsed_addresses.append(address)

    parsed_addresses.sort()
    return parsed_addresses


#email_addresses = "john@doe.com, person@somewhere.org"
#parser = EmailAddressParser(email_addresses)
#parser.parse()
# => ["john@doe.com", 'person@somewhere.org']
#EmailAddressParser("john@doe.com, person@somewhere.org").parse
# => ["john@doe.com", 'person@somewhere.org']
#EmailAddressParser("john@doe.com person@somewhere.org").parser# => ["john@doe.com", "person@somewhere.org"]
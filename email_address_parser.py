# your code goes here!

import re


class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the input string using a regular expression to handle both comma separation and space separation
        addresses = re.split(r",|\s", self.email_addresses)

        parsed_addresses = []
        for address in addresses:
            # Remove any leading or trailing whitespaces from each email address
            address = address.strip()
            if address and address not in parsed_addresses:
                parsed_addresses.append(address)

        # Sort the email addresses alphabetically
        parsed_addresses.sort()

        return parsed_addresses





#email_addresses = "john@doe.com, person@somewhere.org"
#parser = EmailAddressParser(email_addresses)
#parser.parse()
# => ["john@doe.com", 'person@somewhere.org']
#EmailAddressParser("john@doe.com, person@somewhere.org").parse
# => ["john@doe.com", 'person@somewhere.org']
#EmailAddressParser("john@doe.com person@somewhere.org").parser# => ["john@doe.com", "person@somewhere.org"]
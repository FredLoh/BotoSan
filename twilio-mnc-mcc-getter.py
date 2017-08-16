import logging
import os
from twilio.rest import Client


class TwilioClient(object):
    def __init__(self):
        self.logger = logging.getLogger("botosan.logger")
        self.account_sid = os.environ["TWILIO_SID"]
        self.account_token = os.environ["TWILIO_TOKEN"]
        self.client = Client(self.account_sid, self.account_token)

    def get_mcc_and_mnc(self, phone_number):
        """
        Gets the Mobile Country Code and Mobile Network code for a given Twilio Number
        :param phone_number: The phone number, containing the +CC Number, ex: +12345678901 for the US.
        :return: a tuple containing the mcc and mnc
        """
        number = self.client.lookups.phone_numbers(phone_number).fetch(type="carrier")
        self.logger.info(number.carrier['mobile_country_code'])
        self.logger.info(number.carrier['mobile_network_code'])
        return number.carrier['mobile_country_code'], number.carrier['mobile_network_code']

    def get_available_numbers(self):
        numbers = self.client.available_phone_numbers("GB").local.list(exclude_local_address_required=True)
        print(numbers.count())
        phone_numbers = []
        for number in numbers:
            phone_numbers.append(number.phone_number)
        return phone_numbers

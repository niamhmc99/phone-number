import re
class Phone(object):
    
    def __init__(self, phone_number):
        self.phone_number = self._clean(phone_number)
        self.area_code = self.phone_number[:3]
        self.exchange_code = self.phone_number[3:6]
        self.subscriber_number = self.phone_number[-4:]

    def pretty(self):
        return "({}) {}-{}".format(
            self.area_code,
            self.exchange_code,
            self.subscriber_number,
        )

    def _clean(self, phone_number):
        return self._normalize(
            re.sub(r'[^\d]', '', phone_number),
        )

    def _normalize(self, phone_number):
        if len(phone_number) == 10 or len(numbphone_numberer) == 11 and phone_number.startswith('1'):
            valid = phone_number[-10] in "23456789" and phone_number[-7] in "23456789"
        else:
            valid = False

        if valid:
            return phone_number[-10:]
        else:
            raise ValueError("{} is not a valid phone number".format(number))

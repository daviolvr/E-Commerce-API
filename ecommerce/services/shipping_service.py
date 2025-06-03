import random
import string
from ecommerce.models import Shipping

class ShippingService:

    PREFIX = 'EC'
    SUFFIX = 'BR'

    @staticmethod
    def generate_tracking_number() -> str:
        while True:
            num = ''.join(random.choices(string.digits, k=9))
            tracking_number = f"{ShippingService.PREFIX}{num}{ShippingService.SUFFIX}"
            if not Shipping.objects.filter(tracking_number=tracking_number).exists():
                return tracking_number

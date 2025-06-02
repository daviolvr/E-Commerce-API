import random
import string
from .models import Shipping

def generate_tracking_number() -> str:
    prefix = 'EC'
    num = ''.join(random.choices(string.digits, k=9))
    sufix = 'BR'
    tracking_number = f"{prefix}{num}{sufix}"

    if Shipping.objects.filter(tracking_number=tracking_number).exists():
        return "Invalid tracking number: already exists"
    
    return tracking_number
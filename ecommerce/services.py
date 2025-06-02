import random
import string
import uuid
from .models import Shipping, Payment

def generate_tracking_number() -> str:
    prefix = 'EC'
    sufix = 'BR'
    
    while True:
        num = ''.join(random.choices(string.digits, k=9))
        tracking_number = f"{prefix}{num}{sufix}"
        if not Shipping.objects.filter(tracking_number=tracking_number).exists():
            return tracking_number


def generate_transaction_id() -> str:
    while True:
        transaction_id = str(uuid.uuid4()).replace('-', '')[:12].upper()
        if not Payment.objects.filter(transaction_id=transaction_id).exists():
            return transaction_id
        
        
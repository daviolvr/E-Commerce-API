import uuid
from ecommerce.models import Payment

class PaymentService:

    @staticmethod
    def generate_transaction_id() -> str:
        while True:
            transaction_id = str(uuid.uuid4()).replace('-', '')[:12].upper()
            if not Payment.objects.filter(transaction_id=transaction_id).exists():
                return transaction_id

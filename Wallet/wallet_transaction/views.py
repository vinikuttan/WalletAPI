from rest_framework.response import Response
from rest_framework.views import APIView
from wallet_transaction.models import WalletUsers, Wallet, WalletTransaction
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


class NewUser(APIView):
    def post(self, request):
        payload = request.data
        user_name = payload.get("name")
        contact_num = payload["contact"]
        try:
            if WalletUsers.objects.get(contact_num=contact_num):
                return Response({"message": "User exist for this contact number"})
        except ObjectDoesNotExist:
            user = WalletUsers(name=user_name, contact_num=contact_num)
            user.save()
        return Response({"user_id": user.id, "status": "SUCCESS"})


class NewWallet(APIView):
    def post(self, request):
        payload = request.data
        user_id = payload.get("user_id")
        minimum_balance = payload.get("minimum_balance")
        try:
            if Wallet.objects.get(user_id=user_id):
                return Response({"message": "Wallet already created for this user"})
        except ObjectDoesNotExist:
            wallet = Wallet(
                user_id=user_id,
                balance=0,
                minimum_balance=minimum_balance or 0
            )
            wallet.save()
        return Response(
            {"wallet_id": wallet.id, "user_id": user_id, "status": "SUCCESS"}
        )


class Transactions(APIView):
    def post(self, request):
        payload = request.data
        transaction_type = payload.get("transaction_type")
        amount = int(payload.get("amount"))
        user_id = payload.get("user_id")
        wallet = Wallet.objects.get(user_id=user_id)
        if transaction_type.lower() == "credit":
            wallet.balance += amount
        else:
            if wallet.balance < amount:
                raise ValidationError("Insufficient balance to debit given amount")

            balance = wallet.balance - amount
            if balance <= wallet.minimum_balance:
                raise ValidationError("Fund not allowed to go down minimum balance")
            wallet.balance -= amount
        wallet.save()
        transaction = WalletTransaction(
            user_id=user_id, transaction_type=transaction_type, amount=amount
        )
        transaction.save()
        return Response({"status": "SUCCESS"})


class Balance(APIView):
    def get(self, request, user_id):
        try:
            wallet = Wallet.objects.get(user_id=user_id)
            return Response({"Balance": wallet.balance})
        except ObjectDoesNotExist:
            raise ValidationError("Wallet not created for this user")

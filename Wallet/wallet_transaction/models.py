from django.db import models

# Create your models here.


class WalletUsers(models.Model):
    name = models.TextField(null=False)
    contact_num = models.IntegerField(null=False, db_index=True)


class Wallet(models.Model):
    user_id = models.IntegerField(null=False, db_index=True)
    balance = models.IntegerField(null=True)
    minimum_balance = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class WalletTransaction(models.Model):
    user_id = models.IntegerField(null=False, db_index=True)
    transaction_type = models.TextField(null=True)
    amount = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

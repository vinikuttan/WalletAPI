from django.conf.urls import url

from wallet_transaction.views import NewUser, NewWallet, Transactions, Balance

urlpatterns = [
    url(r"^create/user$", NewUser.as_view(), name="create_user"),
    url(r"^create/wallet$", NewWallet.as_view(), name="create_wallet"),
    url(r"^transaction$", Transactions.as_view(), name="transaction"),
    url(r"^balance/(?P<user_id>.+)$", Balance.as_view(), name="balance")
]








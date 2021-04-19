# WalletAPI

### Steps to run
`cd Wallet`

### create virtual Environment (python 3.6)
`python -m venv venv`

`. venv/bin/activate` # this in mac

### Install requirements
`pip install -r requirements.txt`

#### We are Ready to test API. Let start the server
`python manage.py runserver`

The API can be accessed through curl or directly from the browser http://127.0.0.1:8000/ (used DRF in project)

### API to create user (POST)
`http://127.0.0.1:8000/create/user`

Payload to given in the browser
`{"name": "abc", "contact": "6372727373"}`

Response on successful created user
`{"user_id": 1, "status": "SUCCESS"}` # user id is auto increment

### API to create wallet (POST)
`http://127.0.0.1:8000/create/wallet`

Payload request
`{"user_id": 1, "minimum_balance": 1000}`

Response
`{"wallet_id": 1, "user_id": 1, "status": "SUCCESS"}`

### API for credit and debit transaction
`http://127.0.0.1:8000/transaction`

payload request 1 - `{"user_id": 1, "transaction_type": "credit", "amount": 5000}`
Response - `{"status": "SUCCESS"}`

payload request 2 - `{"user_id": 1, "transaction_type": "debit", "amount": 4500}`
Response - `"Fund not allowed to go down minimum balance"`

payload request 3 - `{"user_id": 1, "transaction_type": "debit", "amount": 5500}`
Response - `"Insufficient balance to debit given amount"`


### API to get balance of user (GET)
`http://127.0.0.1:8000/balance/1`
Response - `{"Balance": 5000}`




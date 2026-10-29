import os
import json 

#! A string to keep the name of the data directory 
DATA_DIR = "data"

#! Checks if the data directory is created, if it isn't creates a directory named "data"
def create_data_directory():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

#! Saves the given account data to accounts.json
def save_accounts(accounts_data):
    create_data_directory()
    file_path = os.path.join(DATA_DIR, "accounts.json")
    with open(file_path,"w") as file:
        json.dump(accounts_data,file,indent=2)

#! tries loading user accounts from accounts.json, if accounts.json doesn't exist creates demo user accounts
def load_accounts():
    create_data_directory()
    file_path = os.path.join(DATA_DIR, "accounts.json")
    if not os.path.exists(file_path):
        default_accounts = {
            "user01": {
                "username": "user01",
                "password_hash": "Test@123", 
                "account_number": "10010001",
                "balance": 2500.00,
                "status": "Active",
                "failed_attempts": 0,
                "blocked": False,
                "lockout_expiry": 0,
                "daily_deposit_total": 0.0,
                "daily_withdrawal_total": 0.0,
                "daily_transfer_count": 0,
                "last_reset_date": "2026-10-29"
            },
            "user02": {
                "username": "user02",
                "password_hash": "Test@456",
                "account_number": "10010002",
                "balance": 1500.00,
                "status": "Active",
                "failed_attempts": 0,
                "blocked": False,
                "lockout_expiry": 0,
                "daily_deposit_total": 0.0,
                "daily_withdrawal_total": 0.0,
                "daily_transfer_count": 0,
                "last_reset_date": "2026-10-29"
            },
            "user03": {
                "username": "user03",
                "password_hash": "Test@789",
                "account_number": "10010003",
                "balance": 3000.00,
                "status": "Active",
                "failed_attempts": 0,
                "blocked": False,
                "lockout_expiry": 0,
                "daily_deposit_total": 0.0,
                "daily_withdrawal_total": 0.0,
                "daily_transfer_count": 0,
                "last_reset_date": "2026-10-29"
            }
        }
        save_accounts(default_accounts)
        return default_accounts

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error reading accounts file. Initializing empty/default state.")
        return {}



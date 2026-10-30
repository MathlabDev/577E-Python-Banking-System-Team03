import os
import json 
import math
from datetime import date

#* Every path/directory that is used inside of the functions/modules and default atm cash value
#! Do not modify these UNLESS you are changing any of the paths of the files/folders or any default value is required to change
INITIAL_ATM_CASH = 5000.00
DATA_DIR = "data"
ATM_FILE = os.path.join(DATA_DIR, "atm.json")
ACCOUNTS_FILE = os.path.join(DATA_DIR, "accounts.json")

#* Creating the default accounts in the case of accounts.json not existing or being corrupt
def create_default_accounts():
    today = date.today().isoformat()

    accounts = {
        "user01": {
            "username": "user01",
            "password_hash": "Test@123", #TODO after the creation of secure hash coding, change the password hash into the required format
            "account_number": "100001",
            "balance": 2500.00,
            "status": "active",
            "failed_attempts": 0,
            "blocked": False,
            "lockout_expiry": None,
            "daily_deposit_total": 0.00,
            "daily_withdrawal_total": 0.00,
            "daily_transfer_count": 0,
            "last_reset_date": today
        },
        "user02": {
            "username": "user02",
            "password_hash": "Test@456",
            "account_number": "100002",
            "balance": 1500.00,
            "status": "active",
            "failed_attempts": 0,
            "blocked": False,
            "lockout_expiry": None,
            "daily_deposit_total": 0.00,
            "daily_withdrawal_total": 0.00,
            "daily_transfer_count": 0,
            "last_reset_date": today
        },
        "user03": {
            "username": "user03",
            "password_hash": "Test@789",
            "account_number": "100003",
            "balance": 3000.00,
            "status": "active",
            "failed_attempts": 0,
            "blocked": False,
            "lockout_expiry": None,
            "daily_deposit_total": 0.00,
            "daily_withdrawal_total": 0.00,
            "daily_transfer_count": 0,
            "last_reset_date": today
        }
    }

    return accounts


#* Is used every time inside of other functions to make sure the data folder exists
def create_data_directory():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

#* reads data from any given JSON file
def read_data_file(file_path):
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise

    except json.JSONDecodeError as error:
        raise ValueError(f"{file_path} contains invalid path for JSON file.") from error

#* Reads the account data from accounts.json and returns them. if anything is wrong in accounts.json returns the default account values
def load_accounts():
    
    create_data_directory()

    try:
        data = read_data_file(ACCOUNTS_FILE)

    except FileNotFoundError:
        data = create_default_accounts()
        save_accounts(data)

    if not isinstance(data, dict):
        raise ValueError("accounts.json must contain a dictionary.")

    return data

#* Saves given account data into the accounts.json file.
def save_accounts(accounts_data):

    create_data_directory()

    with open(ACCOUNTS_FILE,"w",encoding="utf-8") as file:
        json.dump(accounts_data,file,indent=2)

#* Saves the given amount of ATM cash left to atm.json
#? Use case: prevents the duplication of code when you eventually need to save data into atm.json file at multiple places
def save_atm_cash(amount):
    create_data_directory() 

    data = {"atm_cash": round(float(amount),2)}
    with open(ATM_FILE,"w",encoding="utf-8") as file:
        json.dump(data,file,indent = 2)

#* Reads the atm.json file and checks if the data is corrupt. if the file doesn't exist, it uses the initial atm cash value
def load_atm_cash():
    create_data_directory()

    try:
        data = read_data_file(ATM_FILE)
    except FileNotFoundError:
        save_atm_cash(INITIAL_ATM_CASH)
        return INITIAL_ATM_CASH

    if not isinstance(data,dict):
        raise ValueError("atm.json must have a dictionary inside it")

    if "atm_cash" not in data:
        raise ValueError("atm.json doesnt have the atm_cash key")

    try:
        amount = float(data["atm_cash"])
    except (ValueError,TypeError) as error:
        raise ValueError("ATM cash must be a number") from error
    
    if not math.isfinite(amount) or amount < 0:
        raise ValueError(
            "ATM cash must be finite and non-negative."
        )

    return amount
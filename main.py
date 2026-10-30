from storage import load_accounts,load_atm_cash

try:
    accounts = load_accounts()
    atm_cash = load_atm_cash
except (ValueError,OSError):
    raise ValueError("Unable to load banking data")

print("Banking system started successfully!")

if __name__ == "__main__":
    main()
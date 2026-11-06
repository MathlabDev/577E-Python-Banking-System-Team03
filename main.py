from storage import load_accounts,load_atm_cash

#* catches any errors before any of the banking processes happen
try:
    accounts = load_accounts()
    atm_cash = load_atm_cash()
except (ValueError,OSError):
    raise ValueError("Unable to load banking data")

print("Banking system started successfully!")

if __name__ == "__main__":
    main() #? Use main() when it is created here
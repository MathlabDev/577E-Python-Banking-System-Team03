def input_validation(mebleg):
    try:
        amount=float(mebleg)
    except ValueError:
        return "Yalniz reqem daxil edin"
    else:
        if amount > 0:
            return "Mebleg qebul olundu"
        else:
            return "Xeta: mebleg musbet olmalidir"
mebleg=input("Meblegi daxil edin:")
print(input_validation(mebleg))
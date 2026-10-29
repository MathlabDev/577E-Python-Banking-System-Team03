def input_validation(mebleg):
    try:
        amount=float(mebleg)
    except ValueError:
        return "Yalniz reqem daxil edin"
    else:
        if amount > 0:
            parts = mebleg.split(".") #! qepik hissesinin yoxlanilmasi
            if len(parts) == 2 and len(parts[1]) > 2:
                return "En cox 2 onluq isare olmalidir"
            else:
                return "Mebleg qebul olundu"
        else:
            return "Xeta: mebleg musbet olmalidir"
mebleg=input("Meblegi daxil edin:")
print(input_validation(mebleg))


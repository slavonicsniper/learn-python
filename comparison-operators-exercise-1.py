weight = input('Weight: ')
unit = input('(L)bs or {K}g: ')

if unit == "L" or unit == "l":
    weight_result = float(weight) / 2.205
    print("You are",weight_result,"kilos.")
elif unit == "K" or unit == "k":
    weight_result = float(weight) * 2.205
    print("You are",weight_result,"pounds.")
else:
    print("You need to enter either L or K")


smaklista1 = ["vanilj", "mango", "choklad"]
smaklista2 = ["vanilj", "mango", "choklad"]

for smak1 in smaklista1:
    for smak2 in smaklista2:
        if (smak1 != smak2):
            print(smak1, smak2)
    smaklista2.pop(0)
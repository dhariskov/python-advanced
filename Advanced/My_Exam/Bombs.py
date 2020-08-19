effects = [int(x) for x in input().split(", ")]  # queue
casings = [int(x) for x in input().split(", ")]  # stack

dict_bobs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

dict_bobs_created = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while effects and casings:
    f_effect = effects[0]
    l_casing = casings[-1]
    temp = l_casing + f_effect
    if temp in dict_bobs:
        dict_bobs_created[dict_bobs[temp]] += 1
        effects.pop(0)
        casings.pop()
    else:
        casings[-1] -= 5
        if casings[-1] < 0:
            casings.pop(0)

    if dict_bobs_created["Datura Bombs"] > 2 and \
            dict_bobs_created["Cherry Bombs"] > 2 and \
            dict_bobs_created["Smoke Decoy Bombs"] > 2:
        break

if dict_bobs_created["Datura Bombs"] > 2 and \
        dict_bobs_created["Cherry Bombs"] > 2 and \
        dict_bobs_created["Smoke Decoy Bombs"] > 2:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(casings[x]) for x in range(len(casings)-1, -1, -1)])}")
else:
    print("Bomb Casings: empty")

dict_bobs_created = dict(sorted(dict_bobs_created.items(), key=lambda x: x[0]))
# if dict_bobs_created['Cherry Bombs'] > 0:
#     print(f"Cherry Bombs: {dict_bobs_created['Cherry Bombs']}")
# if dict_bobs_created['Datura Bombs'] > 0:
#     print(f"Datura Bombs: {dict_bobs_created['Datura Bombs']}")
# if dict_bobs_created['Smoke Decoy Bombs'] > 0:
#     print(f"Smoke Decoy Bombs: {dict_bobs_created['Smoke Decoy Bombs']}")


for k, v in dict_bobs_created.items():
    print(f"{k}: {v}")

# Move to the wizard and get their secret values.
hero.moveXY(20, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = hero.findNearestFriend().getSecretC()

# If ALL three values are true, take the high path.
# Otherwise, take the low path. Save the 4th value.
secretD = secretA and secretB and secretC
if secretD:
    hero.moveXY(30, 33)
else:
    hero.moveXY(30, 15)

# If ANY of the three values are true, take the left path.
# Otherwise, go right. Save the 5th value.
secretE = secretA and secretB and secretC
if secretE:
    hero.moveXY(20, 24)
else:
    hero.moveXY(40, 25)

# If ALL five values are true, take the high path.
# Otherwise, take the low path.
secretF = secretA and secretB and secretC and secretD and secretE
if secretF:
    hero.moveXY(30, 33)
else:
    hero.moveXY(20, 24)


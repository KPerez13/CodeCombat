# Get two secret true/false values from the wizard.
# Check the guide for notes on how to write logical expressions.
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# If BOTH secretA and secretB are true, take the high path; otherwise, take the low path.
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

secretD = secretA or secretB
# If EITHER secretA or secretB is true, take the high path.
if secretD:
    hero.moveXY(32, 33)
else:
    hero.moveXY(32, 36)
hero.moveXY(38, 24)
# If secretB is NOT true, take the high path.
secretE = not secretB
if secretE:
    hero.moveXY(44, 33)
else:
    hero.moveXY(44, 15)
hero.moveXY(50, 24)

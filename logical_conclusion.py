#This one had me scratching my head for a while but the explanation
#for mixing boolean operators makes sense 
#When mixing boolean operators, NOT takes precedence over AND
#which takes precendence over OR:
#link to level: https://codecombat.com/play/level/logical-conclusion?
# Move to 'Eszter' and get three secret values from her.
hero.moveXY(24, 16)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = hero.findNearestFriend().getSecretC()

# Say "TRUE" to 'Tamas' if A AND B are true, OR if C is true. Otherwise, say "FALSE."
# Remember to use parentheses to do your logic in the proper order.
tam = (secretA and secretB) or secretC
hero.moveXY(19, 26)
hero.say(tam)

# Say "TRUE" to 'Zsofi' if A OR B is true, AND if C is true. Otherwise, say "FALSE."
zso = secretC and (secretA or secretB)
hero.moveXY(26, 36)
hero.say(zso)
# Say "TRUE" to 'Istvan' if A OR C is true, AND if B OR C is true. Otherwise, say "FALSE."
ist = secretA or secretC and secretB or secretC
hero.moveXY(37, 34)
hero.say(ist)
# Say "TRUE" to 'Csilla' if A AND B are true, OR if B is true AND C is NOT true. Otherwise, say "FALSE."
csi = (secretA and secretB) or (secretB and (not secretC))
hero.moveXY(40, 22)
hero.say(csi)


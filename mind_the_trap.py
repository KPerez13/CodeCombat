# If you try to attack a distant enemy, your hero will charge toward it, ignoring all flags.
# You'll need to make sure you only attack enemies who are close to you!
# Please note that this is an interactive level 

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        # Pick up the flag.
        hero.pickUpFlag(flag)
        hero.say("I should pick up the flag.")
    elif enemy:
        # Only attack if the enemy distance is < 10 meters
        if hero.distanceTo(enemy) < 10:
            hero.attack(enemy)


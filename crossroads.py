# Use "fire-trap"s to defeat the ogres.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # If the enemy is to the left of the hero:
        if enemy.pos.x < hero.pos.x:
            # buildXY a "fire-trap" on the left X.
            hero.buildXY("fire-trap", hero.pos.x-10,hero.pos.y)
            pass
        # If the enemy is to the right of the hero:
        elif enemy.pos.x > hero.pos.x:
            # buildXY a "fire-trap" on the right X.
            hero.buildXY("fire-trap", hero.pos.x+10,hero.pos.y)
            pass
        # If the enemy is below the hero:
        elif enemy.pos.y < hero.pos.y:
            # buildXY a "fire-trap" on the bottom X.
            hero.buildXY("fire-trap", hero.pos.x,hero.pos.y-10)
            pass
        # If the enemy is above the hero:
        elif enemy.pos.y > hero.pos.y:
            # buildXY a "fire-trap" on the top X.
            hero.buildXY("fire-trap", hero.pos.x,hero.pos.y+10)
            pass
    # Move back to the center.
    hero.moveXY(40, 34)


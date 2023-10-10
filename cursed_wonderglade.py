#soultion 1:
# Wonderglade has changed since our last visit.
# Ogres cursed it and we should defeat them.
# The burl still is collecting gems, so don't touch them.
# Also don't attack the burl.

while True:
    # Find the nearest item.
    # Collect it (if it exists) only if its type isn't "gem".
    item = hero.findNearestItem()
    if item:
        if item.type != "gem":
            hero.moveXY(item.pos.x, item.pos.y)
    # Find the nearest enemy.
    enemy = hero.findNearestEnemy()
    if enemy.type != "burl":
        hero.attack(enemy)
    pass

#Solution 2 and the preferred one tbh since it's shorter :D 
# Wonderglade has changed since our last visit.
# Ogres cursed it and we should defeat them.
# The burl still is collecting gems, so don't touch them.
# Also don't attack the burl.

while True:
    # Find the nearest item.
    # Collect it (if it exists) only if its type isn't "gem".
    item = hero.findNearestItem()
    if item and item.type != "gem":
        hero.moveXY(item.pos.x, item.pos.y)
        
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type != "burl":
        hero.attack(enemy)
    pass


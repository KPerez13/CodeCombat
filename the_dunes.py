# Collect coins. Ignore "sand-yak"s and "burl"s.
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if enemy.type == "sand-yak" or enemy.type == "burl":
            # Don't attack! Collect coins.
            hero.moveXY(itemX, itemY)
            pass
        else:
            # Else, attack.
            hero.attack(enemy)
            pass
        
    elif item:
        # Collect coins: move to item's position.
        itemPos = item.pos
        itemX = item.pos.x
        itemY = item.pos.y
        hero.moveXY(itemX, itemY)
        pass
    else:
        hero.moveXY(41, 31)


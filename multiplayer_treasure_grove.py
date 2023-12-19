# Be the first to 100 gold!
# If you are defeated, you will respawn at 67% gold.
## Solution 1(didn't work)
while True:
    #  Find coins and/or attack the enemy.
    # Use flags and your special moves to win!
    while True:
        flag = hero.findFlag()
        enemy = hero.findNearestEnemy()
        item = hero.findNearestItem()
        distance = hero.distanceTo(enemy)
        
        if enemy and distance < 5:
            hero.attack(enemy)
        elif item:
            itemPos = item.pos
            itemX = item.pos.x
            itemY = item.pos.y
            hero.moveXY(itemX, itemY)
        else:
            if flag:
                flagPos = flag.pos
            flagX = flag.pos.x
            flagY = flag.pos.y
            hero.pickUpFlag(flag)

## Solution 2(also doesn't work, characther chases enemy too much):
# Be the first to 100 gold!
# If you are defeated, you will respawn at 67% gold.

while True:
    #  Find coins and/or attack the enemy.
    # Use flags and your special moves to win!
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    distance = hero.distanceTo(item)
    
    if item and distance < 5:
        itemPos = item.pos
        itemX = item.pos.x
        itemY = item.pos.y
        hero.moveXY(itemX, itemY)
    elif flag:
        flagPos = flag.pos
        flagX = flag.pos.x
        flagY = flag.pos.y
        hero.pickUpFlag(flag)
    else:
        if enemy:
            hero.attack(enemy)


## Proposed Solution 3(also didn't work), while it does chase the enemy less, it isn't as fast to get the coins)
# Be the first to 100 gold!
# If you are defeated, you will respawn at 67% gold.

while True:
    #  Find coins and/or attack the enemy.
    # Use flags and your special moves to win!
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    distance = hero.distanceTo(item)
    
    if item:
        itemPos = item.pos
        itemX = item.pos.x
        itemY = item.pos.y
        hero.moveXY(itemX, itemY)
    elif flag:
        flagPos = flag.pos
        flagX = flag.pos.x
        flagY = flag.pos.y
        hero.pickUpFlag(flag)
    else:
        if enemy and distance < 5:
            hero.attack(enemy)


#Proposed Solution 4
# Be the first to 100 gold!
# If you are defeated, you will respawn at 67% gold.
## Solution 1(didn't work)
while True:
    #  Find coins and/or attack the enemy.
    # Use flags and your special moves to win!
    while True:
        flag = hero.findFlag()
        enemy = hero.findNearestEnemy()
        item = hero.findNearestItem()
        distance = hero.distanceTo(item)

        if flag:
            flagPos = flag.pos
            flagX = flag.pos.x
            flagY = flag.pos.y
            hero.pickUpFlag(flag)
        elif item:
            itemPos = item.pos
            itemX = item.pos.x
            itemY = item.pos.y
            hero.moveXY(itemX, itemY)
        else:
            if enemy:
                hero.attack(enemy)


# After trying many iterations and solutions I finally found a solution
# Albeit this does require you to use flags to get 100 coins faster. 

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if flag:
        flagPos = flag.pos
        flagX = flagPos.x
        flagY = flagPos.y
        hero.pickUpFlag(flag)
    elif item:
        itemPos = item.pos
        itemX = itemPos.x
        itemY = itemPos.y
        if hero.distanceTo(item) < 5:
            hero.moveXY(itemX, itemY)
    elif enemy and hero.isReady("cleave"):
        hero.cleave(enemy)
    elif enemy and hero.isReady("attack"):
        hero.attack(enemy)


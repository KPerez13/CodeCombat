# Grab all the coins and use flags to build traps behind
# you to deal with those ogres.
# Please note that this is an interactive level

while True:
    flag = hero.findFlag()
    item = hero.findNearestItem()
    if flag:
        flagPos = flag.pos
        flagX = flag.pos.x
        flagY = flag.pos.y
        hero.buildXY("fire-trap", flagX, flagY)
        hero.pickUpFlag(flag)
    elif item:
        itemPos = item.pos
        itemX = item.pos.x
        itemY = item.pos.y
        hero.moveXY(itemX, itemY)
        

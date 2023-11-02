# Put flags where you want to build traps.
# When you're not building traps, pick up coins!
# This is an interactive level, so this code by itself won't solve things


while True:
    flag = hero.findFlag()
    if flag:
        # How do we get flagX and flagY from the flag's pos?
        # (Look below at how to get x and y from items.)
        flagPos = flag.pos
        flagX = flag.pos.x
        flagY = flag.pos.y     
        hero.buildXY("fire-trap", flagX, flagY)
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            hero.moveXY(itemX, itemY)


#Hunt all the ogres
#Collect all the coins
@Combine everything you know to venture thorugh the groves!
#Remember while-true loops, if/else, flags, cleave(), attack(), pos, and moveXY()
#Keep in mind this is an interative level 
# Use "if" and "else if" to handle any situation.
# Put it all together to defeat enemies and pick up coins!
# Make sure you bought great armor from the item shop! 400 health recommended.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if flag:
        # What happens when I find a flag?
        hero.pickUpFlag(flag)
    elif enemy:
        # What happens when I find an enemy?
        hero.attack(enemy)
    elif item:
        # What happens when I find an item?
        itemPos = item.pos
        itemX = item.pos.x
        itemY = item.pos.y
        hero.moveXY(itemX, itemY)
        

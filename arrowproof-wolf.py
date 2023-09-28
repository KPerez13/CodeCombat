# Collect mushrooms.

# First, come to the wolf pet and wake up it (say).
hero.moveXY(12, 34)
hero.say("Wake up!")
while True:
    item = hero.findNearestItem()
    if item:
        pos = item.pos
        x = item.pos.x
        y = item.pos.y
        hero.moveXY(x, y

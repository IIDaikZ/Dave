init python:
    def addItemsToSet(itemName):
        global itemsAreAdded
        if len(added_items) != 3:
            added_items.add(itemName)
        if len(added_items) == 3:
            itemsAreAdded = True

    def checkAddedItems():
        global amountOfTimesFailed
        global added_items
        global itemsAreAdded
        if "rot" in added_items and "gelb" in added_items and "pink" in added_items:
            renpy.jump("drogenScene")
        else:
            if len(added_items) == 3:
                added_items = set()
                itemsAreAdded = False
                amountOfTimesFailed += 1
                if amountOfTimesFailed == 3:
                    renpy.jump("todesSzene")

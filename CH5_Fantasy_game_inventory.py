#! python 3
# Fantasy game inventory + list_to_dict function
stuff = {'Arrows': 2, 'Belt': 1, 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'Arrows': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print ('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print (k,v)
        item_total += v
    print ('Total: ' + str(item_total))

def addToInventory(inventory, addedItems):
    print ('Items to be added: ' + str(addedItems))
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    print ('New Inventory: ')

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)

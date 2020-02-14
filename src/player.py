# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # the method is called when the object is created to initialize the attributs of the class (remember that self represents the instance of the class and binds the attributes with given arguments.)
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room

        #multiple items
        self.items = items

    #Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser
    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

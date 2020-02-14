# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description

        #multiple items in rooms
        self.items = items

    #Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser
    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
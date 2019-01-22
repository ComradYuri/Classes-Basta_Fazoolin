# Creates Business that takes in the name and the franchises
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Creates Franchise that takes in address and list of menus. Also has a method .available_items that returns a
# list of available items at the specified time
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    # makes string representation set to the address
    def __repr__(self):
        return self.address
    # checks time with menu times and returns list of menus (e.g. brunch, dinner, kids)
    def available_items(self, time):
        available = []
        for menu in self.menus:
            if menu.end_time >= time >= menu.start_time:
                available.append(menu)
        return available


# Takes in menu name, a dictionary of items w/ prices and the start/end time of said menu
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {} is available from {} to {}".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price


# menu lists
brunch_list = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
earlybird_list = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
dinner_list = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
kids_list = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
arepas_list = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# menu lists converted into menus
brunch = Menu("Brunch menu", brunch_list, 1100, 1600)
earlybird = Menu("Early-bird menu", earlybird_list, 1500, 1800)
dinner = Menu("Dinner menu", dinner_list, 1700, 2300)
kids = Menu("Kids menu", kids_list, 1100, 2100)
arepas = Menu("Arepas menu", arepas_list, 1000, 2000)

print(brunch)
bill_1 = brunch.calculate_bill(['crostini with eggplant caponata', 'pancakes'])
print(bill_1)
bill_2 = earlybird.calculate_bill(['salumeria plate', 'pancakes'])
print(bill_2)

# create franchises
flagship_store = Franchise("1232 West End Road", [brunch, earlybird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, earlybird, dinner, kids])
arepas_installment = Franchise("189 Fitzgerald Avenue", [arepas])
print(flagship_store.available_items(1700))

# create businesses
old_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
new_business = Business("Take a' Arepa", [arepas_installment])

# prints available items from franchise at index 0 (flagship) for the old business (no arepas yet)
print(old_business.franchises[0].available_items(1100))

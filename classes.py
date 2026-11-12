class Station:
    def __init__(self, name, bikes):
        self.name = name
        self.bikes = bikes
    def take_bike(self, number):
        pass
    def add_bike(self, bike):
        pass
    def bike_count(self):
        pass

class Client:
    def __init__(self, name, balance, bike):
        self.name = name
        self.balance = balance
    def ride(self, minutes):
        pass
    def return_bike(self, station, minutes):
        pass
    def pay(self, amount):
        pass


class Bike:
    def __init__(self, number, is_electric,  price_per_minute = 2):
        self.number = number
        self.is_electric = is_electric
        self.price_per_minute = price_per_minute if not is_electric else 5
    def cost(self, minutes):
        pass
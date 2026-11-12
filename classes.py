class Station:
    def __init__(self, name):
        self.name = name
        self.bikes = []
    def add_bike(self, bike):
        self.bikes.append(bike)
    def bike_count(self):
        return len(self.bikes)
    def remove_bike(self, number):
        for bike in self.bikes:
            if bike.number == number:
                self.bikes.remove(bike)
                return bike
        return None

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bike = None
    def pay(self, amount):
        self.balance -= amount


class Bike:
    def __init__(self, number, is_electric,  price_per_minute = 2):
        self.number = number
        self.is_electric = is_electric
        self.price_per_minute = price_per_minute if not is_electric else 5
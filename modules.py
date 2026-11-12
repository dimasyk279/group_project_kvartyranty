
_earned = 0
def calc_cost(minutes, bike):
    return minutes * bike.price_per_minute
def take_bike(client, station, number):
    bike = station.remove_bike(number)
    if bike is None:
        return False
    client.bike = bike
    return True

def return_bike(client, station,minutes):
    global _earned
    cost = calc_cost(minutes, client.bike)
    client.pay(cost)
    station.add_bike(client.bike)
    client.bike = None
    _earned += cost
    return cost

def total_earned():
    return _earned

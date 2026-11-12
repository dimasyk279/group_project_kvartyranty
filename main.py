from modules import *
from classes import *

def print_report(stations):
    for station in stations:
        print(f" Станція{station.name} має {station.bike_count()} велосипедів")
        print(f"Заробила {total_earned()} грн")
def main():
    station_a = Station("A")
    station_b = Station("B")

    station_a.add_bike(Bike(1, is_electric=True))
    station_a.add_bike(Bike(2, is_electric=False))
    station_a.add_bike(Bike(3, is_electric=False))
    station_b.add_bike(Bike(4, is_electric=True))
    station_b.add_bike(Bike(5, is_electric=False))

    olya = Client("Оля", 500)
    ivan = Client("Іван", 300)

    take_bike(olya, station_a, 1)
    return_bike(olya, station_b, 20)
    take_bike(ivan, station_a, 2)
    return_bike(ivan, station_b, 10)
    take_bike(olya, station_a, 3)
    return_bike(olya, station_b, 15)

    if not take_bike(ivan, station_a, 1):
        print("На станції A немає велосипедів")

    print(f"{olya.name}: {olya.balance} грн")
    print(f"{ivan.name}: {ivan.balance} грн")

    print_report([station_a, station_b])

    assert station_a.bike_count() == 0
    assert olya.balance == 370  # 500 - 100 - 30
    assert total_earned() == 150  # 100 + 20 + 30


if __name__ == "__main__":
    main()

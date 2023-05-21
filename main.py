from models.trolleybus import Trolleybus
from models.car import Car
from manager.transport_manager import TransportManager
from models.train import Train
from models.tram import Tram

if __name__ == "__main__":
    transport_manager = TransportManager()
    transport_manager.add_transport(Tram(100, 30, 25, 50))
    transport_manager.add_transport((Tram(100, 60, 17, 45)))
    transport_manager.add_transport(Train(100, 80, 6, 68))
    transport_manager.add_transport(Train(100, 70, 5, 80))
    transport_manager.add_transport(Trolleybus(100, 40, 27, "Naukova",50, 35, 6))
    transport_manager.add_transport(Trolleybus(100, 30, 15,"Stryyska", 42, 50, 12))
    transport_manager.add_transport(Car(100, 4, 150, 4, 230, 250))
    transport_manager.add_transport(Car(100, 8, 125, 8, 250, 500))

    for transport in transport_manager.transport_list:
        print(transport)

    transport_manager.find_all_with_speed_greater_than(45)
    transport_manager.find_all_with_quantity_of_passengers_greater_than(10)

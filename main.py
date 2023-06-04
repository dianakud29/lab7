from models.trolleybus import Trolleybus
from models.car import Car
from manager.transport_manager import TransportManager
from manager.set_manager import SetManager
from models.train import Train
from models.tram import Tram
from exceptions.redundant_refuel_exception import RedundantRefuelException
from decorators.decorators import logged


@logged(RedundantRefuelException, mode="console")
def template_method(transport):
    transport.refuel()


if __name__ == "__main__":
    trolleybus = Trolleybus()
    template_method(trolleybus)
    transport_manager = TransportManager()

    transport_manager.add_transport(Tram(100, 30, 25, 50))
    transport_manager.add_transport(Tram(100, 60, 17, 45))
    transport_manager.add_transport(Train(100, 80, 6, 68))
    transport_manager.add_transport(Train(100, 70, 5, 80))
    transport_manager.add_transport(Trolleybus(100, 40, 27, "Naukova", 50, 35, 6))
    transport_manager.add_transport(Trolleybus(100, 30, 15, "Stryyska", 42, 50, 12))
    transport_manager.add_transport(Car(100, 4, 150, 4, 230, 250))
    transport_manager.add_transport(Car(100, 8, 125, 8, 250, 500))

    print("List of transports:")
    for transport in transport_manager.transport_list:
        print(transport)

    print("\nTransports with speed greater than 45:")
    transport_manager.find_all_with_speed_greater_than(45)

    print("\nTransports with quantity of passengers greater than 10:")
    transport_manager.find_all_with_quantity_of_passengers_greater_than(10)

    # Додати об'єкти в transport_manager
    transport_manager.add_transport(Train(100, 80, 6, 68))
    transport_manager.add_transport(Train(100, 70, 5, 80))

    # Використання методу get_enumerated_objects()
    print("\nEnumerated objects:")
    enumerated_objects = transport_manager.get_enumerated_objects()
    for index, transport in enumerated_objects:
        print(f"Object {index}: {transport}")

    # Використання методу get_results_and_objects()
    print("\nResults and objects:")
    results_and_objects = transport_manager.get_results_and_objects()
    for transport, result in results_and_objects:
        print(f"Object: {transport}, Result: {result}")

    # Використання методу get_attributes_by_type()
    print("\nAttributes of type int:")
    attributes = transport_manager.get_attributes_by_type(int)
    print(attributes)

    # Використання методу check_conditions()
    print("\nCheck conditions:")
    condition = lambda transport: transport.max_speed > 70
    conditions_result = transport_manager.check_conditions(condition)
    print(conditions_result)

    set_manager = SetManager(transport_manager)
    print(len(set_manager))

    # Використання ітерації по об'єкту SetManager
    print("\nItems in SetManager:")
    for item in set_manager:
        print(item)

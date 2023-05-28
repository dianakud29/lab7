from models.transport import Transport
from decorators.decorators import print_iterable_length, print_method_name


class TransportManager:
    def __init__(self):
        """Initializes a new instance of the TransportManager class"""
        self.transport_list = []

    def add_transport(self, transport: Transport):
        """Add a transport object to the transport list"""
        self.transport_list.append(transport)

    @print_iterable_length
    def find_all_with_speed_greater_than(self, value: int):
        """Find and print all transports with speed greater than a given value"""
        print(f'All transports with speed greater than{value}km:')
        filtered_transports = [transport for transport in self.transport_list if transport.max_speed > value]
        for transport in filtered_transports:
            print(transport)

    @print_iterable_length
    def find_all_with_quantity_of_passengers_greater_than(self, value: int):
        """ Find and print all transports with quantity of passengers greater than a given value"""
        print(f'All transports with quantity of passengers greater than{value}:')
        filtered_transports = [transport for transport in self.transport_list if
                               transport.quantity_of_passengers > value]
        for transport in filtered_transports:
            print(transport)

    @print_method_name
    def __len__(self):
        """Returns the number of transports in the manager"""
        return len(self.transport_list)

    @print_method_name
    def __getitem__(self, index):
        """Returns the transport at the specified index"""
        return self.transport_list[index]

    def __iter__(self):
        """Returns an iterator over the transports in the manager"""
        return iter(self.transport_list)

    def get_enumerated_objects(self):
        """Returns a list of enumerated transports"""
        return [(i, transport) for i, transport in enumerate(self.transport_list)]

    def get_results_and_objects(self):
        """Returns a list of results and corresponding transport objects"""
        return [(transport, transport.refuel()) for transport in self.transport_list]

    def get_attributes_by_type(self, attribute_type):
        """Returns a dictionary of transport attributes by type"""
        return {key: value for transport in self.transport_list for key, value in transport.__dict__.items()
                if isinstance(value, attribute_type)}

    def check_conditions(self, condition):
        """Checks conditions on transports in the manager"""
        return {"all": all(condition(transport) for transport in self.transport_list),
                "any": any(condition(transport) for transport in self.transport_list)}

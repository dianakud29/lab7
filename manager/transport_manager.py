from models.transport import Transport


class TransportManager:
    __transport_list = list()

    def add_transport(self, transport: Transport):
        self.transport_list.append(transport)

    def find_all_with_speed_greater_than(self, value: int):
        print(f'All transports with speed greater than{value}km:')
        filtered_transports = [transport for transport in self.transport_list if transport.max_speed > value]
        for transport in filtered_transports:
            print(transport)

    def find_all_with_quantity_of_passengers_greater_than(self, value: int):
        print(f'All transports with quantity of passengers greater than{value}:')
        filtered_transports = [transport for transport in self.transport_list if
                               transport.quantity_of_passengers > value]
        for transport in filtered_transports:
            print(transport)

    @property
    def transport_list(self):
        return self.__transport_list

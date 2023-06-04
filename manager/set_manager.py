from manager.transport_manager import TransportManager


class SetManager:
    """Initializes a new instance of the LockSetManager class"""

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        """Returns an iterator over the lock sets in the manager"""
        for transport in self.regular_manager.transport_list:
            yield from transport.lock_set

    def __len__(self):
        """ Returns the total number of locks in the manager"""
        total_len = 0
        for transport in self.regular_manager.transport_list:
            total_len += len(transport.lock_set)
        return total_len

    def __getitem__(self, index):
        """ Returns the lock at the specified index"""
        count = 0
        for transport in self.regular_manager.transport_list:
            if count <= index < count + len(transport.lock_set):
                inner_index = index - count
                return list(transport.lock_set)[inner_index]
            count += len(transport.lock_set)
        raise IndexError("list index out of range")

    def __next__(self):
        """Returns the next item in the manager"""
        for transport in self.regular_manager:
            for item in transport.data_set:
                yield item

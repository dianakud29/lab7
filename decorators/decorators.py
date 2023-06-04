import logging


def print_iterable_length(func):
    """ Decorator that prints the length of an iterable object returned by the function"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, '__iter__'):
            print(f'Iterable length: {len(result)}')
        else:
            print('Iterable length: 1')
        return result

    return wrapper


def print_method_name(func):
    """Decorator that prints the name of the method being called"""

    def wrapper(*args, **kwargs):
        method_name = func.__name__
        print(f'Calling method: {method_name}')
        return func(*args, **kwargs)

    return wrapper


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.INFO)
                logging.exception(e)

        return wrapper

    return decorator

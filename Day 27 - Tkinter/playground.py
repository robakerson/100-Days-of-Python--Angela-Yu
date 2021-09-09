def add(*args):
    ttl = 0
    for n in args:
        ttl += n
    return ttl


def calculate(value, **kwargs):  # unlimited key word arguments!
    # print(kwargs)  # kwargs is a dictionary
    # for key, value in kwargs.items():
    #     print(key)
    # print(kwargs["add"])
    value += kwargs["add"]
    value *= kwargs["multiply"]
    print(value)


calculate(2, add=3, multiply=5)

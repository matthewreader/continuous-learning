class Scoop:
    """A simple class representing one scoop of ice cream"""
    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():
    """Creates three scoops of ice cream using the Scoop class and prints their value to the console"""
    scoops = [Scoop("chocolate"),
              Scoop("vanilla"),
              Scoop("persimmon")]
    for scoop in scoops:
        print(scoop.flavor)


create_scoops()

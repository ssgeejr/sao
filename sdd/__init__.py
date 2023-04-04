from ScoobyDoo import ScoobyDoo
from MysteryMachine import MysteryMachine

__version__ = "1.0.0"


def main():
    mm = MysteryMachine()
    scooby = ScoobyDoo()
    scooby.solve_mystery(mm)
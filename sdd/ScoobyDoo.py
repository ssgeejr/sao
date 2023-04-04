from MysteryMachine import MysteryMachine
import argparse


class ScoobyDoo:
    def __init__(self, name="Scooby Doo", age=7):
        self.name = name
        self.age = age

    def __init__(self):
        print("it's time to solve a mystery")

    def solve_mystery(self, mystery):
        print(mystery.openai_orgid)


if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser(description="Scooby Doo module for solving mysteries.")
    parser.add_argument("mystery", type=str, help="the mystery to be solved")
    parser.add_argument("--name", type=str, help="the name of the character (default: Scooby Doo)",
                        default="Scooby Doo")
    parser.add_argument("--age", type=int, help="the age of the character (default: 7)", default=7)

    args = parser.parse_args()
    
    scooby = ScoobyDoo(name=args.name, age=args.age)
    scooby.solve_mystery(mystery=args.mystery)
    '''
    mm = MysteryMachine()
    scooby = ScoobyDoo()
    scooby.solve_mystery(mm)
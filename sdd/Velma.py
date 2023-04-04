from MysteryMachine import MysteryMachine
import openai

mystery_machine = MysteryMachine()
openai.api_key = mystery_machine.get_api_key()
openai.organization = mystery_machine.get_organization()


def queryAI():
    response = openai.Engine.list()

    # Print the engine names
    for engine in response['data']:
        print(engine.id)


def main():
    queryAI()


if __name__ == "__main__":
    main()

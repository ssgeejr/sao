from MysteryMachine import MysteryMachine
import openai

mystery_machine = MysteryMachine()
openai.api_key = mystery_machine.get_api_key()
openai.organization = mystery_machine.get_organization()

engine_descriptions = {
    "ada": "The most cost-efficient engine, suitable for simpler tasks and when quick or short answers are needed.",
    "babbage": "A more budget-friendly option, which can handle many tasks but may not be as adept at understanding complex contexts or generating detailed responses.",
    "curie": "A less expensive but still highly capable engine, suitable for a wide range of tasks that do not require the full power of the davinci engine.",
    "davinci": "The most powerful and capable engine, with the most nuanced understanding and ability to generate detailed and accurate responses.",
    "davinci-codex": "A variant of davinci that is optimized for code-related tasks, providing a strong capability to work with programming languages and development tasks.",
}

def queryAI():
    response = openai.Engine.list()

    # Print the engine names
    for engine in response['data']:
        print(engine.id)


def main():
    queryAI()


if __name__ == "__main__":
    main()

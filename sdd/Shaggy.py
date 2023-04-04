from MysteryMachine import MysteryMachine
import openai

mystery_machine = MysteryMachine()
openai.api_key = mystery_machine.get_api_key()
openai.organization = mystery_machine.get_organization()

# Read the Java file content



def analyze_vulnerabilities():
    java_code = ''
    java_file_path = "TestCode.java"
    with open(java_file_path, "r") as file:
        java_code = file.read()

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"analyze the following Java code for vulnerabilities {java_code}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    vulnerabilities = response.choices[0].text.strip()
    print("Potential vulnerabilities found:\n", vulnerabilities)


def main():
    analyze_vulnerabilities()


if __name__ == "__main__":
    main()

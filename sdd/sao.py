import os, sys
import openai

# Define the path to the file
home_directory = os.path.expanduser('~')
file_path = os.path.join(home_directory, '.openai', 'openapi.pk')
message = None
OPENAI_API_KEY = None

# Open the file and read its contents
with open(file_path, 'r') as f:
    contents = f.read()

# Parse the key-value pair from the file contents
for line in contents.split('\n'):
    key, value = line.split('=')
    if key == 'openai_key':
        OPENAI_API_KEY = value.strip()

if not OPENAI_API_KEY:
    print("OpenAI Key Required to continue")
    sys.exit(1)
else:
    # The variable is not empty or null, so assign a value to it
    openai.api_key = OPENAI_API_KEY

# Define prompt and parameters
prompt = "What state has the best BBQ in the US?"
temperature = 0.5
max_tokens = 60

# Generate response using OpenAI API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Extract generated text from API response
generated_text = response.choices[0].text.strip()

# Print generated text
print(generated_text)

sys.exit(1)
messages = [{"role": "user", "content": 'As an intelligent AI model, if you could be any fictional character, who would you choose and why?'}]

response = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens=100,
    temperature=1.2,
    messages=message)

print(response)
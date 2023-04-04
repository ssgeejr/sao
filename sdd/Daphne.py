import os, sys, re
import openai, requests, json

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

#endpoint = "https://api.openai.com/v1/engines/davinci-codex/codex-recommendations"
#endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
#endpoint = "https://api.openai.com/v1/engines/davinci-codex-2022.03.10/completions"
endpoint = "https://api.openai.com/v1/engines/davinci/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

code = """
Identify security vulnerabilities in the following Python code:

package com.redisdeveloper.basicchat.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.redis.connection.Message;
import org.springframework.data.redis.connection.MessageListener;
import org.springframework.stereotype.Service;

import java.util.concurrent.CopyOnWriteArrayList;
import java.util.function.Function;

@Service
public class RedisMessageSubscriber implements MessageListener {
    private static final Logger LOGGER = LoggerFactory.getLogger(RedisMessageSubscriber.class);

    CopyOnWriteArrayList<Function<String, Integer>> handlers = new CopyOnWriteArrayList<>();

    @Override
    public void onMessage(final Message message, final byte[] pattern) {
        String messageBody = new String(message.getBody());

        LOGGER.debug("Received message in global subscriber: "+ message.toString());

        for (Function<String, Integer> handler : handlers) {
            handler.apply(messageBody);
        }
    }

    public void attach(Function<String, Integer> handler) {
        handlers.add(handler);
    }
    public void detach(Function<String, Integer> handler) {
        handlers.removeIf(e -> e.equals(handler));
    }
}
"""




data = {
    "prompt": code,
    "max_tokens": 2048,
    "n": 1,
    "stop": "\n",
    "temperature": 0.7
}

# Send the API request and print the response
response = requests.post(endpoint, headers=headers, json=data)
#print(response.json())

#response = requests.post(endpoint, headers=headers, json=data, stream=True)

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(response)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

'''
for chunk in response.iter_lines():
    if chunk:
        response_json = json.loads(chunk.decode("utf-8"))
        print(response_json)
'''
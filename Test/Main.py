import os
import openai
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

openai.api_key = os.environ.get('OPENAI_API_KEY')
model_id = 'gpt-3.5-turbo'


def chatgpt_converstion(conversation_log):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation_log
    )

    conversation_log.append({
        'role': response.choices[0].message.role,
        'content': response.choices[0].message.content.strip()
    })

    return conversation_log


conversations = []
conversations.append({'role': 'user', 'content': 'Tell me a joke'})
conversations = chatgpt_converstion(conversations)
print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))



# while True:
#     promt = input('User:')
#     conversations.append({'role': 'user',
#                           'content': promt})
#     conversations = chatgpt_converstion(conversations)
#     print()
#     print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))


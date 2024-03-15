import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


# messages = [{"role": "user", "content": "What is the capital of New York?"}]
# try:
#     response = client.chat.completions.create(model="gpt-3.5-turbo",
#     messages=messages,
#     temperature=0)

#     print(response.choices[0].message.content)
# except Exception as e:
#     print(e)

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    return response.choices[0].message["content"]

prompt = "What is the capital of New York?"
get_completion(prompt) # model and temperature will use default values

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]
from openai import OpenAI
from openai_tutorial import openai_api_key

client = OpenAI(api_key= openai_api_key)

MODEL = "gpt-3.5-turbo-1106"

want_to="""너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
content
{}"""

content = "멋사 파이썬 백엔드 9기에 가면 세계 최고의 인재가 모여있다"

# GPT에게 질문하고 응답 받는 함수
while True:
    def ask_to_gpt(messages):
        response = client.chat.completions.create(
            model=MODEL,
            top_p=0.1,
            temperature=0.1,
            messages=messages,
        )

        return response.choices[0].message.content

    messages=[
            {'role': 'system', 'content': want_to.format(content)},
        ]

    user_input = input('You: ')

    messages.append(
        {'role': 'user', 'content': user_input},
    )

    response = ask_to_gpt(messages)

    print(response)
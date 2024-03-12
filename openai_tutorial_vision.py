from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


openai_api_key = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=openai_api_key)
Model="gpt-4-vision-preview"

response = client.chat.completions.create(
model=Model,
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지는 무슨 내용이니?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://mblogthumb-phinf.pstatic.net/MjAxOTAyMDlfMTM0/MDAxNTQ5NjQ1MjgwMjM2.vzj3ctwr9PixJUOXV9iXLFCwC1zTAP7qGmWVGdJjGP0g.o56rSLRdk-77Oc7F-vU2hMAjgZBD3WbQYIbQAVMQn4gg.JPEG.dnjsifjqjd/20190208_182826.jpg?type=w800",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
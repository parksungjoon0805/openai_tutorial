from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image
import requests
import os

load_dotenv()

openai_api_key = os.getenv("OPEN_API_KEY")
MODEL = "dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model=MODEL,
    prompt="흰색 털 위주에 검은색 털이 눈과 귀에만 들어가 있고 정수리 쪽에는 하얀 털이 많고 눈썹이 연갈색인 장모 치와와 그려줘",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url


# 저장파일 이름 설정
filename = "image.jpg"
response = requests.get(image_url)
with open(filename,'wb') as f:
    f.write(response.content)
Image.open(filename)

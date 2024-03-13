from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
  organization=os.getenv("Personal"),
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[{"role": "user", "content": "Say this is a test"}], # Serega LOX
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        
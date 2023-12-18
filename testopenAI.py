# '''example completion with openai > 1.1'''
# from openai import AsyncOpenAI
# client = AsyncOpenAI()
# prompt = "True or false: a banana is smaller than a lemon.\n\n"

# response = await client.completions.create(
#     prompt=prompt,
#     model="gpt-3.5-turbo-instruct",
#     top_p=0.5, max_tokens=50,
#     stream=True)
# for part in response:
#     print(part.choices[0].text or "")
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main():
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())
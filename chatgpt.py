import os
import sys
import time
import asyncio
# import openai
from openai import AsyncOpenAI
client = AsyncOpenAI()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = OPENAI_API_KEY
systemPrompt = { "role": "system", "content": "You are a helpful assistant." }
data = []

async def get_response(incoming_msg) -> None:
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:  
        data.append({"role": "assistant", "content": incoming_msg})

    messages = [ systemPrompt ]
    messages.extend(data)
    try:
        stream = await client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            stream=True)
        content=""
        async for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")
            content=content+ (chunk.choices[0].delta.content or "")
            # content = response["choices"][0]["message"]["content"]
        return content
    except Exception as e:
    # Print the type of the exception
        print(f"Exception Type: {type(e).__name__}")
        return ""

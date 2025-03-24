
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
from browser_use import BrowserConfig
import asyncio

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
os.environ["HTTP_PROXY"]  = "http://127.0.0.1:7890"

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', client_options={
                "api_endpoint": 'https://gateway.ai.cloudflare.com/v1/e113d446794efa80c8059ef000db1600/ration/google-ai-studio'
            },api_key=SecretStr(api_key)) # type: ignore

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
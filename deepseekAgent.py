
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
from browser_use import BrowserConfig
import asyncio

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
os.environ["HTTP_PROXY"]  = "http://127.0.0.1:7890"

# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key)) # type: ignore

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
        use_vision=False
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
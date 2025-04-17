from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig, Controller
import os
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))
browser = Browser()

async def main(natural_input):

    task = f"""
    You are a medical reminder assistant.
    Extract the following from this sentence:
    1. medication_name
    2. dosage
    3. frequency
    4. duration_days

    Sentence: "{natural_input}"

    Respond only in JSON format.
        """
    
    agent=Agent(
        task=task,
        llm=llm
    )
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv
from pydantic import SecretStr
import asyncio
import sys
from time import sleep

load_dotenv()

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# Loading API key
api_key = os.getenv("GEMINI_API_KEY")

# Initializing Gemini LLM
llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash-exp',
    temperature=0.2,
    api_key=SecretStr(api_key)
)

# Declaring JSON parser
parser = JsonOutputParser()

# Defining prompt template for medication data extraction
medication_data_extraction_prompt = PromptTemplate.from_template("""
You are a medical reminder assistant.
Extract structured information from the following sentence and return it as a dictionary in JSON format.

Keys to extract:
- medication_name
- dosage
- frequency (must be one of: "every morning", "every afternoon", "every night", 
  "every morning and night", "every morning and afternoon", 
  "every afternoon and night", "every morning, afternoon, and night")
- duration_days (as an integer)

Sentence: "{input}"
{format_instructions} 
""".strip()) 

# Defining a chain for medication data extraction
medication_data_extraction_chain = medication_data_extraction_prompt | llm | parser # Creates a pipeline of prompt -> LLM -> parser

# Async medication extraction method
async def extract_medication_details(natural_input):
    try:
        result = await medication_data_extraction_chain.ainvoke({
            "input": natural_input,
            "format_instructions": parser.get_format_instructions()
        })

        return result

    except Exception as e:
        print(f"Error: {e}")
        return None

# Defining a prompt template for medical questions
medical_question_prompt = PromptTemplate.from_template("""
You are a knowledgeable medical assistant.
Answer the following medical question concisely and accurately. If the question is outside your expertise, respond with "I'm sorry, I cannot answer that."

Question: "{input}"
""".strip())

# Defining a chain for medical questions
medical_question_chain = medical_question_prompt | llm # Creates a pipeline of prompt -> LLM

async def answer_medical_question(user_question):
    try:
        result = await medical_question_chain.ainvoke({
            "input": user_question
        })

        answer = result.content if hasattr(result, "content") else "Sorry, no answer was provided."
        print("Medical Question Answer:")
        print(answer)
        return answer

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your question."

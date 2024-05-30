from crewai import agent

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("google_API")
)

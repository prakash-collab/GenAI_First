import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="nvidia/nemotron-3-super-120b-a12b",
    temperature=0.7,
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

response = llm.invoke(
    "What is the capital of India?"
)

print("CONTENT:")
print(response.content)

# print("\nRESPONSE METADATA:")
# print(response.response_metadata)

# print("\nUSAGE METADATA:")
# print(response.usage_metadata)
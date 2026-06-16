"""Quick test of instructor with the API."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from config import API_KEY, LLM_BASE_URL, LLM_MODEL
from openai import OpenAI
import instructor
from pydantic import BaseModel, Field

print(f"API URL: {LLM_BASE_URL}")
print(f"Model: {LLM_MODEL}")
print("Creating instructor client...")

client = instructor.from_openai(
    OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL),
    mode=instructor.Mode.JSON,
)

class SimpleTest(BaseModel):
    name: str = Field(description="product name")
    version: str = Field(description="version")

print("Calling LLM with instructor...")
r = client.chat.completions.create(
    model=LLM_MODEL,
    response_model=SimpleTest,
    max_tokens=100,
    messages=[{"role": "user", "content": "Product: PT9L Infrared Thermometer V1.0"}],
)
print(f"Result: {r.model_dump()}")
print("SUCCESS!")

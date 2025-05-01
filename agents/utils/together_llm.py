# Import libraries

import sys
sys.path.append(r"C:\Users\shrey\anaconda3\envs\bot\Lib\site-packages")  # Adjust the path to your project structure

import json
import together
from together import Together

from typing import Any, Optional, Dict, List, Literal
from pydantic import Field, BaseModel, ValidationError
import os

##get environment Key
api_key = os.getenv("TOGETHER_API_KEY")

TOGETHER_API_KEY = api_key
client = Together(api_key= TOGETHER_API_KEY)


# Simple LLM call helper function
def run_llm(user_prompt : str, model : str, system_prompt : Optional[str] = None):
    """ Run the language model with the given user prompt and system prompt. """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    messages.append({"role": "user", "content": user_prompt})
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=4000,        
    )

    return response.choices[0].message.content

# Simple JSON mode LLM call helper function
def JSON_llm(user_prompt : str, schema : BaseModel, system_prompt : Optional[str] = None):
    """ Run a language model with the given user prompt and system prompt, and return a structured JSON object. """
    try:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": user_prompt})
        
        extract = client.chat.completions.create(
            messages=messages,
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            response_format={
                "type": "json_object",
                "schema": schema.model_json_schema(),
            },
        )
        
        response = json.loads(extract.choices[0].message.content)
        return response
        
    except ValidationError as e:
        raise ValueError(f"Schema validation failed: {str(e)}")
    

def together_chat_completion(prompt):
    """Run a serial chain of LLM calls to address the `input_query` 
    using a prompts specified in a list `prompt_chain`.

    Outputs the chain of responses from the LLM models.
    """
    response_chain = [] # Will store the responses from the LLM models
    response = run_llm(f"{prompt}", model='mistralai/Mixtral-8x7B-Instruct-v0.1')
    return response
